import pandas as pd
from pyspark.sql import SparkSession
spark=SparkSession.builder\
.appName("data analytics")\
.getOrCreate()


df=spark.read.csv("pyspark_sales_profit_dataset.csv",header=True,inferSchema=True)
# df.show()
df.printSchema()