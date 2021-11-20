SUSEnabled = False
if storage.__contains__('sus_mode'):
  if storage['sus_mode'] == 'True': storage["theme"] = "sus"
  del storage['sus_mode']

try:
  if storage["theme"] == "sus": SUSEnabled = True
  # if storage["language"] == "sus": SUSEnabled = True
except Exception:
  pass