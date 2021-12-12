from silicium_web import Text, HTML, DefaultTheme


html = HTML()

DefaultTheme(html)

text = Text(html, text="Hello, Silicium-web!")
Text(text, text="I'm behind!")

html.run()
