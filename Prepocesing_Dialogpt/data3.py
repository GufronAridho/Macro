import json

def transform_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    transformed_data = []
    for conversation in data:
        messages = []
        for message in conversation['messages']:
            if message['role'] != 'system':
                messages.append({
                    'role': message['role'],
                    'content': message['content']
                })
        transformed_data.append({'messages': messages})

    with open(output_file, 'w') as f:
        json.dump(transformed_data, f, indent=2)

if __name__ == "__main__":
    input_file = "2.json"
    output_file = "3.json"
    transform_json(input_file, output_file)
