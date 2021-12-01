from flask import Flask, render_template, url_for
from google.cloud import bigquery
from resources.get_data import download_data, create_plot
import os

app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mythical-patrol-219308-0de924333ef2.json"


@app.route('/stream_processing_dashboard', methods=['GET'])
def stream_processing():  # put application's code here
    table_id = os.environ['STREAM_TABLE_ID']
    stream_schema = [
        bigquery.SchemaField("city", "STRING"),
        bigquery.SchemaField("state", "STRING"),
        bigquery.SchemaField("avg_donation", "FLOAT"),
    ]
    donor_df = download_data(table_id, stream_schema)
    create_plot(donor_df,
                columns=["city", "avg_donation"],
                sort_column='avg_donation',
                index_column='city',
                plt_name='3',
                title="5 top cities with the highest donation amount"
                )
    return render_template('Stream.html')


@app.route('/batch_processing_dashboard', methods=['GET'])
def batch_processing():  # put application's code here
    table_id = os.environ['BATCH_TABLE_ID']

    batch_schema = [
        bigquery.SchemaField("School_City", "STRING"),
        bigquery.SchemaField("School_Name", "STRING"),
        bigquery.SchemaField("total_donation_amount", "FLOAT"),
        bigquery.SchemaField("school_category", "STRING"),
    ]
    school_df = download_data(table_id, batch_schema)
    create_plot(school_df,
                columns=["School_City", "total_donation_amount"],
                sort_column='total_donation_amount',
                index_column='School_City',
                plt_name='batch',
                title="5 top cities with the highest donation amount"
                )
    return render_template('Batch.html')


# #
# if __name__ == '__main__':
#     app.run()
app.run(host='0.0.0.0', port=5000)
