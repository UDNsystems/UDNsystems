def acli(ev):
  Win(lang.get('UATitle_aclidenix'), "<iframe src='https://aclidenix-udn.udnsystems.repl.co' width=600 height=500/>", 600, 500)
  # Win("Aclidenix", "<iframe src='https://aclidenix-udn.udnsystems.repl.co' style='width:100%;height:100%;'/>", 600, 500)

registerApp(
  App(
    "Aclidenix",
    "aclidenix.png",
    acli
  )
)