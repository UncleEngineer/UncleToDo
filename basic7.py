from flet import *

def main(page: Page):
    page.add(Image(src="logo.svg", width=500, height=500))

app(target=main)

