from browser import document,html, alert, console, window
class Popup:
  def __init__(self, name, popuptype, innerHTML):
    self.title = name
    self.windowclose = html.DIV()
    self.windowclose <= "✖";
    self.windowclose.attrs["class"] = "app-close-button";
    self.windowclose.bind('click',self.close)
    self.windowtop = html.DIV()
    self.windowtop.attrs["id"] = f"windows-top-{name}"
    self.windowtop.attrs["class"] = "windows-top"
    self.windowtop <= name
    ### UTIL CALC
    calculatedSize = Util.TextToPX(innerHTML)
    calculatedSize["x"] -= 76
    calculatedSize["y"] = 20
    x = calculatedSize["x"]
    y = calculatedSize["y"]
    self.windowtop.attrs["style"] = f"height:{y}px;width:{x}px;"
    self.windowtop.appendChild(self.windowclose);
    self.windowcontent = html.DIV()
    self.windowcontent.attrs["id"] = f"windows-content-{name}"
    self.windowcontent.attrs["style"] = f"width:{x}px;height:{y}px;"
    self.windowcontent.attrs["class"] = "windows-content"
    # popup type anchor
    if popuptype == "Warning":
      self.windowcontent.html = "<img src='content/system/systemicons/warning.png' width='22' height='20'/><duck style='font-size:22;'>"+innerHTML+"</duck>"
      window.warningSound()
    elif popuptype == "Error":
      self.windowcontent.html = "<img src='content/system/systemicons/error.png' width='22' height='20'/><duck style='font-size:22;'>"+innerHTML+"</duck>"
      window.errorSound()
    elif popuptype == "Info":
      print("popuptype unducked :D")
      self.windowcontent.html = "<img src='content/system/systemicons/icon.svg' width='22' height='20'/><duck style='font-size:16;'>"+innerHTML+"</duck>"
      window.informationSound()
    # end of popup type stuff
    self.windowContainer = html.DIV()
    self.windowContainer.attrs["id"] = f"window-{name}"
    self.windowContainer.attrs["class"] = "windows"
    #self.windowContainer.attrs['style'] = "top: 0; left: 0;"
    self.windowContainer.appendChild(self.windowtop)
    self.windowContainer.appendChild(self.windowcontent)
    self.dragging = False
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
    openWindows.append(self)

  def drag(self, ev):
    if self.dragging:# and ev.x > 0 and ev.y > 0:
      #print(str(self.windowContainer.style.left))
      self.pos1 = self.pos3 - ev.clientX;
      self.pos2 = self.pos4 - ev.clientY;
      self.pos3 = ev.clientX;
      self.pos4 = ev.clientY;
      self.windowContainer.attrs["style"] = f"left:{self.windowContainer.offsetLeft - self.pos1}px;top:{self.windowContainer.offsetTop - self.pos2}px;"
  def dragBegin(self,ev):
    ev.preventDefault();
    self.pos3 = ev.clientX;
    self.pos4 = ev.clientY;
    self.dragging = True
    document.bind('mouseup',self.dragEnd);
    document.bind('mousemove',self.drag);
  def dragEnd(self,ev):
    document.unbind('mouseup')
    document.unbind('mousemove')
    self.dragging = False
  def close(self, ev):                 
    self.windowContainer.parentNode.removeChild(self.windowContainer)