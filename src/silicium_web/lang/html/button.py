from silicium import Component
from . import actions


class Button(Component):
    build_target = "html"
    text: str = "Not Clicked"

    @property
    def code(self) -> str:
        return f"""<div id="button">{self.text}</div>"""

    @actions.Action
    def onclick(self):
        self.text = "clicked"
