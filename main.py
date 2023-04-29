#list to store all the tasks
tasks = []

#accessing elements
todo_input = Element("todo_input")
error_element = Element("error").element
template = Element("task-template").select(".task", from_content=True)
list = Element("items")

#function to do the job
def add_todo(*args):
    input_value = todo_input.element.value
    if input_value:
        error_element.innerHTML = ""
        todo_id = f"todo-{len(tasks)}"
        todo = {
            "id" : todo_id,
            "text" : input_value,
            "done" : False
        }
        tasks.append(todo)
        
        #create new task
        task = template.clone(todo_id, to=list)
        task_content = task.select("p")
        task_content.element.innerHTML = input_value
        task_checkbox = task.select("input")
        task_checkbox.element.checked = False

        # appending task to the list
        list.element.appendChild(task.element)
        todo_input.clear()

        def complete_task(task_id):
            task_checkbox_element = task_checkbox.element
            task_checkbox_element.checked = True
            task_checkbox_element.disabled = True
            task_content.element.style.textDecoration = "line-through"

        task_checkbox.element.onclick = complete_task

    else:
        error_element.innerHTML = "PLEASE ENTER A TODO"