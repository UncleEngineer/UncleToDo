from flet import *

def main(page: Page):
    tasks = Column()
    task_input = TextField(label="New Task")

    def add_task(e):
        tasks.controls.append(Text(task_input.value))
        task_input.value = ""
        page.update()

    page.add(task_input, ElevatedButton("Add Task", on_click=add_task), tasks)

app(target=main)
