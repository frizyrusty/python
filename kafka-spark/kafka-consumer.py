from kafka import KafkaConsumer
import sys
bootstrap_servers = ['192.168.43.250:9092']
topicName = 'test2'
consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
auto_offset_reset = 'earliest')
for message in consumer:
	print (message.value)
