import json

import json

def filter_conversations(json_data):
    filtered_data = []
    for conversation in json_data:
        utterances = conversation["utterances"]
        if utterances[0]["speaker"] == "USER" and utterances[-1]["speaker"] == "ASSISTANT":
            filtered_data.append(conversation)
    return filtered_data
# Load JSON data from file
with open('1.json', 'r') as f:
    json_data = json.load(f)

# Extract user-assistant utterances
transformed_data = filter_conversations(json_data)

# Save extracted data to a new file
with open('2.json', 'w') as f:
    json.dump(transformed_data, f, indent=2)

print("Extraction complete. Output saved to '2.json'.")
