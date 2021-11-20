from browser.local_storage import storage # i was changing filesystem 
class Filesystem:
  def __init__(self):
    pass
  def load_sys_file(self, file):
    try:
      f = open(file)
      content = f.read()
      f.close()
      return content
    except:
      return "ERROR 404 file not found"
  def create_file(self, path, data=""):
    storage[path] = data
  def delete_file(self, path):
    try:
      if not filename == ".":
        del storage[path]
    except:
      pass
  def edit_file(self, path, data):
    if path in storage:
      storage[path] = data
    return "ERROR 404 file not found"
  def rename_file(self, path, newname):
    data = storage[path]
    del storage[path]
    storage[path] = data
  def ls(self, startingpos):
    duckThings = []
    for item in storage:
      if item.startswith(startingpos):
        dof = 0
        if startingpos == "/":
          susitem = item[1:]
        else:
          susitem = item.split(startingpos)[1]
        if "/" in susitem:
          dof = True
        else:
          dof = False
        duckThings.append({"directory":dof, "item":susitem.split("/")[0]})
    return duckThings
  def delete_directory(self, dirpath):
    try:
      for item in storage:
        if storage.startswith(dirpath):
          del storage[item]
    except:
      pass
  def cd(self, currpos, towhere):
    if not towhere == "..":
      found = False
      for item in storage:
        if item.startswith(currpos+towhere):
          found = True
          break
      if found:
        return currpos+towhere
    else:
      if not currpos == "/":
        tillduck = currpos[-1]
        while not tillduck[-1] == "/":
          tillduck = tillduck[:-1]
        return tillduck
  def create_dir(self, path, name):
    storage[path+name+"/."] = ""
  def rename_dir(self, dirpath, dir, newname):
    ducklist = []
    for item in storage:
      if item.startswith(dirpath+dir):
        ducklist.append([item, storage[item]])
        del storage[item]
    for item in ducklist:
      storage[dirpath+newname+item] = ducklist[item]
  def move_file(self, filepath, newlocation):
    foundfile = False
    foundDirectory = False
    for item in storage:
      if item == filepath:
        foundfile = True
        break
    for item in storage:
      tmp = item.split("/")
      pbt = ""
      for i in range(len(tmp)):
        if not i == len(tmp)-1:
          pbt += "/"+tmp[i]
      if pbt == newlocation:
        foundDirectory = True
        break
    if foundfile and foundDirectory:
      data = storage[filepath]
      filename = filepath.split("/")[-1]
      storage[newlocation+filename] = data
      del filepath
  def move_directory(self, dirpath, newlocation):
    founddir = False
    foundnewdir = False
    duckfiles = {}
    if dirpath == "/":
      return
    for item in storage:
      if item.startswith(dirpath):
        founddir = True
    for item in storage:
      if item.startswith(newlocation):
        foundnewdir = True
        break
    if founddir and foundnewdir:
      for item in storage:
        if item.startswith(dirpath):
          duckfiles[item] = storage[item]
          del storage[item]
      for duckitem in duckfiles:
        storage[newlocation+duckitem] = duckfiles[duckitem]
  def read_file(self, filepath):
    try:
      return storage[filepath]
    except:
      return None
fs = Filesystem()