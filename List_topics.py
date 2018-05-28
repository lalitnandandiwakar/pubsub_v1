import os
#import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/linux/Desktop/pubsub_v1/google_cloud_personal.json"
# Imports the Google Cloud client library

from google.cloud import pubsub_v1

# Instantiates a client

publisher = pubsub_v1.PublisherClient()
project_path = publisher.project_path('diwakar-203006')

for topic in publisher.list_topics(project_path):
    print(topic)

