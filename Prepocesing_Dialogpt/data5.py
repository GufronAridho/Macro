import json
import random

def select_json_objects_random(input_file, output_file, num_objects):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Shuffle the data randomly
    random.shuffle(data)

    # Select the specified number of random objects
    selected_data = data[:num_objects]

    with open(output_file, 'w') as f:
        json.dump(selected_data, f, indent=4)

input_file = "4.json"
output_file = "5.json"
num_objects_to_select = 400

select_json_objects_random(input_file, output_file, num_objects_to_select)
