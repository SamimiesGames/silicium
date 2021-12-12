from silicium_web import Text, HTML


html = HTML()

Text(html, text="Hello, Silicium!")
Text(html, text="Silicium is a progressive, infinitely scalable Python web-framework.")


html.builder.build()

