from browser import document, html, window, alert, window
import base64
import browser.widgets.menu as widgets
import javascript

stbtnSelected = False;

startbutton = html.IMG()
startbutton.attrs['class'] = "startbutton-img";
startbutton.attrs['id'] = "startbtn"
startbutton.attrs['src'] = "/content/startmenu/unselected.png";

YappList = []

startmenu = html.DIV()
startmenu.attrs["style"] = 'display:none;'
startmenu.attrs["id"] = "start-menu"

def restart(ev):
  window.location.reload();

def clock(ev):
  Win("clock!", "<iframe src='/scripts/software/softwaredata/clock/clock.html' width=200 height=200/>", 200, 200)

def load_taskbar():
  global startmenu
  taskBar = html.DIV()
  taskBar.attrs["id"] = "taskbar"
  taskBar.appendChild(startbutton)
  f = open("styling/startmenu.css")
  customCss = f.read()
  f.close()
  menu = widgets.Menu(container=startmenu)
  programs = menu.add_menu(lang.get('apps')+' >')
  for app in YappList:
    programs.add_item(app.name).bind("click", app.code)
  document.getElementById("desktop").appendChild(startmenu)
  #end of menu stuff
  startbutton.bind('click',startMenuClick)
  document.body.appendChild(taskBar)
  if not timeSystem:
    code = base64.b64decode("d2luZG93LnNldHVwQW1vZ3VzQ2xvY2sgPSBmdW5jdGlvbigpewogIHZhciBjbG9ja29iaiA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoIkRJViIpCiAgY2xvY2tvYmouaWQgPSAidGFza2Jhci5DTE9DSyIKICBjbG9ja29iai5zdHlsZSA9ICJmbG9hdDogcmlnaHQ7IG1hcmdpbi1yaWdodDo1cHg7IgogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJ0YXNrYmFyIikuYXBwZW5kQ2hpbGQoY2xvY2tvYmopCiAgc2V0SW50ZXJ2YWwoZnVuY3Rpb24oKXsKICAgIHZhciB0aW1lID0gbmV3IERhdGUoKQogICAgdmFyIG1pbnV0ZXMgPSB0aW1lLmdldE1pbnV0ZXMoKQogICAgaWYobWludXRlcyA8IDEwKXsKICAgICAgICBtaW51dGVzID0gIjAiK21pbnV0ZXMudG9TdHJpbmcoKQogICAgfSBlbHNlIHsKICAgICAgICBtaW51dGVzID0gbWludXRlcy50b1N0cmluZygpCiAgICB9CiAgICB2YXIgY29tYmluZWRUaW1lID0gdGltZS5nZXRIb3VycygpLnRvU3RyaW5nKCkrIjoiK21pbnV0ZXM7CiAgICBjbG9ja29iai5pbm5lckhUTUwgPSBjb21iaW5lZFRpbWU7CiAgfSkKfQ==").decode("utf-8")
  else:
    code = base64.b64decode("d2luZG93LnNldHVwQW1vZ3VzQ2xvY2sgPSBmdW5jdGlvbigpewogIHZhciBjbG9ja29iaiA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoIkRJViIpCiAgY2xvY2tvYmouaWQgPSAidGFza2Jhci5DTE9DSyIKICBjbG9ja29iai5zdHlsZSA9ICJmbG9hdDogcmlnaHQ7IG1hcmdpbi1yaWdodDo1cHg7IgogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJ0YXNrYmFyIikuYXBwZW5kQ2hpbGQoY2xvY2tvYmopCiAgc2V0SW50ZXJ2YWwoZnVuY3Rpb24oKXsKICAgIHZhciB0aW1lID0gbmV3IERhdGUoKQogICAgdmFyIG1pbnV0ZXMgPSB0aW1lLmdldE1pbnV0ZXMoKQogICAgdmFyIGFtcG0gPSAiQU0iCiAgICB2YXIgaG91cnMgPSB0aW1lLmdldEhvdXJzKCkKICAgIGlmKGhvdXJzPjEyKXsKICAgICAgYW1wbSA9ICJQTSIKICAgICAgaG91cnMgPSBob3VycyAtIDEyCiAgICB9CiAgICBob3Vycy50b1N0cmluZygpCiAgICBpZihtaW51dGVzIDwgMTApewogICAgICAgIG1pbnV0ZXMgPSAiMCIrbWludXRlcy50b1N0cmluZygpCiAgICB9IGVsc2UgewogICAgICAgIG1pbnV0ZXMgPSBtaW51dGVzLnRvU3RyaW5nKCkKICAgIH0KICAgIHZhciBjb21iaW5lZFRpbWUgPSBob3VycysiOiIrbWludXRlcysiICIrYW1wbQogICAgY2xvY2tvYmouaW5uZXJIVE1MID0gY29tYmluZWRUaW1lOwogIH0pCn0=").decode("utf-8") 
  window.evalJS(code)
  window.setupAmogusClock()
  document.getElementById("taskbar.CLOCK").bind("click",clock)


def startMenuClick(ev):
  global startmenu
  global stbtnSelected
  stbtnSelected = not stbtnSelected
  if stbtnSelected:
    startbutton.attrs['src'] = "/content/startmenu/selected.png"
    startmenu.attrs["style"] = "display:block;"
  else:
    startbutton.attrs['src'] = "/content/startmenu/unselected.png"
    startmenu.attrs["style"] = "display:none;" 