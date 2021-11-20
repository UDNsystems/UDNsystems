from brython import document, html

def notepad(ev):
  Win("Notepad", "<iframe src='Notepad.html' width=200 height=200></iframe>", 200, 200)

registerApp(
  App(
    "Notepad",
    "default.jpg",
    notepad
  )
)