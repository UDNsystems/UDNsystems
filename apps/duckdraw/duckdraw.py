from browser import document, html

def Duckdraw(ev):
  Win("Duckdraw", '<iframe src="/apps/duckdraw/index.html" style="width: 100%; height: 100%; border: none;">', 500, 500)

registerApp(
  App(
    "Duckdraw",
    "duckdraw.jpg",
    Duckdraw
  )
)