import json

def filter_user_first_conversations(dataset):
    filtered_dataset = []
    for item in dataset:
        if item['utterances'][0]['speaker'].lower() == 'user':
            filtered_dataset.append(item)
    return filtered_dataset

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        dataset = json.load(file)
    filtered_dataset = filter_user_first_conversations(dataset)
    with open(output_file, 'w') as file:
        json.dump(filtered_dataset, file, indent=4)

# Get the uploaded file name
input_file = "restaurant-search.json"

# Output file name
output_file = "1.json"

# Run the main function
main(input_file, output_file)
