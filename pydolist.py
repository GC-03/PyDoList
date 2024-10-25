from time import sleep

def main(tasks):

	while True:
		print("PYDOLIST\n")
		print("1 - Add a task")
		print("2 - Show all tasks")
		print("3 - Mark as done")
		print("4 - Quit")

		command = input("Enter command: ")

		print()

		if command == "1":
			add_task(tasks)
		elif command == "2":
			show_tasks(tasks)
		elif command == "3":
			mark_task(tasks)
		elif command == "4":
			kill()
		#else:
		#	print("Invalid command")

def add_task(tasks):
	print("---------------------------")
	task = input("Enter the task: ")
	tasks.append({"Task": task, "Done": False})
	print("Task added!")
	print("---------------------------\n")

def show_tasks(tasks):

	print("---------------------------")
	for i, task in enumerate(tasks):
		status = "Done" if task["Done"] else "Not Done"
		print(f"{i + 1} - {task['Task']}, {status}")
	print("---------------------------\n")

def mark_task(tasks):

	print("---------------------------")
	task = int(input("Enter the task number: ")) - 1
	if 0 <= task <= len(tasks):
		tasks[task]["Done"] = True
		print("Task marked as done!")
	else:
		print("Invalid task number")
	print("---------------------------\n")

def kill():

	print("---------------------------")
	print("Quitting...")
	quit()

tasks = []

main(tasks)
