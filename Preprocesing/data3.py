import json 
def rearrange_utterances(json_data):
    for conversation in json_data:
        utterances = conversation["utterances"]
        rearranged_utterances = []
        current_speaker = None
        for utterance in utterances:
            if current_speaker is None or utterance["speaker"] != current_speaker:
                rearranged_utterances.append(utterance)
                current_speaker = utterance["speaker"]
        conversation["utterances"] = rearranged_utterances
    return json_data

# Your JSON data
with open('2.json', 'r') as f:
    json_data = json.load(f)

rearranged_json_data = rearrange_utterances(json_data)

# Writing the rearranged data to a JSON file
with open("3.json", "w") as outfile:
    json.dump(rearranged_json_data, outfile, indent=2)
