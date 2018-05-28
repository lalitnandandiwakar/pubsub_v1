import os
#import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/linux/Desktop/pubsub_v1/google_cloud_personal.json"
# Imports the Google Cloud client library

from google.cloud import pubsub_v1
subscriber = pubsub_v1.SubscriberClient()
topic_path = subscriber.topic_path('diwakar-203006', 'my-new-topic_t1')
subscription_path = subscriber.subscription_path(
    'diwakar-203006', 'subscription_name')

subscription = subscriber.create_subscription(
    subscription_path, topic_path)

print('Subscription created: {}'.format(subscription))