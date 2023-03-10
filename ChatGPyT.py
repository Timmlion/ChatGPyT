import os
import openai
import keyboard
 
# Load your API key from an environment variable or secret management service
openai.api_key = "klucz API"
exit_keys = ['ctrl', 'c']
messageArray = []
responseText = ""
 
while True:
# Prompt the user for input
  user_input = input("User: ")
 
  messageArray.append({"role": "user", "content": user_input})
 
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messageArray
  )
  responseText = response['choices'][0]['message']['content']
  messageArray.append({"role":"assistant", "content": responseText})
 
  print("Response: " + responseText)
