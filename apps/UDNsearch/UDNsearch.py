def Search(ev):
  Win(lang.get('UATitle_searchEngine'), "<iframe src='https://udnsearch.udnsystems.repl.co/.html' width=600 height=500/>", 600, 500)

registerApp(
  App(
    "UDN Search Engine",
    "thispngdoesnotexist.png",
    Search
  )
)
