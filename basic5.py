from flet import *

def main(page: Page):
    n1 = TextField(label="Number 1", width=150)
    n2 = TextField(label="Number 2", width=150)
    result = Text()

    def calculate(e):
        try:
            total = float(n1.value) + float(n2.value)
            result.value = f"Result: {total}"
        except:
            result.value = "Invalid input!"
        page.update()

    page.add(n1, n2, ElevatedButton("Add", on_click=calculate), result)

app(target=main)
