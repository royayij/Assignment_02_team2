# Data Pipeline Architecture
![Report 2](https://user-images.githubusercontent.com/34235886/144294583-79885449-13da-46ae-8466-637808fcbf76.png)
Both batch and streaming data processing pipelines save their results in the same data sink, namely BigQuery -used as data warehouse as well as serving layer-. The dashboard -Google’s Data Studio- retrieves data from this data warehouse in order to generate the visualizations.
The batch processing pipeline is straightforwardly implemented. The data gets directly uploaded in the data warehouse BigQuery.

Afterward, we implemented Spark to do steam processing this data according to our configurations and needed output. After processing, processed data is stored in the BigQuery data warehouse previously mentioned to serve as input for the dashboards.
The stream data processing pipeline is implemented as follows. Firstly, data gets uploaded in the GCP -bucket-. Afterward, the Kafka-producer uses the data for transformations and publishes the data toward spark -stream-. Then the Kafka consumer subscribes to the topic and sends the data to the common BigQuery data warehouse, where it is once again used as an input source for Data Studio. Also, a simple visualization by using BigQuery and Flask API is implemented.
