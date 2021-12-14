from silicium import Component
from silicium.utils.require import require


class DefaultTheme(Component):
    build_target = "css"

    def __init__(self, parent, add: bool = True, **kwargs):
        super().__init__(parent, add=add, **kwargs)

    from .optimizer import min_css

    @property
    def code(self) -> str:
        css_optimized = self.min_css(require(__file__, "themes.css"))
        return f"<style>{css_optimized}</style>"
