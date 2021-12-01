from kafka import KafkaProducer
from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mythical-patrol-219308-0de924333ef2.json"


def kafka_python_producer_sync(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8'))
    print("Sending " + msg)
    producer.flush(timeout=60)


def success(metadata):
    print(metadata.topic)


def error(exception):
    print(exception)


def kafka_python_producer_async(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8')).add_callback(success).add_errback(error)
    producer.flush()


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='34.91.110.15:9092')  # use YOUR EXTERNAL IP

    client = storage.Client(project='mythical-patrol-219308')
    bucket = client.get_bucket('in_assignment_2')       # Bucket Name
    blob_donation = bucket.blob('Donations.csv')        # blob
    blob_donation.download_to_filename('Donations.csv')

    with open('Donations.csv') as f_donation:
        lines_donation = f_donation.readlines()

    # send data to topic
    for line in lines_donation:
        kafka_python_producer_sync(producer, line, 'data')

    f_donation.close()
