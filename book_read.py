from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, IntegerType, StructType


# build the session with the name
spark = SparkSession.builder.appName('Read Data').getOrCreate()

# read file
df = spark.read.json('training_data.json')

# generate the log_value_vector
log_value_vector_schema = [StructField('Content', StringType(), True), StructField('Log Key', StringType(), True)]
log_value_vector = StructType(fields=log_value_vector_schema)
