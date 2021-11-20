def invducc(ev):
  ducc = Win(lang.get('UATitle_invduck'), "<iframe src='https://invduck.abruhuser.repl.co/' style=\"width: 100%; height: 100%;\"></iframe>", 800, 600)

registerApp(
  App(
    "InvDuck VM",
    "invduck.png",
    invducc
  )
)