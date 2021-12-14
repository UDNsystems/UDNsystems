export default function sus() {
	// had to add this to fix global
}
interface $B {
	run_script: Function;
}
declare global {
    interface Window {
			startupSound: Function;
			shutdownSound: Function;
			warningSound: Function;
			errorSound: Function;
			informationSound: Function;
			evalJS: Function;
			setupAmogusClock: Function;
			$B: $B;
			evalPy: Function;
			ctx: CanvasRenderingContext2D;
			localforage: any;
			langFileParser: Function;
		}
}

class Cursor {
	line: number;
	color: string;
  constructor() {
    this.line = 0;
    this.color = "";
  }
  nextLine() {
    this.line++;
    return this;
  }
  prevLine() {
    this.line--;
    return this;
  }
  setLine(x: number) {
    this.line = x;
    return this;
  }
  changeColor(hex: string) {
    this.color = hex;
    return this;
  }
}
class TextScreen {
	div: HTMLDivElement
	cursor: Cursor
	static instance: TextScreen
  constructor() {
    this.div = document.createElement('div');
    this.div.id = "screen_container";
    //this.div.style = "font-family: monospace;color:#00FF00;";
		this.div.style.fontFamily = "monospace";
		this.div.style.color = "#00ff00";
    this.div.className = "unfocused"
    document.body.appendChild(this.div);
    this.cursor = new Cursor();
  }
  print(text: string) {
    const txt = document.createElement("span");
    txt.innerText = text;
    txt.style.color = this.cursor.color;
    this.div.appendChild(txt);
    this.cursor.nextLine();
  }
  changeColor(hex: string) {
    this.div.style.color = hex;
  }
  changeCursorColor(hex: string) {
    this.cursor.changeColor(hex);
  }
  printToLine(text: string, line: number) {
    const ln = this.div.children[line] as HTMLElement;
    let oldtxt = ln.innerText.slice(text.length);
    ln.style.color = this.cursor.color;
    ln.innerText = `${text}${oldtxt}\n`;
    this.cursor.setLine(line);
  }
  clear() {
    this.div.innerHTML = "";
    this.cursor.setLine(0);
  }
  hide() {
    this.div.hidden = true;
  }
  show() {
    this.div.hidden = false;
  }
}
function evalPy(code: string) {
	//@ts-ignore
	return JSON.parse(window.evalPy(code));
}
function execPy(code: string) {
	//@ts-ignore
  return window.execPy(code)
}
window.evalJS = function (code: string) {
  return eval(code);
}
// window.onerror = function (err) {
//   document.body.innerHTML = "<p>An error has occured while trying to boot the system, or to do changes from an important function.<br>" + "Technical ".repeat(!(!err.stack)) + "Information: " + (err.stack ? err.stack : err.toString());
//   document.body.style = "background-color:blue;color:white;font-family:monospace;"
//   // var lolwindow = window;
//   // window = new Error("nope"); // hmmmmmm this is not good idea        it prevents from other bsod and prevents from other stuff etc, please dont mind
//   // window.old = lolwindow;
// }; // moved to boot.py
// Ponali plz dont be sus

