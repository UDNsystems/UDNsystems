def hexecVMFunc(ev):
  hexec = Win("HEXEc VM", "<iframe src='https://hexec.dateplays.repl.co/' style=\"width: 100%; height: 100%;\"></iframe>", 800, 600)

registerApp(
  App(
    "HEXEc",
    "hexec.png",
    hexecVMFunc
  )
)