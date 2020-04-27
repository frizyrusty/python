from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='192.168.43.250:9092')
producer.send('test', b'Hello, World!')
producer.send('test', key=b'message-two', value=b'This is Kafka-Python')

