from silicium import Builder


class HTMLBuilder(Builder):
    def build(self, build_content: str = None) -> str:
        build_targets = {
            "css": [],
            "html": []
        }

        html_content = self.build_component.code

        for component in self.components:
            print(f"(html) BuildComponent: {component.__class__.__name__}")
            build_targets[component.build_target].append(f"{component.code}")

        for build_target, html in build_targets.items():
            build_target = "{%" + f" {build_target} " + "%}"
            build_content = "".join(html)
            html_content = html_content.replace(build_target, build_content)

        html_content = html_content.replace("\n", "")

        return html_content
