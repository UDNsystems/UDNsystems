def credits(ev):
  #html = '''<duck style="font-family:monospace;">Coded by:</br>Coder() (@Fox551)</br>Nicejsiscool (@TBSharedAccount)</br>Sussy (@abruhuser)</br>Ponali (@Ponali)</br></br>Made Icons:</br>NT_Cat (made icon called cloudduck, we were allowed to use it)</duck>'''
  html = lang.get('UAContent_credits')
  Win(lang.get('UATitle_credits'), html, 300, 300)
registerApp(
  App(
    "credits",
    "credits.png",
    credits
  )
)