from silicium import Component
from silicium.utils import require
from .optimizer import min_css


class DefaultTheme(Component):
    build_target = "css"

    @property
    def code(self) -> str:
        css = require(__file__, "default.css")
        css = min_css(css)
        return f"<style>{css}</style>"