// deprecated & removed
/*function graphicsMode() {
  TextScreen.instance.hide();
  const canvas: HTMLCanvasElement = document.querySelector('#graphicsSc');
  const ctx = canvas.getContext('2d');
  window.ctx = ctx;
  document.querySelector<HTMLElement>('#graphics').hidden = false;
  document.querySelector<HTMLElement>('#desktop').hidden = true;
  document.querySelector<HTMLElement>('#taskbar').hidden = true;
  document.body.removeAttribute('style');

  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  ctx.fillStyle = "white";
}*/
/*function screenSaver() {
  function choice(...arr: any[]) { return arr[Math.floor(Math.random() * arr.length)]; };
  graphicsMode(); // go into graphics mode
  window.ctx.fillStyle = "white";
  window.ctx.fillText("UDN Systems", Math.floor(window.innerWidth / 2), Math.floor(window.innerHeight / 2))
	let graphicsSc = document.querySelector<HTMLCanvasElement>('#graphicsSc');
	if (!graphicsSc.width || !graphicsSc.height) return;
  setInterval(() => {
    //if (choice(false,false,false,false,false,false,false,false,false,false,false,false,true)) {
    //ctx.clearRect(0,0,document.querySelector('#graphicsSc').width,document.querySelector('#graphicsSc').height)
    //}
    for (var i = 0; i < 1000; i++) {
      window.ctx.fillStyle = choice('red', 'green', 'blue', 'cyan', 'purple', 'yellow', 'gray', 'white', 'brown', 'pink', 'lime')

      window.ctx.fillRect(
        Math.floor(Math.random() * document.querySelector<HTMLCanvasElement>('#graphicsSc')?.width),
        Math.floor(Math.random() * document.querySelector<HTMLCanvasElement>('#graphicsSc')?.height),
        Math.floor(Math.random() * 10),
        Math.floor(Math.random() * 10)
      );
    }
    window.ctx.clearRect(
      Math.floor(Math.random() * graphicsSc.width),
      Math.floor(Math.random() * document.querySelector<HTMLCanvasElement>('#graphicsSc')?.height),
      Math.floor(Math.random() * document.querySelector<HTMLCanvasElement>('#graphicsSc')?.width),
      Math.floor(Math.random() * document.querySelector<HTMLCanvasElement>('#graphicsSc')?.height)
    )
    window.ctx.fillStyle = "white";
    window.ctx.font = "30px monospace";
    window.ctx.clearRect(Math.floor(window.innerWidth / 2) - ("UDN Systems".length + 60), Math.floor(window.innerHeight / 2) - 30, 200, 50)
    window.ctx.fillText("UDN Systems", Math.floor(window.innerWidth / 2) - ("UDN Systems".length + 60), Math.floor(window.innerHeight / 2))
  }, 10)

}*/

TextScreen.instance = new TextScreen();
const screenActions: {[key: string]: Function} = {
  print(data: {text: string}) {
    TextScreen.instance.print(data.text);
  },
  changeColor(data: {hex: string}) {
    TextScreen.instance.changeColor(data.hex);
  },
  changeCursorColor(data: {hex: string}) {
    TextScreen.instance.changeCursorColor(data.hex);
  },
  clear() {
    TextScreen.instance.clear();
  },
  printToLine(data: {text: string; line: number}) {
    TextScreen.instance.printToLine(data.text, data.line);
  },
  evalJS(data: {code: string}, message: any) {
    try {
      message.source.postMessage({
        action: 'evalJS',
        data: eval(data.code)
      }, '*');

    } catch (err) {
      console.error(err)
    }
  },
  evalPy(data: {code: string}, message: any) {
    try {
      let output = window.evalPy(data.code);

      message.source.postMessage({
        action: 'evalPy',
        data: output
      }, '*');

    } catch (err) {
      console.error(err)
      message.source.postMessage({
        action: 'evalPy',
        data: err,
        error: true
      }, '*')
    }
  },
  // udn apis
  storageGetKeys(data: {action: string}, message: any) {
    console.log(message.source)
    message.source.postMessage({
      action: data.action,
      data: Object.keys(localStorage)
    }, "*");
  },
  getStorageKey(data: {action: string; data: string}, message: any) {
    message.source.postMessage({
      action: data.action,
      data: localStorage.getItem(data.data)
    }, "*")
  },
  setStorageKey(data: {key: string; value: string;}) {
    localStorage.setItem(data.key, data.value)
  },
  removeStorageKey(data: {key: string;}) {
    localStorage.removeItem(data.key);
  },
  shutdown() {
    if (window.onerror) window.onerror('ACPI Shutdown.');
  },
	setLocalforageItem(data: {key: string; value: string; action: string}, message: any) {
		window.localforage.setItem(data.key, data.value).then(() => message.source.postMessage({action: data.action},'*'))
	},
	async getLocalforageItem(data: {action: string; key: string}, message: any) {
		return message.source.postMessage({
			action: data.action,
			data: await window.localforage.getItem(data.key)
		},'*')
	},
	removeLocalforageItem(data: {key: string; action: string}, message: any) {
		window.localforage.removeItem(data.key).then(() => message.source.postMessage({action: data.action},'*'))
	},
	async lfWriteChar(data: {key: string; char: string; action: string;}, message: any) {
		if (data.char.length > 1) return console.error('not a char');
		let item = await window.localforage.getItem(data.key);
		item += data.char;
		await window.localforage.setItem(data.key, item);
		message.source.postMessage({action: data.action},'*')
	}
}
function secondHandler(e: any) {}
window.onmessage = function (message: any) {
  const data = message.data;
  const action = screenActions[data.action];
  console.log(`[TASK] Action=${data.action} Data=${JSON.stringify(data)}`)
  if (action) return action(data, message);
  //TextScreen.instance.println(data.text);
	secondHandler(message);
}

