from browser import document,html, alert, console, window
from browser.local_storage import storage

openWindows = []

class Win:
  def __init__(self, name, innerHTML, width, height, invis=False):
    self.invis = invis
    if not invis:
      self.title = name
      self.windowclose = html.DIV()
      self.windowclose <= "✖";
      self.windowclose.attrs["class"] = "app-close-button";
      self.windowclose.bind('click',self.close)
      self.windowminimize = html.DIV()
      self.windowminimize <= "🗕";
      self.windowminimize.attrs["class"]="app-minimize-button";
      self.windowminimize.bind('click',self.minimize)
      self.windowtop = html.DIV()
      self.windowtop.attrs["id"] = f"windows-top-{name}"
      self.windowtop.attrs["class"] = "windows-top"
      self.windowtop <= name
      self.windowtop.attrs["style"] = f"height:30px;width:{width}px;"
      self.windowtop.appendChild(self.windowclose);
      self.windowtop.appendChild(self.windowminimize)
      self.windowcontent = html.DIV()
      self.windowcontent.attrs["id"] = f"windows-content-{name}"
      self.windowcontent.attrs["style"] = f"width:{width}px;height:{height}px;"
      self.windowcontent.attrs["class"] = "windows-content"
      self.windowcontent.html = innerHTML
      self.windowContainer = html.DIV()
      self.windowContainer.attrs["id"] = f"window-{name}"
      self.windowContainer.attrs["class"] = "windows"
      self.windowContainer.appendChild(self.windowtop)
      self.windowContainer.appendChild(self.windowcontent)
      self.dragging = False
      self.minimized = False
      #self.windowtop.bind("drag",self.drag)
      #self.windowtop.bind("dragstart", self.dragBegin)
      #self.windowtop.bind("dragend", self.dragEnd);
      self.windowtop.bind('mousedown',self.dragBegin);
      self.pos1 = 0;
      self.pos2 = 0;
      self.pos3 = 0;
      self.pos4 = 0;
      desktopElement = document.getElementById("desktop")
      desktopElement.appendChild(self.windowContainer)
    else:
      desktopElement = document.getElementById("desktop")
      self.windowContainer = html.DIV()
      self.windowContainer.attrs["id"] = f"window-invis-{name}"
      desktopElement.appendChild(self.windowContainer)
    openWindows.append(self)

  def drag(self, ev):
    if self.dragging and not self.minimized and not self.invis:# and ev.x > 0 and ev.y > 0:
      #print(str(self.windowContainer.style.left))
      self.pos1 = self.pos3 - ev.clientX;
      self.pos2 = self.pos4 - ev.clientY;
      self.pos3 = ev.clientX;
      self.pos4 = ev.clientY;
      self.windowContainer.attrs["style"] = f"left:{self.windowContainer.offsetLeft - self.pos1}px;top:{self.windowContainer.offsetTop - self.pos2}px;"
  def dragBegin(self,ev):
    if not self.minimized and not self.invis:
      ev.preventDefault();
      self.pos3 = ev.clientX;
      self.pos4 = ev.clientY;
      self.dragging = True
      document.bind('mouseup',self.dragEnd);
      document.bind('mousemove',self.drag);
  def dragEnd(self,ev):
    if not self.minimized and not self.invis:
      document.unbind('mouseup')
      document.unbind('mousemove')
      self.dragging = False
  def close(self, ev):
    if not self.minimized and not self.invis:
      self.windowContainer.parentNode.removeChild(self.windowContainer)
  def minimize(self, ev):
    if not self.invis:
      self.minimized = True
      self.windowContainer.attrs["style"] = "display:none;"
      taskbar = document.getElementById("taskbar")
      self.taskbarwinobj = html.DIV()
      self.taskbarwinobj.attrs["id"] = f"taskbar-win-obj-{self.title}"
      self.taskbarwinobj.attrs["class"] = "taskbar-win-obj"
      self.taskbarwinobj <= self.title
      self.taskbarwinobj.bind("click",self.unminimize)
      taskbar.appendChild(self.taskbarwinobj)
  def unminimize(self, ev):
    if not self.invis:
      self.minimized = False
      self.windowContainer.attrs["style"] = "display:block;"
      self.taskbarwinobj.remove()
      self.taskbarwinobj = None


def handleMsgs(e):
  if e.data.event == "openIframe":
    Win(e.data.title,f"<iframe src=\"{e.data.url}\" width=\"100%\" height=\"100%\" style=\"border: none;\">",e.data.width,e.data.height);
  if e.data.event == "DownloadApp":
    storage["$downloadedApp$"+e.data.appname] = e.data.code
    exec(e.data.code)
    reloadApps()
  if e.data.event == "evalPy":
    try:
      e.source.postMessage({
        "event": "evalPy",
        "result": str(eval(e.data.code))
      },"*")
    except Exception as e:
      e.source.postMessage({
        "event": "evalPy",
        "error": str(e)
      },"*")
		# i forgor eval in exec, well that works too
		
window.secondHandler = handleMsgs;