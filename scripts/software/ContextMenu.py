from browser import document, html
class Menu:
  def __init__(self, name, width, height):
    self.name = name
    menu = html.DIV()
    menu.attrs["class"] = "Menu"
    menu.attrs["id"] = "Menu-"+name
    menu.attrs["style"] = f"top:{height}px;left:{width}px;"
  def addElement(self, element):
    menu.html += "<div id='menu-elemen
    