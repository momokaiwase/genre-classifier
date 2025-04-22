import os
os.environ["WANDB_DISABLED"] = "true"

clickbait = load_dataset('csv',data_files={'train': '/content/drive/MyDrive/lab8/click_train.csv',
                                           'test': '/content/drive/MyDrive/lab8/click_test.csv'})

small_train_dataset = imdb["train"].shuffle(seed=42).select([i for i in list(range(3000))])
small_test_dataset = imdb["test"].shuffle(seed=42).select([i for i in list(range(300))])

print("Text:", small_train_dataset[0]["text"])
print("Label:", small_train_dataset[0]["label"])

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def preprocess_function(examples):
  return tokenizer(examples["text"], truncation=True)

# (removing batched=True)
tokenized_small_train = small_train_dataset.map(preprocess_function)
tokenized_small_test = small_test_dataset.map(preprocess_function)

# Let's look at the first training sentence

print(tokenized_small_train)

print("Text:", tokenized_small_train[0]["text"])
print("Label:", tokenized_small_train[0]["label"])
print("Input IDs:", tokenized_small_train[0]["input_ids"])
print("Attention Mask:", tokenized_small_train[0]["attention_mask"])

# Convert token IDs back to tokens
tokens = tokenizer.convert_ids_to_tokens(tokenized_small_train[0]["input_ids"])
print("Tokenized text:", tokens)

from transformers import DataCollatorWithPadding
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

import numpy as np
from evaluate import load


def compute_metrics(eval_pred):
   load_accuracy = load("accuracy")
   load_f1 = load("f1")

   logits, labels = eval_pred
   predictions = np.argmax(logits, axis=-1)
   accuracy = load_accuracy.compute(predictions=predictions, references=labels)["accuracy"]
   f1 = load_f1.compute(predictions=predictions, references=labels)["f1"]
   return {"accuracy": accuracy, "f1": f1}

training_args = TrainingArguments(
    output_dir="/content/drive/MyDrive/lab8/results",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=5,
    weight_decay=0.01,
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_small_train,
    eval_dataset=tokenized_small_test,
    processing_class=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()

trainer.evaluate()