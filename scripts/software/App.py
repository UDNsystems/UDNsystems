from browser import document, html, window, aio, console

class App:
  def __init__(self, name, icon, exec, customIcon=False):
    iconElement = html.IMG()
    if customIcon:
      iconElement.attrs["src"] = icon
    else:
      iconElement.attrs["src"] = f"content/appicons/{icon}"
    iconElement.attrs["class"] = "app-icon"
    self.name = name
    self.app = html.BUTTON()
    self.app.attrs["id"] = name
    self.app.attrs["class"] = "apps"
    self.app <= iconElement
    self.appcontainer = html.DIV()
    self.appcontainer.attrs["id"] = f"{name}-container"
    self.appcontainer.attrs["class"] = "app-containers"
    self.appcontainer.appendChild(self.app)
    text = html.SPAN()
    text.attrs["class"] = "app-text"
    translationKey = f"UDNAPP_{name}"
    if lang.get(translationKey):
      text.innerHTML = lang.get(translationKey)
    else:
      text.innerHTML = name;

    self.appcontainer <= html.BR() + text
    self.code = exec
    self.app.bind("click", window.weirdrun)
  def weirdrun(self, ev):
    try:
      self.code(ev)
    except Exception as e:
      Popup("Error!","Error",str(e))
      print("ERROR AT "+self.name+": "+str(e))
  def loadApp(self):
    document.getElementById("desktop").appendChild(self.appcontainer)

def pain():
  global appList, YappList
  for i in range(len(appList)):
    appList.pop()
    YappList.pop()
    
def reloadApps():
  global downloadedapps, appList, YappList
  pain()
  downloadedapps2 = []
  duck = document.getElementsByClassName('app-containers')
  for element in duck:
    document.getElementById("desktop").removeChild(element)
  for item in storage:
    if item.startswith("$downloadedApp$"):
      downloadedapps2.append(item)
  for app in apps:
    folder = app.split(".")[0]
    try:
      exec(fs.load_sys_file(f"apps/{folder}/{app}"))
    except Exception as e:
      pass
  for app in downloadedapps2:
    exec(storage[app])
  setupApps()
  # for window in openWindows:
  #   window.windowContainer.attrs["style"] = f"left:{window.windowContainer.offsetLeft - window.pos1}px;top:{window.windowContainer.offsetTop - window.pos2}px;"
