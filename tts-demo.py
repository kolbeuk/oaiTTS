#!/usr/bin/env python
# coding: utf-8

from openai import OpenAI
import json

# To run this script, you need an API key from OpenAI. 
# Obtain the key from https://openai.com/blog/openai-api and set it up as per OpenAI's documentation.
# Initialize the OpenAI client
client = OpenAI()

# Step 1: Read the conversation data from a JSON file. This JSON file contains the conversation,
# with each entry comprising a 'speaker' and their corresponding 'text'.
with open('conversation.json', 'r') as file:
    data = json.load(file)

# Iterate over the conversation entries and generate audio for each segment.
for i, entry in enumerate(data['conversation']):
    speaker = entry['speaker']
    text = entry['text']

    # Generate speech from text using the TTS service.
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice=speaker,  # Ensure the 'voice' parameter corresponds to the TTS service's available voices.
            input=text
        )
        # Save the generated audio to an MP3 file, with a unique filename for each segment.
        filename = f"fivewhyss{i+1}.mp3"  # Filenames will be output1.mp3, output2.mp3, etc.
        response.stream_to_file(filename)
        print(f"Saved audio segment {i+1} to {filename}")
    except openai.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
