from browser import document, html, window
'''class Screen:
  def __init__(self):
    self.screen = document.createElement("div")
    self.screen.attrs["style"] = "font-family: monospace;color:#00FF00;"
    self.screen.attrs["id"] = "screen_container"
    document.body.appendChild(self.screen)
		#self.println("Sussy baka.")#test
    print("finished da screen") this part has been multi-commented out, ignore
  def println(self,text):
    self.screen <= text+html.BR()
  def getData(self):
    return self.screen.innerHTML
  def println_col(self,text,color="#00FF00"):
    te = document.createElement("ColorPrint") # te stands for temporary element
    te.attrs["style"] = f"color:{color};"
    te.innerHTML = text
    self.screen <= te + html.BR()
  def clear(self):
    screen.parentNode.removeChild(screen)
    self.screen = document.createElement("div")
    self.screen.attrs["style"] = "font-family: monospace;color:#00FF00;"
    self.screen.attrs["id"] = "screen_container"
    document.body.appendChild(self.screen)'''
class Screen:
	def __init__(self):
		pass
	def println(self,text):
		window.postMessage({
			'action': 'print',
			'text': text + "\n" 
		},'/')
	def changeColor(self,hex):
		window.postMessage({
			'action': 'changeColor',
			'hex': hex
		},'/')
	def printToLine(self,text,line):
		window.postMessage({
			'action': 'printToLine',
			'text': text,
			'line': line
		},'/')
	def changeCursorColor(self,hex):
		window.postMessage({
			'action': 'changeCursorColor',
			'hex': hex
		},'/')
	def clear(self):
		window.postMessage({
			'action': 'clear'
		},'/')
screen = Screen()