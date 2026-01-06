# imp
# No of times Charecter repeated in the list 

list1 = ["Hello students", "Hello pyspark", "Hello rdd"]
input_rdd = sc.parallelize(list1)
flat_map_rdd = input_rdd.flatMap(lambda x: x.split(" "))

result = input_rdd.flatMap(lambda x: x.split(" "))\
                  .map(lambda x: (x, 1))\
                  .reduceByKey(lambda x, y: x + y)
print(result.collect())
