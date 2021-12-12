from silicium_web import Text, HTML, DefaultTheme


html = HTML()

DefaultTheme(html)

text = Text(html, text="Hello, Silicium-web!")
Text(text, text="Silicium-web is a progressive, infinitely scalable Python web-framework.")

html.run()
