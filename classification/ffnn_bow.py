import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Load and clean the dataset
df = pd.read_csv("songs_final422.csv")
df['bow_text'] = df['Stemmed No Stop Words'].apply(lambda x: ' '.join(eval(x)) if isinstance(x, str) else '')
df = df[(df['bow_text'] != '') & df['Genre'].notna()]

# Bag-of-Words vectorization
vectorizer = CountVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['bow_text']).toarray()

# Encode genres as one-hot targets
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['Genre'])
y_cat = to_categorical(y)

# Train/test split
X_train, X_test, y_train_cat, y_test_cat = train_test_split(X, y_cat, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the FFNN model
model = Sequential([
    Dense(128, input_dim=X_train_scaled.shape[1], activation='relu'),
    Dense(64, activation='relu'),
    Dense(y_cat.shape[1], activation='softmax')  # output layer
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train_scaled, y_train_cat, epochs=10, batch_size=32, validation_data=(X_test_scaled, y_test_cat))

# Evaluate performance
loss, accuracy = model.evaluate(X_test_scaled, y_test_cat)
print(f"Test Accuracy: {accuracy:.4f}")

# Predict probabilities on test set
y_pred_probs = model.predict(X_test_scaled)

# Convert one-hot predictions and true labels to class indices
y_pred_classes = np.argmax(y_pred_probs, axis=1)
y_true_classes = np.argmax(y_test_cat, axis=1)

# Generate and print classification report
print("\nClassification Report:\n")
print(classification_report(y_true_classes, y_pred_classes, target_names=label_encoder.classes_))

cm = confusion_matrix(y_true_classes, y_pred_classes)

# Display confusion matrix with genre labels
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
disp.plot(cmap='Blues', xticks_rotation=45)
plt.title("Confusion Matrix for Feed Forward Neural Network, Bag-Of-Words")
plt.tight_layout()
plt.show()