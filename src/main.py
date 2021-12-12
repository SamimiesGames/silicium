from silicium_web import Text, Button, HTML, DefaultTheme


html = HTML()

DefaultTheme(html)

text = Text(html, text="Hello, Silicium-web!")
Text(text, text="I'm behind!")
Button(text, text="Click me to see the world!")

html.run()
