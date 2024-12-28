# Step 1: Import necessary modules
import os
import json
from openai import OpenAI
from data import training_data, validation_data
from dotenv import load_dotenv

# Step 2: Initialize the OpenAI client with the API key from environment variables
load_dotenv()
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
)

# Step 3: Define the names of the training and validation data files
training_file_name = "training_data.jsonl"
validation_file_name = "validation_data.jsonl"

# Step 4: Function to prepare data and write it to a JSONL file
def prepare_data(dictionary_data: list[dict], final_file_name):
    with open(final_file_name, "w") as outfile:
        for entry in dictionary_data:
            json.dump(entry, outfile)
            outfile.write("\n")

# Step 5: Call the prepare_data function for both training and validation data
prepare_data(training_data, training_file_name)
prepare_data(validation_data, validation_file_name)

# Step 6: Upload the training data file to OpenAI and get the file ID
training_file_id = client.files.create(
    file=open(training_file_name, "rb"),
    purpose="fine-tune"
)

# Step 7: Upload the validation data file to OpenAI and get the file ID
validation_file_id = client.files.create(
    file=open(validation_file_name, "rb"),
    purpose="fine-tune"
)

# Step 8: Print the file IDs for reference
print("Training file ID:", training_file_id)
print("Validation file ID:", validation_file_id)
#import pdb; pdb.set_trace()

# Step 9: Create a fine-tuning job with the uploaded files and specific hyperparameters
response = client.fine_tuning.jobs.create(
    model="gpt-4o-mini-2024-07-18",
    training_file=training_file_id.id,
    validation_file=validation_file_id.id,
    hyperparameters={
        "n_epochs": 15,
        "batch_size": 3,
        "learning_rate_multiplier": 0.3,
    }
)

# Step 10: Retrieve the job ID and status from the response
job_id = response.id
status = response.status

# Step 11: Print the job ID and initial status
print("Fine-tuning model with Job ID:", job_id)
print("Training Response:", response)
print("Training status:", status)

# Step 12: Import signal and datetime modules for handling interruptions and timestamps
import signal
from datetime import datetime

# Step 13: Define a signal handler to manage interruptions
def signal_handler(sig, frame):
    status = client.fine_tuning.jobs.retrieve(job_id=job_id).status
    print("Stream interrupted. Fine-tuning job status:", status)
    return

# Step 14: Print the start of event streaming
print("Streaming events for fine-tuning job:", job_id)

# Step 15: Set up the signal handler for keyboard interruptions
signal.signal(signal.SIGINT, signal_handler)

# Step 16: List events for the fine-tuning job and print them with timestamps
events = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id)
try:
    for event in events:
        print(f"{datetime.fromtimestamp(event.created_at)} - {event.event_type} - {event.message}")
except Exception as e:
    print("Stream interrupted (client disconnected):", e)

# Step 17: Import time module for sleep function
import time

# Step 18: Check the status of the fine-tuning job and wait if it is not in a terminal state
status = client.fine_tuning.jobs.retrieve(job_id).status
while status not in ["succeeded", "failed", "cancelled"]:
    print("Waiting for fine-tuning job to complete... status:", status)
    time.sleep(3)
    status = client.fine_tuning.jobs.retrieve(job_id).status
print(f"Fine-tuning job {job_id} completed. Status: {status}")

# Step 19: Print the status of other fine-tuning jobs in the subscription
print("Other fine-tuning jobs in the subscription:", client.fine_tuning.jobs.list())

# Step 20: Retrieve and print the ID of the fine-tuned model
job_response = client.fine_tuning.jobs.retrieve(job_id)
fine_tuned_model_id = job_response.fine_tuned_model
print("Fine-tuned model ID:", fine_tuned_model_id)
