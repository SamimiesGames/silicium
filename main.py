from silicium import Component
from silicium.interactions import Hoverable
from silicium import Text
from silicium import events


class Tooltip(Component):
    @events.Create
    def on_create(self):
        self.instantiate(Text)

    @Hoverable
    def on_hover(self, e):
        self.position = e.absolute_position

