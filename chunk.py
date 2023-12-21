import textwrap
import json

def create_json_file(chunks, filename="output.json"):
    """
    Creates a JSON file where each chunk of text is stored as a separate entry in a conversation format.

    :param chunks: List of text chunks to be included in the JSON file.
    :param filename: Name of the JSON file to be created.
    """
    conversation = []
    speaker_name = "shimmer"  # Assuming a fixed speaker name for all chunks

    for chunk in chunks:
        # Creating a dictionary for each chunk
        print("chunk " + chunk)
        entry = {
            "speaker": speaker_name,
            "text": chunk
        }
        conversation.append(entry)

    # Creating the final JSON structure
    json_data = {
        "conversation": conversation
    }

    # Writing to a file
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=2)

def split_text_into_chunks(text, max_length):
    """
    Splits a text into chunks each of which has a maximum length of max_length.
    It uses the textwrap library to ensure that words are not broken in the middle.

    :param text: The text to be split.
    :param max_length: The maximum length of each chunk.
    :return: A list of text chunks.
    """
    # Splitting the text into lines, each having a length of max_length
    wrapped_text = textwrap.wrap(text, max_length)

    return wrapped_text

# Example text (for demonstration, a shorter text is used here)
example_text = """
Hi. For those of you who don't know me, my name is Steve Jobs, and this is the first of many chalk talks we're going to have here together. The subject to this one is essential: who is our target customer? Why are they selecting our products over our competitors? What distribution channels are we going to use to reach these customers? A lot of light bulbs have come on over the last 90 days. I've had the good fortune to be with many of you out in the field, meaning customers get first-hand information about what they're doing with our products. You have fed a lot of information to the management of this company. We've done a lot of thinking and looked at the data, and all of a sudden, out of this data, some very, very important things have come to light. I want to share them with you today. Historically, We've struggled to figure out exactly who our customers are and we want to show you why. When we first look at the workstation marketplace, look something like this and the biggest player, as you know, in the workstation marketplace is Sun. The second biggest player is HP Apollo. The third biggest player is a Deck, and IBM, with the RS6000, is also in the game. And then, outside the workstation marketplace, the huge market for PCs and Macintoshes, the traditional personal computer market. We looked at the workstation marketplace and said, wow, we have multitasking. We have great networking, just like the workstations. We use Unix. Hi. For those of you who don't know me, my name is Steve Jobs, and this is the first of many chalk talks we're going to have here together. The subject to this one is essential: who is our target customer? Why are they selecting our products over our competitors? What distribution channels are we going to use to reach these customers? A lot of light bulbs have come on over the last 90 days. I've had the good fortune to be with many of you out in the field, meaning customers get first-hand information about what they're doing with our products. You have fed a lot of information to the management of this company. We've done a lot of thinking and looked at the data, and all of a sudden, out of this data, some very, very important things have come to light. I want to share them with you today. Historically, We've struggled to figure out exactly who our customers are and we want to show you why. When we first look at the workstation marketplace, look something like this and the biggest player, as you know, in the workstation marketplace is Sun. The second biggest player is HP Apollo. The third biggest player is a Deck, and IBM, with the RS6000, is also in the game. And then, outside the workstation marketplace, the huge market for PCs and Macintoshes, the traditional personal computer market. We looked at the workstation marketplace and said, wow, we have multitasking. We have great networking, just like the workstations. We use Unix. Hi. For those of you who don't know me, my name is Steve Jobs, and this is the first of many chalk talks we're going to have here together. The subject to this one is essential: who is our target customer? Why are they selecting our products over our competitors? What distribution channels are we going to use to reach these customers? A lot of light bulbs have come on over the last 90 days. I've had the good fortune to be with many of you out in the field, meaning customers get first-hand information about what they're doing with our products. You have fed a lot of information to the management of this company. We've done a lot of thinking and looked at the data, and all of a sudden, out of this data, some very, very important things have come to light. I want to share them with you today. Historically, We've struggled to figure out exactly who our customers are and we want to show you why. When we first look at the workstation marketplace, look something like this and the biggest player, as you know, in the workstation marketplace is Sun. The second biggest player is HP Apollo. The third biggest player is a Deck, and IBM, with the RS6000, is also in the game. And then, outside the workstation marketplace, the huge market for PCs and Macintoshes, the traditional personal computer market. We looked at the workstation marketplace and said, wow, we have multitasking. We have great networking, just like the workstations. We use Unix. Hi. For those of you who don't know me, my name is Steve Jobs, and this is the first of many chalk talks we're going to have here together. The subject to this one is essential: who is our target customer? Why are they selecting our products over our competitors? What distribution channels are we going to use to reach these customers? A lot of light bulbs have come on over the last 90 days. I've had the good fortune to be with many of you out in the field, meaning customers get first-hand information about what they're doing with our products. You have fed a lot of information to the management of this company. We've done a lot of thinking and looked at the data, and all of a sudden, out of this data, some very, very important things have come to light. I want to share them with you today. Historically, We've struggled to figure out exactly who our customers are and we want to show you why. When we first look at the workstation marketplace, look something like this and the biggest player, as you know, in the workstation marketplace is Sun. The second biggest player is HP Apollo. The third biggest player is a Deck, and IBM, with the RS6000, is also in the game. And then, outside the workstation marketplace, the huge market for PCs and Macintoshes, the traditional personal computer market. We looked at the workstation marketplace and said, wow, we have multitasking. We have great networking, just like the workstations. We use Unix. 
"""

# Splitting the example text into chunks
max_length = 4096
chunks = split_text_into_chunks(example_text, max_length)

# Creating the JSON file
create_json_file(chunks, "jobs.json")

print(chunks)