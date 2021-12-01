from kafka import KafkaConsumer
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mythical-patrol-219308-0de924333ef2.json"


def upload_data_to_big_query(topic, table_name):
    # find table by name
    client = bigquery.Client(project='mythical-patrol-219308')
    try:
        client.get_table(table_name)
    # if table not exists, create a table
    except NotFound:
        schema = [
            bigquery.SchemaField("city", "STRING", mode="Nullable"),
            bigquery.SchemaField("state", "STRING", mode="Nullable"),
            bigquery.SchemaField("avg_donation", "FLOAT", mode="Nullable"),
        ]
        table = bigquery.Table(table_name, schema=schema)
        client.create_table(table)

    # create a consumer
    consumer = KafkaConsumer(bootstrap_servers='34.91.110.15:9092',
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=10000)  # use YOUR EXTERNAL IP
    # subscribe to topic
    consumer.subscribe(topics=[topic])

    # save topic in the table
    for msg in consumer:
        if msg.key is not None and msg.value is not None:
            keys = msg.key.decode("utf-8").split()
            value = float(msg.value.decode("utf-8"))
            row = {"city": keys[0], "state": keys[1], "avg_donation": value}
            errors = client.insert_rows_json(table_name, [row])
            if not errors:
                print("Added data")
            else:
                print("Something went wrong: {}".format(errors))


if __name__ == '__main__':
    upload_data_to_big_query('donor_result', "mythical-patrol-219308.assignment_dataset.result_donor")
