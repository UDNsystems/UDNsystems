from browser import document

def StartSus(ev):
  document.body.attrs["style"] = "background-image: url(\"/content/system/sus.png\");background-size:20%;background-repeat:repeat;background-color:white;"

registerApp(
  App(
    "SussyBaka",
    "amogus.png",
    StartSus
  )
)