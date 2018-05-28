import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/linux/Desktop/pubsub_v1/google_cloud_personal.json"
# Imports the Google Cloud client library

from google.cloud import pubsub_v1

# Instantiates a client
publisher = pubsub_v1.PublisherClient()

# The resource path for the new topic contains the project ID
# and the topic name.
topic_path = publisher.topic_path(
    'diwakar-203006', 'my-new-topic_v1')

# Create the topic.
topic = publisher.create_topic(topic_path)

print('Topic created: {}'.format(topic))