# Sets up extra functions on the OSAPI.
from browser import window
def OSAPI_Init():
	#sussy decorator
	def OSAPIFunction(x):
		def decorator(func):
			window.OSAPIFunctions[x] = func;
		return decorator;
	@OSAPIFunction("POST$createWindow")
	def createWin(reply, body):
		duckwin = Win(body.name, body.innerHTML, body.width, body.height)
		reply(None)
	@OSAPIFunction("POST$showPopup")
	def showPopup(reply, body):
		duckpopup = Popup(body.name, body.popuptype, body.text);
		reply(None)
	@OSAPIFunction("POST$registerApp")
	def regApp(reply, body):
		def wrapperDuck(ev):
			exec(body.code, globals());
		App(body.name, body.icon, wrapperDuck, body.customIcon);
		reply(None);
	@OSAPIFunction("POST$reloadApps")
	def relApps(reply, body):
		reloadApps()
		reply(None);
	
OSAPI_Init();