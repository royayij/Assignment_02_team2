from google.cloud import bigquery
import os
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [10, 6]
# Set up with a higher resolution screen (useful on Mac)


def download_data(table_id, schema):
    client = bigquery.Client()
    # Download a table.
    table = bigquery.TableReference.from_string(table_id)
    rows = client.list_rows(table, selected_fields=schema, )
    dataframe = rows.to_dataframe(create_bqstorage_client=True, )
    return dataframe


def create_plot(df, columns, sort_column, index_column, plt_name, title):
    result = df[columns].sort_values(by=[sort_column], ascending=False).drop_duplicates()
    result.set_index(index_column, inplace=True)
    z = result[:5]
    z.plot(kind='bar')
    plt.title(title)
    plt.savefig('./static/{}.png'.format(plt_name))
