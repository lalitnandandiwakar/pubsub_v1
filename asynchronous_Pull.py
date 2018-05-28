import os
import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/linux/Desktop/pubsub_v1/google_cloud_personal.json"
# Imports the Google Cloud client library

from google.cloud import pubsub_v1

# Instantiates a client
publisher = pubsub_v1.PublisherClient()

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    'diwakar-203006', 'sub_v1')

def callback(message):
    print('Received message: {}'.format(message))
    message.ack()

subscriber.subscribe(subscription_path, callback=callback)

# The subscriber is non-blocking, so we must keep the main thread from
# exiting to allow it to process messages in the background.
print('Listening for messages on {}'.format(subscription_path))
while True:
    time.sleep(60)