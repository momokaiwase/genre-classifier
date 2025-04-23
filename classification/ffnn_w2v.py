import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Load dataset
df = pd.read_csv("songs_final422.csv")

# Prepare token lists from stemmed lyrics
df['tokens'] = df['Stemmed No Stop Words'].apply(lambda x: eval(x) if isinstance(x, str) else [])
df = df[(df['tokens'].apply(len) > 0) & df['Genre'].notna()]

# Train Word2Vec model
w2v_model = Word2Vec(sentences=df['tokens'], vector_size=100, window=5, min_count=1, workers=4, seed=42)

# Represent each song as the average of its word vectors
def average_word_vectors(tokens, model, vector_size):
    vectors = [model.wv[token] for token in tokens if token in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(vector_size)

X = np.array([average_word_vectors(tokens, w2v_model, 100) for tokens in df['tokens']])

# Encode genres
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['Genre'])
y_cat = to_categorical(y)

# Train/test split
X_train, X_test, y_train_cat, y_test_cat = train_test_split(X, y_cat, test_size=0.2, random_state=42)

# Normalize
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build FFNN
model = Sequential([
    Dense(64, input_dim=X_train_scaled.shape[1], activation='relu'),
    Dense(32, activation='relu'),
    Dense(y_cat.shape[1], activation='softmax')
])

# Compile and train
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train_scaled, y_train_cat, epochs=10, batch_size=32, validation_data=(X_test_scaled, y_test_cat))

# Evaluate
loss, accuracy = model.evaluate(X_test_scaled, y_test_cat)
print(f"Test Accuracy: {accuracy:.4f}")

# Predict on test data
y_pred_probs = model.predict(X_test_scaled)
y_pred_classes = np.argmax(y_pred_probs, axis=1)
y_true_classes = np.argmax(y_test_cat, axis=1)

print("\nClassification Report:\n")
print(classification_report(y_true_classes, y_pred_classes, target_names=label_encoder.classes_))

# Generate confusion matrix
cm = confusion_matrix(y_true_classes, y_pred_classes)

# Display confusion matrix with labels
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
disp.plot(cmap='Blues', xticks_rotation=45)
plt.title("Confusion Matrix for Feed Forward Neural Network, Word2Vec")
plt.show()