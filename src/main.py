from silicium_web import Text, HTML, DefaultTheme


html = HTML()

DefaultTheme(html)

Text(html, text="Hello, Silicium-web!")


html.run()
