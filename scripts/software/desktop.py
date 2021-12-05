from browser import document, html, window, aio

contextMenus = []

def sSFunc(ev):
  window.screenSaver();

def setupApps():
  global appList
  for app in appList:
    app.loadApp()

def load_desktop():
  global appList
  load_taskbar()
  setupApps()
  Popup("UDN "+str(__WEBOSVERSION__), "Warning","This is still in beta.")