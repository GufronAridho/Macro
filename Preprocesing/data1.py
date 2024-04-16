import json

def transform_json(json_data):
    transformed_data = []
    for conv in json_data:
        utterances = conv.get('utterances', [])
        conv_data = []
        for utterance in utterances:
            utterance_data = {
                'index': utterance.get('index', None),
                'speaker': utterance.get('speaker', None),
                'text': utterance.get('text', None)
            }
            conv_data.append(utterance_data)
        transformed_data.append({
            'conversation_id': conv.get('conversation_id', None),
            'instruction_id': conv.get('instruction_id', None),
            'utterances': conv_data
        })
    return transformed_data

# Load JSON data from file
with open('restaurant-search.json', 'r') as f:
    json_data = json.load(f)

# Transform JSON data
transformed_data = transform_json(json_data)

# Save transformed data to a new file
with open('1.json', 'w') as f:
    json.dump(transformed_data, f, indent=2)

print("Transformation complete. Output saved to '1.json'.")
