#!/usr/bin/python
# python version must be => 3.5
import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
project_id = "pubsubdemo-245111"               #set to your specific value
topic_name = "trydemo"                         #set to your specific value
topic_path = publisher.topic_path(project_id, topic_name)
print (topic_path)
#topic = publisher.create_topic(topic_path)
print('Message is going to publish: {}'.format(topic_path))
message = publisher.publish(topic_path, b'pubsub damn', spam='eggs')
