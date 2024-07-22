from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Инициализация SparkSession
spark = SparkSession.builder.appName("ProductsCategories").getOrCreate()

# Пример данных
products_data = [
    (1, "ProductA"),
    (2, "ProductB"),
    (3, "ProductC"),
    (4, "ProductD")
]

categories_data = [
    (1, "Category1"),
    (2, "Category2"),
    (3, "Category3")
]

product_category_data = [
    (1, 1),
    (2, 2),
    (3, 1),
    (3, 3)
]

# Создание датафреймов
products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])
categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

# Объединение продуктов с категориями
product_with_category_df = products_df.join(
    product_category_df, on="product_id", how="left"
).join(
    categories_df, on="category_id", how="left"
).select(
    col("product_name"), col("category_name")
)

# Найти продукты без категорий
products_without_category_df = products_df.join(
    product_category_df, on="product_id", how="left_anti"
).select(
    col("product_name")
)

# Вывод результата
print("Продукты с категориями:")
product_with_category_df.show()

print("Продукты без категорий:")
products_without_category_df.show()
