from time import sleep
from browser import window;

def loadLanguageChanger(ev):
	exec(fs.load_sys_file("apps/settings/langchanger.py"));
def loadQuickBoot(ev):
	exec(fs.load_sys_file("apps/settings/quickboot.py"));
# def loadSus(ev): 
#   exec(fs.load_sys_file("apps/settings/sus.py"));
def themes(ev):
  exec(fs.load_sys_file("apps/settings/themes.py"))
def switchtoaurora(ev):
  exec(fs.load_sys_file("apps/settings/switch2aurora.py"))

def settings(ev):
  config = Win(lang.get('UDNAPP_Settings'),window.parseKeys(fs.load_sys_file("apps/settings/settings.html"),lang.lang),200,400);
  document["changeLang"].bind('click',loadLanguageChanger)
  document["quickBoot"].bind('click',loadQuickBoot)
  # document["enableSus"].bind('click',loadSus)
  document["changeThemes"].bind("click", themes)
  document["SwitchToAurora"].bind("click", switchtoaurora)
	
registerApp(
  App(
    "Settings",
    "settings.png",
    settings
  )
)