from silicium import AbstractScene, Component
from .builder import HTMLBuilder
from dataclasses import field


BOILDER_PLATE_HTML = """
<!doctype html>
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8">

  <title>Silicium Site</title>

  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <link rel="manifest" href="site.webmanifest">
  <link rel="apple-touch-icon" href="icon.png">
</head>

<body>
{% content %}
</body>

</html>
"""


class BasicHTML(Component):

    @property
    def code(self) -> str:
        return BOILDER_PLATE_HTML


class HTML(AbstractScene):
    builder: HTMLBuilder = HTMLBuilder()

    def __init__(self):
        self.builder.build_component = BasicHTML(self, add_now=False)
