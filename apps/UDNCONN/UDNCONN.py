from browser import aio, prompt, alert
from browser.local_storage import storage;
import javascript

author = ""
bypass = "https://corsanywhere.herokuapp.com/"
def prerunUDN(ev):
  aio.run(UDNCONNECT(ev))
def ducktestRun(ev):
  aio.run(checkMsg(ev))
def submitName(ev):
  global author
  author = document.getElementById("author").value
  document.getElementById("applyName").unbind("click")
  document.getElementById("namereq").parentNode.removeChild(document.getElementById("namereq"))
  print(author)
  sendingContainer = html.DIV()
  sendingContainer.attrs["id"] = "senderstuff"
  msgTxtbar = html.INPUT()
  msgTxtbar.attrs["placeholder"] = "insert message here"
  msgTxtbar.attrs["id"] = "msg"
  btn = html.A();
  btn.attrs['href'] = "#";
  btn.attrs["id"] = "sendmsg"
  btn.className = "btn";
  btn <= "send"
  btn2 = html.A()
  btn2.attrs["href"] = "#"
  btn2.attrs["id"] = "ducktest"
  btn2.attrs["class"] = "btn"
  btn2 <= "getMsgTest"
  sendingContainer.appendChild(msgTxtbar)
  sendingContainer.appendChild(btn)
  sendingContainer.appendChild(btn2)
  document.getElementById("windows-content-UDN console").appendChild(sendingContainer)
  btn.bind("click",sendMsgRun)
  btn2.bind("click",ducktestRun)
async def checkMsg(ev):
  global bypass
  req = (await window.axios.get("https://pyduck.codersquack.ml/udn/getmessage"))
  #json = str(req.data).replace("'", '"')
  #print(str(javascript.JSON.parse(json)["msg"]))
  print(req.data)
  print("requested!!!!")
  print(str(req.data))
  print(javascript.JSON.parse(req.data))
async def sendMsg(ev):
  global author, bypass
  msg = document.getElementById("msg").value
  req = (await window.axios.get(f"https://pyduck.codersquack.ml/udn/postmessage?msg={msg}&author={author}"))
  document.getElementById("msg").value = ""
def sendMsgRun(ev):
  aio.run(sendMsg(ev))
async def UDNCONNECT(ev):
  bypass = "https://corsanywhere.herokuapp.com/"
  #req = (await window.axios.get(f"{bypass}nothttps://pyduck.fox551.repl.co/udn/postmessage")).data;
  author = ""
  f = open("apps/UDNCONN/ui.html")
  stuff = f.read()
  f.close()
  theWindow = Win("UDN console", stuff, 500, 500)
  #naming sys
  document.getElementById("applyName").bind("click",submitName)
registerApp(
  App(
    "UDN",
    "cloudduck.png",
    prerunUDN
  )
)