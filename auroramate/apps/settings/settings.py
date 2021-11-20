from browser import document
from browser.local_storage import storage

settingshtml = '''
<h2>Switch versions</h2>
<button id="noasApply" onclick="localStorage['auroramate']=false;location.reload();">Switch Back To Normal UDN</button>
'''

def settings(ev):
  Win("Settings", settingshtml, 200, 200)

registerApp(
  App(
    "AuroraSettings",
    "settings.png",
    settings
  )
)