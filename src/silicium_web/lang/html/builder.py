from silicium import Builder


class HTMLBuilder(Builder):
    def build(self):
        build_content = self.build_component.code
        new_content = ""

        indent = 2

        for component in self.components:
            print(f"BuildComponent: {component.__class__.__name__}")
            new_content += f"{' ' * indent}{component.code}\n"

        build_content = build_content.replace("{% content %}", new_content)

        with open("index.html", "w") as fh:
            fh.write(build_content)

        print("Build complete.")
