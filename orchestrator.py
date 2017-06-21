#Main orchestrator 

import yaml
import queue
from pprint import pprint

file = "test.yaml"
with open(file) as data_file:    
	    orchdata = yaml.load(data_file)


q = queue.Queue()

tasks = orchdata['tasks']

for task in tasks:
	key=next(iter(task))
	value=task.get(key)

	if(value.get('type') == 'service'):
		q.put(value)
q.put(None)

# for task in tasks:
# 	next(iter(task))
# 	pprint(task.get().get('type'))

hasMoreItems = True

while hasMoreItems:
	taskItem = q.get()
	if taskItem is None:
		hasMoreItems = False
	print(taskItem)
	q.task_done()