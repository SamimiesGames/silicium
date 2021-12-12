from silicium import Component


class Text(Component):
    build_target = "html"
    text: str

    @property
    def code(self) -> str:
        return f"<p>{self.text}</p>"
