tasks = []

print("------To-Do List Application------")
print("Enter tasks to add them to your to-do list.")
while True:
    task = input("Enter a task (or type 'done' to finish): ")
    if task.lower() == 'done':
        break
    tasks.append(task)

print("\nYour To-Do List:")
for task in tasks:
    print("- " + task)
print("You have " + str(len(tasks)) + " tasks in your to-do list.")