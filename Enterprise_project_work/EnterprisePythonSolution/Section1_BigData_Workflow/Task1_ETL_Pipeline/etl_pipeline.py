from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Big Data ETL Pipeline") \
    .getOrCreate()

# Load Data
input_path = "s3://your-bucket/input-data.csv"  # Replace with Azure Blob Storage or AWS S3 path
data = spark.read.csv(input_path, header=True, inferSchema=True)

# Data Transformation
transformed_data = data.filter(col("column_name").isNotNull()) \
    .withColumnRenamed("old_column", "new_column")

# Save Transformed Data
output_path = "s3://your-bucket/output-data.csv"  # Replace with Azure Blob Storage or AWS S3 path
transformed_data.write.csv(output_path, header=True)

# Stop Spark Session
spark.stop()