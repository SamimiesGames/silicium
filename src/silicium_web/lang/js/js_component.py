from silicium import Component


class JSComponent(Component):
    build_target = "scripts"

    @property
    def code(self) -> str:
        ...
