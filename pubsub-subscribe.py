#!/usr/bin/python

import os
import pprint
from google.cloud import pubsub_v1

# required variable project_id , pubsub topic name, pubsub subscription name
subscriber = pubsub_v1.SubscriberClient()
project_id = "pubsubdemo-245111"
topic = "trydemo"
sub = "trydemo-subscription"

# Creating topic and subscription path related to pubsub topic
topic_path = subscriber.topic_path(project_id,topic)
subscription_path = subscriber.subscription_path(project_id, sub)
print (topic_path)
print (subscription_path)

#use this code to only create subscription for mentioned topic

#subname = subscriber.create_subscription(name=subscription_path,topic=topic_path)
#print (subname)

def callback(message):
    print(message.data)
    message.ack()
future = subscriber.subscribe(subscription_path, callback)
print (future)
#future.result()
#pprint(vars(future))

