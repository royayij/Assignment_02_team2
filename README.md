# Data Pipeline Architecture
![Report 2](https://user-images.githubusercontent.com/34235886/144624746-6f04f94e-ffb5-4a9d-ae78-d50e15bef7b5.png)

Both processing pipelines have their ending in common. The batch and streaming data processing pipelines save their results in the same data sink, namely BigQuery -used as data warehouse as well as serving layer-. The dashboard -Google’s Data Studio/Flask API- retrieves data from this data warehouse in order to generate the visualizations.

Firstly, the batch processing pipeline is straightforwardly implemented. After processing, data gets directly uploaded in the data warehouse BigQuery, available for visualization. 
Secondly, we implemented Spark for the stream processing pipeline in order to process the data according to our configurations and needed output. After processing, processed data is stored in the BigQuery data warehouse previously mentioned to serve as input for the dashboards. The stream data processing pipeline is -in concreto- implemented as follows. Firstly, data gets uploaded in the GCP -bucket-. Afterwards, the Kafka-producer publishes the data towards Spark -stream-. Then Spark does several transformations/actions on the data. Then the Kafka consumer subscribes to the topic and sends the data to the common BigQuery data warehouse, where it is once again used as an input source for Data Studio/Flask API.
