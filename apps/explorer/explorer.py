from browser import document, window
from browser.local_storage import storage
duckpos = "/"
def cdInto(ev):
  global duckpos
  for sussybaka in fs.ls(duckpos):
    if not sussybaka["item"] == ".":
      if sussybaka["directory"]:
        document.getElementById("UDE-folder-"+sussybaka['item']).unbind("click")
  document.getElementById("UDE-LeaveFolder").unbind("click")
  duckpos = fs.cd(duckpos, ev.srcElement.attrs["id"].split('-')[-1])+"/"
  document.getElementById("windows-content-UD-Explorer").html = calculateAmogusSus()
  rebind()
def goOut(ev):
  global duckpos
  if not duckpos == "/":
    for sussybaka in fs.ls(duckpos):
      if not sussybaka["item"] == ".":
        if sussybaka["directory"]:
          document.getElementById("UDE-folder-"+sussybaka['item']).unbind("click")
    document.getElementById("UDE-LeaveFolder").unbind("click")
    duckpos = fs.cd(duckpos, "..")
    document.getElementById("windows-content-UD-Explorer").html = calculateAmogusSus()
    rebind()
  else:
    Popup("Oh no!", "Error", "cannot leave root directory")

def rebind():
  global duckpos
  for sussybaka in fs.ls(duckpos):
    if not sussybaka["item"] == ".":
      if sussybaka["directory"]:
        document.getElementById("UDE-folder-"+sussybaka["item"]).bind("click", cdInto)
  document.getElementById("UDE-LeaveFolder").bind("click",goOut)
def calculateAmogusSus():
  global duckpos
  print(duckpos)
  duckls = fs.ls(duckpos)
  calculatedamogussus = ""
  for sussybaka in duckls:
    if not sussybaka["item"] == ".":
      if sussybaka["directory"]:
        item = sussybaka["item"]
        calculatedamogussus += f"<div class='UDE-folder' id='UDE-folder-{item}'>{item}     📂<br></div>"
      else:
        calculatedamogussus += sussybaka["item"] + "     📄<br>"
  calculatedamogussus += "<div class='UDE-folder' id='UDE-LeaveFolder'>..     📂</div>"
  return calculatedamogussus
def mainfunc(ev):
  Popup("sussy warning","Warning","this is in dev, watch out!")
  Win("UD-Explorer",calculateAmogusSus(),200,200)
  rebind()
registerApp(
  App(
    "UD-Explorer", # Universal Duck Explorer 👍
    "explorer.png",
    mainfunc
  )
)