from browser import document, local_storage

currlang = local_storage.storage["language"]
languages = {
  "english": "English - nicejsisverycool @TBSharedAccount",
  "dutch": "Dutch - coder() (@Fox551) and Google Translate (done by @TBSharedAccount)",
  "portuguese": "Portuguese - Google Translate",
  "hindi": "Hindi - sdf @mkcodes",
  "french": "French - Ponali (@Ponali)",
  "russian": "Russian - Magestick (@Nixtrome)",
	"japanese": "Japanese - Magestick (@Nixtrome)", 
	"korean": "Korean - Magestick (@Nixtrome)",
	"chinese": "Chinese - Magestick (@Nixtrome)",
  "spanish": "Spanish - Magestick (@Nixtrome)",
  "galactic": "Galactic - Magestick (@Nixtrome)",
  "duck": "Duck - Magestick (@Nixtrome)",
  "hhhhhhh": "Hhhhhhh - hhhhh (@hhhhhhhhh)"
	# "sus": "Sus - sussy (@abruhuser)" // this language only available on theme menu
	
}
def combineLangs():
  global languages
  combined = ""
  for lang in languages:
    if lang == currlang:
      combined = combined + f"<option value={lang} selected>{languages[lang]}</option>"
    else:
      combined = combined + f"<option value={lang}>{languages[lang]}</option>"
  return combined
def langchanger():
  ls = lang.get('langsel')
  apply = lang.get('apply')
  lc = Win(lang.get('UATitle_changelanguage'),f'''
	<p class="font">{ls}</p>
	<select name="langsel" id="langsel" style="width: 100%;">
		{combineLangs()}
	</select>
	<a href="#" class="btn round" onclick="localStorage.language = document.querySelector('#langsel').value; location.reload();">{apply}</button>
	''',300,200)
langchanger();
