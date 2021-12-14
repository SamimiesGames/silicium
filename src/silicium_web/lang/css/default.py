from silicium import Component
from silicium.utils import require

from . import optimizer

class DefaultTheme(Component):
    build_target = "css"

    def __init__(self, parent, add: bool = True, **kwargs):
        super().__init__(parent, add=add, **kwargs)

    @property
    def code(self) -> str:
        css_optimized = optimizer.min_css(require(__file__, "themes.css"))
        return f"<style>{css_optimized}</style>"
