from flet import *

def main(page: Page):
    count = Text("0")

    def increment(e):
        count.value = str(int(count.value) + 1)
        page.update()

    page.add(Text("Click Counter"), count, ElevatedButton("Click me", on_click=increment))

app(target=main)
