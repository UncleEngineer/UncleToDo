from flet import *

def main(page: Page):
    switch = Switch(label="Dark Mode")

    def toggle_theme(e):
        page.theme_mode = "dark" if switch.value else "light"
        print(switch.value)
        page.update()

    switch.on_change = toggle_theme
    page.add(switch)

app(target=main)
