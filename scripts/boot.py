# version alpha v0.8a
# This is a commit test, feel free to ignore this bit of code...

from browser import document, html, window
from browser.local_storage import storage
import javascript
import json

__WEBOSVERSION__ = "v0.8a"

if not "auroramate" in storage:
  storage["auroramate"] = 'false'
auroramate = storage["auroramate"] == 'true'
if not "AMPMtimeSystem" in storage:
  storage["ampmtimeSystem"] = 'false'
timeSystem = storage["ampmtimeSystem"] == 'true'
cont = True
apps = ["test.py", "hexec.py", "invduck.py","win96.py","UDNCONN.py", "credits.py","terminal.py", "vm.py","settings.py", "appstore.py", "icefox.py", "NotAVirus.py", "Aclidenix.py", "explorer.py", "discord.py", "wiki.py"]
appList = []
YappList = []

# load low level scripts
lowlvlScripts = ["BOS.py","filesystem.py","SUS.py"] # moved SUS.py to lowlevel because SUSEnabled ducked up
for script in lowlvlScripts:
  f = open(f"scripts/lowlevel/{script}")
  scriptcode = f.read()
  f.close() # looks sus
  exec(scriptcode)
  screen.println(f"initialized {script}")
def print_col(text,hex):
  screen.changeCursorColor(hex)
  screen.println(text)
  screen.changeCursorColor("#00FF00")
def evalPy(code):
  try:
    return json.dumps({ "error": False, "output": str(eval(code)) })
  except Exception as duckup:
    return json.dumps({ "error": True, "output": str(duckup) })
def execPy(code):
  try:
    exec(code)
    return javascript.NULL
  except Exception as duck:
    return str(duck)
window.evalPy = evalPy
window.execPy = execPy
# load the icon
iconElement = html.IMG()
iconElement.attrs["src"] = "content/system/icon.jpg"
text = html.SPAN()
text.attrs["style"] = "font-size:18;color:#FFFFFF;font-family:Calibri;"
# uncomment this code to enable auroramate
# auroramate = True
# uncommont this to enable sus
# SUSEnabled = True # is it SUSE enabled or SUS enabled?
if auroramate:
  text <= "Universal Duck Network AuroraMATE."
else:
  if SUSEnabled:
    text <= "Universal Duck Network Sustems!"
  else:
    text <= "Universal Duck Network Systems."
centerelement = html.CENTER()
centerelement.attrs["id"] = "icon"
centerelement.attrs["class"] = "focused"
centerelement.appendChild(iconElement)
centerelement.appendChild(html.BR())
centerelement.appendChild(text)
document.body.appendChild(centerelement)
screen.println("loaded icon")
def registerApp(app):
  appList.append(app)
  YappList.append(app)
def emeregisterApp(app):
  appList.append(app)
  YappList.append(app)
# load the scripts

scripts = ["langs.py","Window.py","Util.py","Popup.py","start.py","desktop.py", "App.py"]
error = False
screen.println("loading duck scripts...")
for script in scripts:
  try:
    exec(fs.load_sys_file(f"scripts/software/{script}"))
    screen.println(f"loaded {script}")
  except Exception as e:
    error = True
    print_col(f"failed to load {script}, check the console for an error","#FF0000")
    window.console.error(f"failed to load {script} error below:")
    window.console.error(str(e))
    print(f"ERROR !!! {str(e)} !!! ERROR")
    #print(f"an error occured in {script}: {str(e)}")
  #  print(f"an error occured in {script}: ",end="")
  #  print
screen.println("Finished loading duck scripts")
screen.println("Preparing app loading")
screen.println("Prepared app loading, loading apps")
if not auroramate:
  downloadedapps = []
  for item in storage:
    if item.startswith("$downloadedApp$"):
      downloadedapps.append(item)
  for app in apps:
    folder = app.split(".")[0]
    try:
      exec(fs.load_sys_file(f"apps/{folder}/{app}"))
      screen.println(f"Loaded app {app}")
    except Exception as e:
      print("UDN systems: [ERROR DETECTED] "+str(e))
      error = True
      print_col(f"failed to load {app}, check console for the error and report it to the devs!!!", "#FF0000")
  if not error:
    screen.println("Finishing up...")
  for app in downloadedapps:
    exec(storage[app])
else:
  screen.println("intitializing auroramate subsystem")
  try:
    apps = ["test.py", "settings.py", "createApp.py", "docs.py", "terminal.py", "wiki.py"]
    for app in apps:
      folder = app.split(".")[0]
      exec(fs.load_sys_file(f"auroramate/apps/{folder}/{app}"))
      screen.println(f"Loaded app {app}")
    screen.println("finishing up app loading")
  except Exception as e:
    error = True
    print_col(f"failed to load {app}, check the console for an error","#FF0000")
    print("AuroraMate: [ERROR DETECTED] "+str(e))
def keypress():
  screen.clear()
  window.startupSound()
  icon = document.getElementById("icon")
  icon.parentNode.removeChild(icon)
  txt = document.getElementById("screen_container")
  txt.parentNode.removeChild(txt)
  desktopElement = html.DIV()
  desktopElement.attrs["id"] = "desktop"
  # if SUSEnabled:
  #   document.body.attrs["style"] = "background-image: url(\"/content/system/sus.png\");background-size:20%;background-repeat:repeat;background-color:white;";
  # else:
  try:
    bg = storage["theme"]
  except:
    bg = "classic"
    storage["theme"] = "classic"
  if auroramate:
    bg = "auroramate"
  if SUSEnabled: 
    bg = "sus"
  document.body.attrs["style"] = f"background-image: url(\"content/system/wallpapers/{bg}.png\");background-size:cover;width:100%;height:100%;background-repeat: no-repeat;-moz-background-size: cover;   -webkit-background-size: cover;"
  if bg == "sus": 
    document.body.attrs["style"] = "background-image: url(\"/content/system/wallpapers/sus.png\");background-size:20%;background-repeat:repeat;background-color:white;";
  document.body.appendChild(desktopElement)
  load_desktop()
  if auroramate:
    Win("duck", "duck", 0, 0, True)
  #document.body.unbind("keypress")
  
# screen.println("udn systems ready, press any key to continue...")
#document.body.bind("keypress",keypress)
if not storage.__contains__('quick-boot'):
	storage['quick-boot'] = "False";True
quickBoot = bool(storage['quick-boot']);
#print(quickBoot)
#print('^B')
if not error:
  if not quickBoot:
	  window.setTimeout(keypress,3000);
  else:
	  window.setTimeout(keypress,10);