import json

def filter_last_speaker_assistant(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    filtered_data = []
    for conversation in data:
        messages = conversation['messages']
        if messages and messages[-1]['role'] == 'assistant':
            filtered_data.append(conversation)

    with open(output_file, 'w') as f:
        json.dump(filtered_data, f, indent=2)

if __name__ == "__main__":
    input_file = "3.json"
    output_file = "4.json"
    filter_last_speaker_assistant(input_file, output_file)
