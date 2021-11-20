from browser import document, html, window, ajax

def icefox(ev):
  Win("IceFox", "<iframe src=\"https://udn-systems-icefox.fox551.repl.co\" width=600px height=500px>", 600, 500)
registerApp(
  App(
    "IceFox",
    "icefox.png",
    icefox
  ) 
)