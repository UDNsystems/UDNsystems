def wikipog(ev):
  Win("UDWiki","<iframe src=\"https://wiki.udnsystems.repl.co/\" width=600 height=400></iframe>",600,400)
registerApp(
  App(
    "UD-Wiki",
    "udnwiki.png",
    wikipog
  )
)