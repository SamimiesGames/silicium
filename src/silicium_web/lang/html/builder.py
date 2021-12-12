from typing import Union

from silicium import Builder
from silicium.component import AbstractComponent


class HTMLBuilder(Builder):
    build_locations = {
        "css": [],
        "html": []
    }

    def build(self, build_content: str = None) -> str:
        html_content = self.builder_component.code

        for component in self.components:
            print(f"(html) BuildComponent: {component.__class__.__name__}")
            self.place_component(component)

        html_content = self.place_all_tags(html_content)
        html_content = self.minimize(html_content)

        return html_content

    def place_component(self, component: AbstractComponent):
        source = component.grand_render()
        self.build_locations[component.build_target].append(source)

    def place_all_tags(self, html_content) -> str:
        for build_location, html in self.build_locations.items():
            build_location = self.variable_format(build_location)
            build_content = "".join(html)
            html_content = html_content.replace(build_location, build_content)

        return html_content

    @staticmethod
    def minimize(html_content):
        return html_content.replace("\n", "")

    @staticmethod
    def variable_format(name: str):
        return "{%" + f" {name} " + "%}"
