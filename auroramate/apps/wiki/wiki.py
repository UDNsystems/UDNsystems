def wikipog(ev):
  Win("UDWiki","https://udn-wiki.udnsystems.repl.co",200,200)
registerApp(
  App(
    "UD-Wiki",
    "udn-wiki.png",
    wikipog,
    False
  )
)