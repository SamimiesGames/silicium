from silicium import Component
from silicium.utils import require

from . import optimizer

class DefaultTheme(Component):
    build_target = "css"

    @property
    def code(self) -> str:
        css = require(__file__, "themes.css")
        css_optimized = optimizer.min_css(css)
        return f"<style>{css_optimized}</style>"
