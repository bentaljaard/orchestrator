from kafka import KafkaConsumer
from kafka import KafkaProducer
import requests
# import untangle
# from bs4 import BeautifulSoup

consumer = KafkaConsumer('task_response')
for msg in consumer:
	print(msg)
# 	result = requests.get(msg.value.decode("utf-8"))
# 	# doc = BeautifulSoup(msg.value.decode("utf-8"),"xml")

	
# 	# print (doc.find_all("taskSteps").find)


# producer = KafkaProducer()
# producer.send('task_response', r.text)