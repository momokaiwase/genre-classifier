from mistralai import Mistral
import pandas as pd
import time #needed to sleep() between requests
from sklearn.metrics import classification_report

client = Mistral(api_key="Td241z6rBzd1cQbBYETVT8l26hZIxqQo")

MODEL = "mistral-large-latest"

df = pd.read_csv('click_test.csv') #replace with test set (data labeled with text, and label)
sampled_df = df.sample(n=100, random_state=42)

##PREDICT CLASSIFICATIONS WiTH MISTRAL

# to store results (Mistral's responses)
predictions = []

# Loop through the headlines in the subset of 100 headlines we made above.
# This code is just how to go through a column in a pandas dataframe.
for index, row in sampled_df.iterrows():
  lyrics = row['text']

  # Create the prompt
  prompt = f"What genre are the following lyrics? Answer only with '1' (rap), '2' (pop), '3' (R&B), '4' (rock), '5' (country), '6' (EDM): {lyrics}"

  # Put it in the MESSAGES variable that will get passed
  # to Mistral.
  MESSAGES = [{"role": "user", "content": prompt}]

  # This the call to Mistral with that prompt.
  completion = client.chat.complete(
      model= MODEL,
      messages = MESSAGES
  )

  print(prompt)

  print(completion.choices[0].message.content) #response

  # This saves out the response to our list of predictions so that
  # we can evaluate the predictions of the LLM in the next code block.
  predictions.append(completion.choices[0].message.content)

  # This will pause the execution for 5 seconds so that we don't
  # exceed our rate limit with Mistral
  time.sleep(5)

##EVALUATE CLASSIFICATIONS

# turn the predictions into integers
npredictions = [int(x) for x in predictions]

# print a classification report
print(classification_report(npredictions, sampled_df["label"]))