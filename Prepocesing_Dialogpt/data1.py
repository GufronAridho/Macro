import json

def convert_to_desired_format(data):
    messages = []
    current_role = None
    current_content = None
    for utterance in data:
        role = utterance['speaker'].lower()
        content = utterance['text'].lower()  # Convert text to lowercase
        if current_role is None or current_role != role:
            if current_role is not None:
                messages.append({"role": current_role, "content": current_content})
            current_role = role
            current_content = content
        else:
            current_content += " " + content
    if current_role is not None:
        messages.append({"role": current_role, "content": current_content})
    return messages

def transform_data(dataset):
    transformed_data = []
    for item in dataset:
        instruction_id = item["instruction_id"]
        if instruction_id.startswith("restaurant") or instruction_id.startswith("lunch") or instruction_id.startswith("hungry") or instruction_id.startswith("dinner")or instruction_id.startswith("dessert"):
            role = "system"
            content = "you are a diligent assistant,your task is to discover and recommend food options to the user.you will continuously inquire about user preferences until they are fully satisfied with your recommendations.{instruction_id.split('-')[1]}"
            transformed_item = {
                "messages": [{"role": role, "content": content}] + convert_to_desired_format(item['utterances']),
            }
            transformed_data.append(transformed_item)
        else:
            for utterance in item['utterances']:
                role = utterance['speaker'].lower()
                content = utterance['text'].lower()  # Convert text to lowercase
                transformed_item = {
                    "messages": [{"role": "system", "content": content}] + convert_to_desired_format(item['utterances']),
                }
                transformed_data.append(transformed_item)
    return transformed_data

# Load the dataset from JSON
with open('1.json', 'r') as file:
    dataset = json.load(file)

# Apply the transformation
transformed_dataset = transform_data(dataset)

# Save the transformed dataset to JSON
with open('2.json', 'w') as file:
    json.dump(transformed_dataset, file, indent=4)