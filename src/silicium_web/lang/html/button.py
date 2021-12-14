from silicium import Component


class Button(Component):
    build_target = "html"
    text: str = "Not Clicked"

    @property
    def code(self) -> str:
        return f"""<div id="button">{self.text}</div>"""

    def onclick(self):
        self.text = "clicked"
