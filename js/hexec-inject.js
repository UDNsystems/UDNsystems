/*var oldHandler = window.onmessage;

window.onmessage = async function (e) {
  console.log('got event', e.data)
  if (e.data.event === "desktopLoaded" && e.data.arg !== "udnsys-freload") {
    console.log('[RBug] Injecting RBug...')
    var ifduck = document.querySelector('iframe[src="https://hexec.dateplays.repl.co/"]').contentWindow;
    var payload = await (await fetch('/js/rbug-payload.js')).text();

    console.log('payload:', payload)
    ifduck.postMessage({ event: 'eval', data: payload }, "*");

  }
  oldHandler(e)
	secondHandler(e);
}*/