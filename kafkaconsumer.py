from kafka import KafkaConsumer
consumer = KafkaConsumer('Topic1', bootstrap_servers='3.17.156.95:9092')
for msg in consumer:
    print (msg.key, msg.value)
