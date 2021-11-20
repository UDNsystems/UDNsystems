from browser import window
def readFile(path):
	data = "";
	file = open(path);
	data = file.read();
	file.close();
	return data;
class Language:
	def __init__(self,name):
		self.name = name;
		self.langFile = readFile(f"lang/{name}.lang");
		self.lang = window.langFileParser(self.langFile); # this is an JSObject class
	def get(self,key):
		if key in self.lang.__dict__:
			return self.lang.__dict__[key];
		else:
			print(f"Non-existing key '{key}' on '{self.name}' language.")
			return key.split("_")[1:]
if not storage.__contains__('language'):
	storage['language'] = "english";
language = storage['language'];

if SUSEnabled:
  language = "sus";
lang = Language(language);