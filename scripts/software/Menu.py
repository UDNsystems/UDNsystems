from browser import document, html
class Menu:
  def __init__(self, name, width, height, x, y):
    self.name = name
    menu = html.DIV()
    menu.attrs["class"] = "Menu-Objects"
    menu.attrs["id"] = "Menu-Objects"+name
    menu.attrs["style"] = f"width:{height}px;height:{width}px;left:{x}px;top:{y}px;"
    document.getElementById("desktop").appendChild(menu)
  def addElement(self, element):
    menu.html += f"<div class='Menu-Object-Elements' id='Menu-Object-{self.name}-Element-{str(element)}'>{element}</div>"