from silicium import Component


class Text(Component):
    text: str

    @property
    def code(self) -> str:
        return f"<p>{self.text}</p>"
