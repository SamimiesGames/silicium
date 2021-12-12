from silicium import Component


class DefaultTheme(Component):
    build_target = "css"

    @property
    def code(self) -> str:
        return """
        <style>
        html {
          scroll-behavior: smooth;
          background-color: whitesmoke;
          font-family: -apple-system, 'Arial', sans-serif;
          color: #1e1e1e;
        }
        </style>
        """

