from silicium import AbstractScene, Component
from .builder import HTMLBuilder


BOILER_PLATE_HTML = """
<!doctype html>
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8">

  <title>Silicium Site</title>

  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <link rel="manifest" href="site.webmanifest">
  <link rel="apple-touch-icon" href="icon.png">
  
  {% css %}
</head>
<body>
{% html %}
</body>

</html>
"""


class BasicHTML(Component):
    @property
    def code(self) -> str:
        return BOILER_PLATE_HTML


class HTML(AbstractScene):
    def __init__(self):
        html_builder = HTMLBuilder()

        self.builder = html_builder

        self.builder.builder_component = BasicHTML(self, add=False)

    def run(self) -> None:
        print(f"Run scene: {self.__class__.__name__}")

        page = self.builder.build()

        with open("index.html", "w") as fh:
            fh.write(page)

        print(f"Run success: {self.__class__.__name__}")

