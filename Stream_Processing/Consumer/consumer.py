from kafka import KafkaConsumer, TopicPartition


def read_from_topic(kafka_consumer, topic):
    kafka_consumer.subscribe(topics=[topic])
    for msg in kafka_consumer:
        if msg.key is not None and msg.value is not None:
            print(msg.key.decode("utf-8"), msg.value.decode("utf-8"))


def read_from_topic_with_partition(kafka_consumer, topic):
    kafka_consumer.assign([TopicPartition(topic, 1)])
    for msg in kafka_consumer:
        print(msg)


def read_from_topic_with_partition_offset(kafka_consumer, topic):
    partition = TopicPartition(topic, 0)
    kafka_consumer.assign([partition])
    last_offset = kafka_consumer.end_offsets([partition])[partition]
    for msg in kafka_consumer:
        if msg.offset == last_offset - 1:
            break


if __name__ == '__main__':
    consumer = KafkaConsumer(bootstrap_servers='34.91.110.15:9092',
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=10000) # use YOUR EXTERNAL IP
    print(consumer.topics())
    read_from_topic(consumer, 'donor_result')
