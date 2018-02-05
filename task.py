from datetime import datetime

class Task:
	def __init__(self, task_name, task_category):
		self.start_time = datetime.now()
		self.task_name = task_name
		self.task_category = task_category
		
	def close(self):
		self.end_time = datetime.now()
		
	def getseconds(self):
		return (self.end_time - self.start_time).total_seconds()
