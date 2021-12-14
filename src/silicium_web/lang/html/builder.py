import htmlmin

from silicium import Builder
from silicium.component import AbstractComponent
from silicium.utils import vars


class HTMLBuilder(Builder):
    build_locations = {
        "css": [],
        "html": [],
        "scripts": []
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
            build_content = "".join(html)
            html_content = vars.translate(html_content, build_location, build_content)

        return html_content

    @staticmethod
    def minimize(html_content):
        return htmlmin.minify(html_content, remove_comments=True, remove_empty_space=True, reduce_empty_attributes=True)
