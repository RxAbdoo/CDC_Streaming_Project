from pyflink.common import Configuration
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer

# إعداد الكونفيج لإضافة الـ JARs الخاصة بـ Kafka
config = Configuration()
config.set_string(
    "pipeline.jars",
    "file:///opt/flink/usrlib/flink-connector-kafka-3.2.0-1.19.jar;file:///opt/flink/usrlib/kafka-clients-3.4.0.jar"
)

# إنشاء بيئة التشغيل
env = StreamExecutionEnvironment.get_execution_environment(config)

# خصائص Kafka للـ Consumer
kafka_consumer_props = {
    "bootstrap.servers": "kafka:29092",
    "group.id": "flink-group",
    "auto.offset.reset": "earliest"
}

# مصدر Kafka
kafka_source = FlinkKafkaConsumer(
    topics="cdc.public.transactions",
    deserialization_schema=SimpleStringSchema(),
    properties=kafka_consumer_props
)

# قراءة البيانات
ds = env.add_source(kafka_source)

# خصائص Kafka للـ Producer
kafka_producer_props = {
    "bootstrap.servers": "kafka:29092"
}

# إعداد الـ Kafka Producer لتوبيك جديد
kafka_sink = FlinkKafkaProducer(
    topic="processed.transactions",
    serialization_schema=SimpleStringSchema(),
    producer_config=kafka_producer_props
)

# ربط البيانات القادمة للـ sink (إرسالها للتوبيك الجديد)
ds.add_sink(kafka_sink)

# تنفيذ الجوب
env.execute("Kafka Source to Sink Streaming Job")