function langFileParser(data: string) {
  function parseLine(text: string) {
    let lp = text.split('=');
    if (lp[1].startsWith('base64:')) {
      lp[1] = atob(lp[1].slice('base64:'.length));
    }
    return [
      lp[0],
      lp[1]
    ]
  }
  const lines = data
    .replace(/#(.*)\n/g, "")
    .replace(/\n+/g, "\n")
    .split(/;\n|;/g);

  var newJSON: {[key: string]: string} = {};
  for (let line of lines) {
    if (line === "") continue;
    let res = parseLine(line);
    let name = res[0];
    let text = res[1];
    newJSON[name] = text;
  }
  console.log('Language file parsed', newJSON);
  // didn't work *intense breathing*
  return newJSON;
  // wait enable notifications and click on the notification when i send a message maybe that will work
}
window.langFileParser = langFileParser;
function parseKeys(text: string, json: {[key: string]: string}) {
  return text
    .replace(/{key\.(.*)}/g, (str: string, name: string) => {
      console.log(name);
      return json[name]
    });
}
window.startupSound = function () {
  var audio = new Audio("content/system/startup.mp3");
  audio.play()
} // warning.wav error.wav ding.wav
window.shutdownSound = function () {
  var audio = new Audio("content/system/shutdown.wav");
  audio.play()
}
window.warningSound = function () {
  var audio = new Audio("content/system/sounds/warning.wav");
  audio.play();
}
window.errorSound = function () {
  var audio = new Audio("content/system/sounds/error.wav");
  audio.play();
}
window.informationSound = function () {
  var audio = new Audio("content/system/sounds/info.wav");
  audio.play();
}
window.evalJS = function(code: string){
  return eval(code)
}
window.setupAmogusClock = function(){
  var clockobj = document.createElement("DIV")
  clockobj.id = "taskbar.CLOCK"
	let taskbar = document.getElementById("taskbar");
  if (taskbar) taskbar.appendChild(clockobj);
  setInterval(function(){
    var time = new Date()
    var combinedTime = time.getHours().toString+":"+time.getMinutes().toString();
    clockobj.innerHTML = combinedTime;
  })
};
/*let bak = $B.run_script;
$B.run_script = function(src, name, url, run_loop) {
	console.log('call',src,name,url,run_loop)
	return bak(src, name, url, run_loop);
}*/
//startup
document.addEventListener('DOMContentLoaded', async()=>{
	let duckv: string | null = await window.localforage.getItem('/bootloader/boot.py');
	
	let bootScript: string = duckv || await (await fetch('/scripts/boot.py')).text();
	
	window.$B.run_script(bootScript, '__main__', 'https://udn-systems.udnsystems.repl.co/scripts/boot.py', true); // wtf is a B
});