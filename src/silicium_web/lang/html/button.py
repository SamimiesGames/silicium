from silicium import Component
from .actions import Action


class Button(Component):
    build_target = "html"
    text: str = "Not Clicked"

    @property
    def code(self) -> str:
        return f"""<div id="button">{self.text}</div>"""

    @Action
    def onclick(self):
        self.text = "clicked"
