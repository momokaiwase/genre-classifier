from mistralai import Mistral
import pandas as pd
import time #needed to sleep() between requests
from sklearn.metrics import classification_report


client = Mistral(api_key="Td241z6rBzd1cQbBYETVT8l26hZIxqQo")

MODEL = "mistral-large-latest"

df = pd.read_csv('raw_lyrics_test_dataset.csv') #replace with test set (data labeled with text, and label)
sampled_df = df.sample(n=100, random_state=42)

##PREDICT CLASSIFICATIONS WiTH MISTRAL

# to store results (Mistral's responses)
predictions = []

# Loop through the headlines in the subset of 100 headlines we made above.
# This code is just how to go through a column in a pandas dataframe.
for index, row in sampled_df.iterrows():
  lyrics = row['Lyrics']

  # Create the prompt
  prompt = f"What genre are the following lyrics? Answer only with '0' (Pop), '1' (Rock), '2' (R&B), '3' (Country), '4' (EDM), or '5' (Rap): {lyrics}."

  # Put it in the MESSAGES variable that will get passed
  # to Mistral.
  MESSAGES = [{"role": "user", "content": prompt}]

  # This the call to Mistral with that prompt.
  completion = client.chat.complete(
      model= MODEL,
      messages = MESSAGES
  )

  #print(prompt)

  #print(completion.choices[0].message.content) #response

  # This saves out the response to our list of predictions so that
  # we can evaluate the predictions of the LLM in the next code block.
  predictions.append(completion.choices[0].message.content)

  # This will pause the execution for 5 seconds so that we don't
  # exceed our rate limit with Mistral
  time.sleep(5)

print(predictions)
##EVALUATE CLASSIFICATIONS

# turn the predictions into integers
npredictions = [int(x) for x in predictions]

# print a classification report
print(classification_report(npredictions, sampled_df["Genre_Label"]))