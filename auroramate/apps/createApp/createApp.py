from browser import window, document

def registerCustomApp(code):
  try:
    exec(code)
    reloadApps()
  except Exception as e:
    Popup("Error!", "Error", str(e))

def modifyBootloader(code):
  window.localforage.setItem("/bootloader/boot.py",'''f = open("scripts/boot.py")
UDNBL = f.read()
f.close()
exec(UDNBL)''' + code)

def overwriteBootloader(code):
  #storage['/bootloader/boot.py'] = code
  window.localforage.setItem('/bootloader/boot.py', code);

window.registerCustomApp = registerCustomApp

def createapp(ev):
  Win("UDN code editor", "<iframe src='auroramate/apps/createApp/bigcool-test.html' width='100%' height='100%' style=\"border: none;\"/>",800, 500)
registerApp(
  App(
    "UDN code editor",
    "appcreator.jpg",
    createapp
  )
)