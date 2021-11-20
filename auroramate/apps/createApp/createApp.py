from browser import window, document

def registerCustomApp(code):
  try:
    exec(code)
    reloadApps()
  except Exception as e:
    Popup("Error!", "Error", str(e))
window.registerCustomApp = registerCustomApp

def createapp(ev):
  Win("UDN code editor", "<iframe src='auroramate/apps/createApp/bigcool-test.html' width='100%' height='100%' style=\"border: none;\"/>", 600, 400)
registerApp(
  App(
    "UDN code editor",
    "appcreator.jpg",
    createapp
  )
)