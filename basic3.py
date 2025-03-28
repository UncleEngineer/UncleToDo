from flet import *

def main(page: Page):
    name = TextField(label="Enter your name")
    output = Text()

    def greet(e):
        output.value = f"Hello, {name.value}!"
        page.update()

    page.add(name, ElevatedButton("Greet", on_click=greet), output)

app(target=main)


