from silicium import Component
import os
from .optimizer import min_css


class DefaultTheme(Component):
    build_target = "css"

    @property
    def code(self) -> str:
        css = open(os.path.join(os.path.dirname(__file__), "default.css"), "r").read()
        css = min_css(css)
        return f"<style>{css}</style>"

