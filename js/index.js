export default function sus() {
    // had to add this to fix global
}
class Cursor {
    line;
    color;
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
    setLine(x) {
        this.line = x;
        return this;
    }
    changeColor(hex) {
        this.color = hex;
        return this;
    }
}
class TextScreen {
    div;
    cursor;
    static instance;
    constructor() {
        this.div = document.createElement('div');
        this.div.id = "screen_container";
        //this.div.style = "font-family: monospace;color:#00FF00;";
        this.div.style.fontFamily = "monospace";
        this.div.style.color = "#00ff00";
        this.div.className = "unfocused";
        document.body.appendChild(this.div);
        this.cursor = new Cursor();
    }
    print(text) {
        const txt = document.createElement("span");
        txt.innerText = text;
        txt.style.color = this.cursor.color;
        this.div.appendChild(txt);
        this.cursor.nextLine();
    }
    changeColor(hex) {
        this.div.style.color = hex;
    }
    changeCursorColor(hex) {
        this.cursor.changeColor(hex);
    }
    printToLine(text, line) {
        const ln = this.div.children[line];
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
function evalPy(code) {
    //@ts-ignore
    return JSON.parse(window.evalPy(code));
}
function execPy(code) {
    //@ts-ignore
    return window.execPy(code);
}
window.evalJS = function (code) {
    return eval(code);
};
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
const screenActions = {
    print(data) {
        TextScreen.instance.print(data.text);
    },
    changeColor(data) {
        TextScreen.instance.changeColor(data.hex);
    },
    changeCursorColor(data) {
        TextScreen.instance.changeCursorColor(data.hex);
    },
    clear() {
        TextScreen.instance.clear();
    },
    printToLine(data) {
        TextScreen.instance.printToLine(data.text, data.line);
    },
    evalJS(data, message) {
        try {
            message.source.postMessage({
                action: 'evalJS',
                data: eval(data.code)
            }, '*');
        }
        catch (err) {
            console.error(err);
        }
    },
    evalPy(data, message) {
        try {
            let output = window.evalPy(data.code);
            message.source.postMessage({
                action: 'evalPy',
                data: output
            }, '*');
        }
        catch (err) {
            console.error(err);
            message.source.postMessage({
                action: 'evalPy',
                data: err,
                error: true
            }, '*');
        }
    },
    // udn apis
    storageGetKeys(data, message) {
        console.log(message.source);
        message.source.postMessage({
            action: data.action,
            data: Object.keys(localStorage)
        }, "*");
    },
    getStorageKey(data, message) {
        message.source.postMessage({
            action: data.action,
            data: localStorage.getItem(data.data)
        }, "*");
    },
    setStorageKey(data) {
        localStorage.setItem(data.key, data.value);
    },
    removeStorageKey(data) {
        localStorage.removeItem(data.key);
    },
    shutdown() {
        if (window.onerror)
            window.onerror('ACPI Shutdown.');
    },
    setLocalforageItem(data, message) {
        window.localforage.setItem(data.key, data.value).then(() => message.source.postMessage({ action: data.action }, '*'));
    },
    async getLocalforageItem(data, message) {
        return message.source.postMessage({
            action: data.action,
            data: await window.localforage.getItem(data.key)
        }, '*');
    },
    removeLocalforageItem(data, message) {
        window.localforage.removeItem(data.key).then(() => message.source.postMessage({ action: data.action }, '*'));
    },
    async lfWriteChar(data, message) {
        if (data.char.length > 1)
            return console.error('not a char');
        let item = await window.localforage.getItem(data.key);
        item += data.char;
        await window.localforage.setItem(data.key, item);
        message.source.postMessage({ action: data.action }, '*');
    }
};
function secondHandler(e) { }
class OSAPIError {
    name;
    message;
    constructor(name, message) {
        this.name = name;
        this.message = message;
    }
}
function OSAPI_GenerateMessageID() {
    return Math.floor(Math.random() * 99999999);
}
window.onmessage = function (message) {
    /*const data = message.data;
    const action = screenActions[data.action];
    console.log(`[TASK] Action=${data.action} Data=${JSON.stringify(data)}`)
    if (action) return action(data, message);
    //TextScreen.instance.println(data.text);
      secondHandler(message);*/
    if (!message)
        return;
    if (!message.source)
        return;
    //console.log(message.data)
    if (message.data.hasOwnProperty('response'))
        return;
    console.log(message.data);
    const requestMessage = message.data;
    const request = requestMessage.request;
    const messageId = requestMessage.messageId;
    const origin = requestMessage.origin;
    let rawPostMessageReply = message.source.postMessage;
    if (!rawPostMessageReply)
        return;
    const action = request.action;
    const kind = request.kind;
    const requestBody = request.body;
    let func = OSAPIFunctions[`${action}$${kind}`];
    let replyFunc = function (data) {
        if (data instanceof OSAPIError) {
            return rawPostMessageReply({
                response: {
                    error: {
                        name: data.name,
                        message: data.message,
                        str: `${data.name}: ${data.message}`
                    }
                },
                status: 1,
                messageId
            });
        }
        return rawPostMessageReply({
            response: data,
            status: 0,
            messageId
        });
    };
    func(replyFunc, requestBody);
};
const OSAPIFunctions = {
    POST$open_alert(reply, body) {
        reply(null);
        alert(body.text);
    },
    POST$BOS_print(reply, body) {
        TextScreen.instance.print(body);
        reply(null);
    },
    DELETE$BOS_clear(reply, body) {
        TextScreen.instance.clear();
        reply(null);
    },
    PATCH$BOS_color(reply, body) {
        TextScreen.instance.changeColor(body);
        reply(null);
    },
    POST$BOS_printToLine(reply, body) {
        TextScreen.instance.printToLine(body.text, body.line);
        reply(null);
    },
    PATCH$BOS_cursorColor(reply, body) {
        TextScreen.instance.changeCursorColor(body);
        reply(null);
    },
    GET$localStorage(reply, body) {
        reply(localStorage.getItem(body));
    },
    POST$localStorage(reply, body) {
        localStorage.setItem(body.key, body.value);
        reply(null);
    }
};
window.OSAPIFunctions = OSAPIFunctions;
function langFileParser(data) {
    function parseLine(text) {
        let lp = text.split('=');
        if (lp[1].startsWith('base64:')) {
            lp[1] = atob(lp[1].slice('base64:'.length));
        }
        return [
            lp[0],
            lp[1]
        ];
    }
    const lines = data
        .replace(/#(.*)\n/g, "")
        .replace(/\n+/g, "\n")
        .split(/;\n|;/g);
    var newJSON = {};
    for (let line of lines) {
        if (line === "")
            continue;
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
function parseKeys(text, json) {
    return text
        .replace(/{key\.(.*)}/g, (str, name) => {
        console.log(name);
        return json[name];
    });
}
window.startupSound = function () {
    var audio = new Audio("content/system/startup.mp3");
    audio.play();
}; // warning.wav error.wav ding.wav
window.shutdownSound = function () {
    var audio = new Audio("content/system/shutdown.wav");
    audio.play();
};
window.warningSound = function () {
    var audio = new Audio("content/system/sounds/warning.wav");
    audio.play();
};
window.errorSound = function () {
    var audio = new Audio("content/system/sounds/error.wav");
    audio.play();
};
window.informationSound = function () {
    var audio = new Audio("content/system/sounds/info.wav");
    audio.play();
};
window.evalJS = function (code) {
    return eval(code);
};
window.setupAmogusClock = function () {
    var clockobj = document.createElement("DIV");
    clockobj.id = "taskbar.CLOCK";
    let taskbar = document.getElementById("taskbar");
    if (taskbar)
        taskbar.appendChild(clockobj);
    setInterval(function () {
        var time = new Date();
        var combinedTime = time.getHours().toString + ":" + time.getMinutes().toString();
        clockobj.innerHTML = combinedTime;
    });
};
/*let bak = $B.run_script;
$B.run_script = function(src, name, url, run_loop) {
    console.log('call',src,name,url,run_loop)
    return bak(src, name, url, run_loop);
}*/
//startup
document.addEventListener('DOMContentLoaded', async () => {
    let duckv = await window.localforage.getItem('/bootloader/boot.py');
    let bootScript = duckv || await (await fetch('/scripts/boot.py')).text();
    window.$B.run_script(bootScript, '__main__', 'https://udn-systems.udnsystems.repl.co/scripts/boot.py', true); // wtf is a B
});
