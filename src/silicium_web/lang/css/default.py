from silicium import Component


class DefaultTheme(Component):
    build_target = "css"

    @property
    def code(self) -> str:
        return """
        <style>
        html {
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100%;
          scroll-behavior: smooth;
          background-color: #4684ff;
          font-family: -apple-system, 'Arial', sans-serif;
          color: #1e1e1e;
          text-align: center;
        }
        p {
          font-size: 2rem;
        }
        </style>
        """

