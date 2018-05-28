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

for n in range(1, 10):
    data = u'Message number {}'.format(n)
    # Data must be a bytestring
    data = data.encode('utf-8')
    publisher.publish(topic_path, data=data)

print('Published messages.')
