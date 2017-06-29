from kafka import KafkaConsumer
from kafka import KafkaProducer
import requests
# import untangle
# from bs4 import BeautifulSoup

consumer = KafkaConsumer('task_topic', group_id='my_favorite_group')
for msg in consumer:
	print(msg)
	result = requests.get(msg.value.decode("utf-8"))

	producer = KafkaProducer(bootstrap_servers='localhost:9092')
	producer.send('task_response', result.text.encode("utf-8"))
	# doc = BeautifulSoup(msg.value.decode("utf-8"),"xml")

	
	# print (doc.find_all("taskSteps").find)

