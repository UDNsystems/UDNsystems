from browser import load
def NotAVirus(ev):
  load("https://udn.codersquack.ml/apps/NotAVirus/NotAVirus.js")

registerApp(
  App(
    "Not A Virus",
    "default.jpg",
    NotAVirus
  )
)