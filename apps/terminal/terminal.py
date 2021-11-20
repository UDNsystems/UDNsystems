'''cmd_input = ""
def term(ev):
  #terminal

  def cmd(e): 
    global cmd_input
    if e.key=="Enter":
      if not cmd_input == "":
        new = document.getElementById("terminal-result").html[:-15]
        try:
          new += "<br>"+str(eval(cmd_input))+"<br>&gt;"
        except Exception as e:
          new += f"<br>{lang.get('error')} "+str(e)+"<br>&gt;"
        document.getElementById("terminal-result") += new
        cmd_input = ""
        
    else:
      cmd_input += e.key.split("\n")[0]
      document.getElementById("terminal-result") <= e.key.split("\n")[0]
  Win(lang.get('UATitle_terminal'), "<div id='terminal-result'>&gt;\n><blink>_</blink>", 300, 300)
  document.getElementById("terminal-result").bind("keypress", cmd)

registerApp(
  App(
    "terminal",
    "terminal.png",
    term
  )
)'''
# Nvm you are doing an rewrite
#Ok
"""cmdIn = ""
def keysus(ev):
  global cmdIn
  print(ev.which)
  if ev.key == "Enter":
    if not cmdIn == "":
      document.getElementById("windows-content-Terminal").html += "<br>"
      try:
        result = str(eval(cmdIn))
        document.getElementById("windows-content-Terminal").html += result + "<br>&gt;"
      except Exception as sus:
        document.getElementById("windows-content-Terminal").html += "<error style='color:#FF0000'>"+str(sus) + "</error><br>&gt;"
      cmdIn = ""
    elif ev.key == "Backspace":
      cmdIn = cmdIn[:-1]
      print("backspace!")
      document.getElementById("windows-content-Terminal")[:-1]
    else:
      cmdIn = ""
      document.getElementById("windows-content-Terminal") = cmdIn
  else:
    cmdIn += ev.key
    
def term(ev):
  Win("Terminal", "&gt;", 300, 300)
  document.body.bind("keypress",keysus)"""
def term(ev):
	Win("Terminal", "<iframe src=\"https://terminal.udnsystems.repl.co\" width=\"100%\" height=\"100%\" allow=\"clipboard-read; self ${URL}\" style=\"border: none;\"/>", width=800, height=500) # wait can u copy all code to the terminal folder?
	
registerApp(
  App(
    "terminal",
    "terminal.png",
    term
  )
)