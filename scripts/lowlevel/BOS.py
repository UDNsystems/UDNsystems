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
def osapi_send_msg_wnr(action, kind, body):
	return window.postMessage({
		'request': {
			'action': action,
			'kind': kind,
			'body': body
		},
		'messageId': 0, # 0 means you don't want a response back
		'origin': 'self'
	})
class Screen:
	def __init__(self):
		pass
	def println(self,text):
		'''window.postMessage({
			'action': 'print',
			'text': text + "\n" 
		},'/')'''
		osapi_send_msg_wnr('POST','BOS_print', text + "\n");
	def changeColor(self,hex):
		'''window.postMessage({
			'action': 'changeColor',
			'hex': hex
		},'/')'''
		osapi_send_msg_wnr('PATCH','BOS_color', hex);
	def printToLine(self,text,line):
		'''window.postMessage({
			'action': 'printToLine',
			'text': text,
			'line': line
		},'/')'''
		osapi_send_msg_wnr('POST','BOS_printToLine', {'text': text, 'line': line});
	def changeCursorColor(self,hex):
		'''window.postMessage({
			'action': 'changeCursorColor',
			'hex': hex
		},'/')'''
		osapi_send_msg_wnr('PATCH','BOS_cursorColor', hex);
	def clear(self):
		osapi_send_msg_wnr('DELETE','BOS_clear', None);
screen = Screen()