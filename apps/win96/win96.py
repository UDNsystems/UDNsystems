def win96(ev):
  win96 = Win("Windows96 VM","<iframe src=\"https://windows96.net/\" style=\"width: 100%; height: 100%;\"></iframe>",800,600)

registerApp(
  App(
    "WIN96",
    "win96.png",
    win96
  )
)