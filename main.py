import datetime

from task import Task

exit_logging = False
logged_tasks = []

print("Starting program...")

while exit_logging == False:
	print("Would you like to create a new task (y/n)")
	response = input()
	if response == "y" or response == "Y":
		print("What are you going to do?")
		task_name = input()
		print("What category does this task fall under (optional)")
		task_cat = input()
		if task_name != None:
			current_task = Task(task_name, task_cat)
			print("Logging " + task_name + ". Press enter when you are finished.")
			input()
			current_task.close()
			logged_tasks.append(current_task)
			print("Logged " + task_name + " successfully.")
		else:
			print("Your task needs a name, please try again")
	elif response == "n" or response == "N":
		print("Would you like to exit the program? (enter y to exit)")
		exit_response = input()
		if exit_response == "y" or exit_response == "Y":
			exit_logging = True
	else:
		print("Didn't understand your response, please try again")
		
exit_saving = False

while exit_saving == False:
	print("Would you like to save your tasks? (y/n)")
	saving_response = input()
	if saving_response == "y" or saving_response == "Y":
		with open('output.csv', 'w') as file:
			file.write('name, category, seconds\n')
			for logged_task in logged_tasks:
				logged_name = str(logged_task.task_name).replace(","," - ")
				logged_category = str(logged_task.task_category).replace(",", " - ")
				logged_time = str(round(logged_task.getseconds(), 1))
				file.write(logged_name + "," + logged_category + "," + logged_time + "\n")
			print("Outputted data in output.csv. This data will be overwritten the next time you attempt to save a file. Exiting program...")
			exit_saving = True
	elif saving_response == "n" or saving_response == "N":
		print("Are you sure you want to discard your tasks?")
		confirm_response = input()
		if confirm_response == "y" or confirm_response == "Y":
			exit_saving = True
	else:
		print("Didn't understand your response, please try again")
