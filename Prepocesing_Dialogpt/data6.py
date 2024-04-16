import json
import csv

# Load JSON data
with open('5.json') as f:
    data = json.load(f)

# Initialize lists to store user and assistant messages
user_messages = []
assistant_messages = []

# Extract user and assistant messages
for conversation in data:
    for message in conversation['messages']:
        if message['role'] == 'user':
            user_messages.append(message['content'])
        elif message['role'] == 'assistant':
            assistant_messages.append(message['content'])

# Write to CSV
with open('sation.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['User Content', 'Assistant Content'])
    for user, assistant in zip(user_messages, assistant_messages):
        writer.writerow([user, assistant])

print("CSV file created successfully!")
