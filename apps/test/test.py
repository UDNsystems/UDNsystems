from browser import window
def testFunc(ev):
  test = Win("testduck",f"<center>It works!</center></br>replit update duck test!!!!"+str(appList),400,400)
  popuptest = Popup("test","Error","lmao sus")
registerApp(
  App(
    "test",
    "default.jpg",
    testFunc
  )
)