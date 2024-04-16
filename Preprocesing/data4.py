import json

def convert_to_qa(data):
  """
  Converts a JSON conversation dataset to question-answer format.

  Args:
    data: A list of dictionaries representing conversations.

  Returns:
    A list of dictionaries with "question" and "answer" keys.
  """
  qa_list = []
  for conversation in data:
    for utterance in conversation["utterances"]:
      if utterance["speaker"] == "USER":
        question = utterance["text"]
      elif utterance["speaker"] == "ASSISTANT":
        answer = utterance["text"]
        if question and answer:
          qa_list.append({"question": question, "answer": answer})
          question = None  # Reset question for next assistant utterance
  return qa_list

# Load your JSON data
with open("3.json", "r") as f:
  data = json.load(f)

# Convert to question-answer format
qa_data = convert_to_qa(data)

# Print the converted data (optional)

# Writing the rearranged data to a JSON file
with open("restaurant.json", "w") as outfile:
    json.dump(qa_data, outfile, indent=2)
