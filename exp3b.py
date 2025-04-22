todo_list=()

todo_list+=("Pay bills",)
todo_list+=("rizzing up lvl 3 gyatts",)
todo_list+=("goonmaxxing",)

print("The Updated Todo List is:")
print(todo_list)

todo_list= tuple(task for task in todo_list if task != "Pay bills")
print("The updated todo list:")
print(todo_list)

todo_list=("Cocknballtorture",)+todo_list
print("The updated todo list:")
print(todo_list)

todo_list=tuple(sorted(todo_list))
print("The updated todo list:")
print(todo_list)

todo_list=tuple(reversed(todo_list))
print("The updated todo list:")
print(todo_list)

todo_list=()
print("The updated todo list:")
print(todo_list)