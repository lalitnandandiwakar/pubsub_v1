import os
#import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/linux/Desktop/pubsub_v1/google_cloud_personal.json"
# Imports the Google Cloud client library

from google.cloud import pubsub_v1

# Instantiates a client

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(
    'diwakar-203006', 'my-new-topic_t1')

publisher.delete_topic(topic_path)

print('Topic deleted: {}'.format(topic_path))