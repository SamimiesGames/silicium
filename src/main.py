from silicium_web import Text, HTML, DefaultTheme


html = HTML()

DefaultTheme(html)
Text(html, text="Hello, Silicium!")
Text(html, text="Silicium is a progressive, infinitely scalable Python web-framework.")

html.run()

