import sys
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    bucket = "gs://play-desafio-dataproc"
    with open(bucket+"/resultado/part-00000.txt", encoding="utf8") as file:
        data = file.read().split('\n')
        data = data[:10]
        top10 = ""
        top10 = '\n'.join(data)
        print(top10)

    with open(bucket+"/resultado/resultado.txt", 'w') as newFile:
        newFile.write(top10)