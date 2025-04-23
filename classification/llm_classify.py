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

  # Create the prompt (zero-shot)
  prompt = f"What genre are the following lyrics? Answer only with '0' (Pop), '1' (Rock), '2' (R&B), '3' (Country), '4' (EDM), or '5' (Rap): {lyrics}."
  
  #tried few-shot but it did not perform better
  '''
  prompt = f"""
  What genre are the following lyrics? 
  The lyrics 'Lyrics[Intro] Oh-oh-oh  [Verse 1] If you ever find yourself stuck in the middle of the sea I'll sail the world to find you If you ever find yourself lost in the dark and you can't see I'll be the light to guide you  [Pre-Chorus] We find out what we're made of When we are called to help our friends in need  [Chorus] You can count on me like one, two, three, I'll be there And I know when I need it I can count on you like four, three, two and you'll be there 'Cause that's what friends are s'posed to do, oh, yeah  [Post-Chorus] Ooh-ooh-ooh-ooh-ooh Ooh-ooh-ooh-ooh-ooh Ooh, yeah, yeah  [Verse 2] If you're tossin' and you're turnin' and you just can't fall asleep I'll sing a song beside you And if you ever forget how much you really mean to me Everyday, I will remind you, oh   [Pre-Chorus] We find out what we're made of When we are called to help our friends in need  [Chorus] You can count on me like one, two, three, I'll be there And I know when I need it I can count on you like four, three, two and you'll be there 'Cause that's what friends are s'posed to do, oh, yeah  [Post-Chorus] Ooh-ooh-ooh-ooh-ooh Ooh-ooh-ooh-ooh-ooh Ooh, yeah, yeah  [Bridge] You'll always have my shoulder when you cry I'll never let go, never say goodbye  [Chorus] You know you can count on me like one, two, three, I'll be there And I know when I need it I can count on you like four, three, two and you'll be there 'Cause that's what friends are s'posed to do, oh, yeah  [Post-Chorus] Ooh-ooh-ooh-ooh-ooh Ooh-ooh-ooh-ooh-ooh Ooh   [Outro] You can count on me 'cause I can count on you...' are in genre Pop '0'. 
  The lyrics 'LyricsContinuing the existential themes of A Rush of Blood to the Head, “Clocks” opens with a haunting piano melody into Chris Martin’s falsetto vocals.  The song concerns the paradox facing humanity: an obsession… Read More [Verse 1] The lights go out, and I can't be saved Tides that I tried to swim against Have brought me down upon my knees Oh, I beg, I beg and plead, singin' Come out of things unsaid Shoot an apple off my head, and a Trouble that can't be named A tiger's waitin' to be tamed, singin' are in genre Rock '1'.
  Do not give an explanation. Answer only with '0' (Pop), '1' (Rock), '2' (R&B), '3' (Country), '4' (EDM), or '5' (Rap): {lyrics}."""
  '''

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