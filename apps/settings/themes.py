from browser import document, local_storage

currtheme = local_storage.storage["theme"]
wallpapers = {
  "classic": "Classic",
  "default": "Modern",
  "img1": "Blue Box",
  "img2": "Green Box",
  "img3": "Space Travel",
  "bliss": "Bliss Duck",
  "betarelease": "Beta Release Wallpaper",
  "sus": "SUS AMOGUS IMPOSTER"
}

def CombineThemez():
  global wallpapers
  combined = ""
  for wallpapor in wallpapers:
    if wallpapor == currtheme:
      combined = combined + f"<option value={wallpapor} selected>{wallpapers[wallpapor]}</option>"
    else:
      combined = combined + f"<option value={wallpapor}>{wallpapers[wallpapor]}</option>"
  return combined 

def sus():
  data = f'''
	<p class="font">Change Themes</p>
	<select name="Select A Theme!" id="ThemeSelect" style="width: 100%;">
		{CombineThemez()}
	</select>
	<a href="#" class="btn round" onclick="localStorage.theme = document.querySelector('#ThemeSelect').value; location.reload();">Apply!</button>'''
  Win("Change Themes", data, 200, 200)
sus()