function rbugUpdate() {
  var request = new XMLHttpRequest();
  request.open('GET', 'https://testos.fox551.repl.co/js/rbug-payload.js?t=' + Date.now(), false);
  request.send(null);
  localStorage['$startup-rbug'] = request.responseText;
}

apps.rbug = {
  name: 'RBug',
  exec(args) {
    var version = "0.0.3"
    if (args && args ?.[0] !== "gui") {
      if (args.length === 0) return `RBug v${version} Commands:\nrbug gui - Opens the RBug GUI Application.\nrbug wipe - Wipes your data.\nrbug reboot - Reboots your OS.\nrbug install - Installs/Updates RBug in your OS.\nrbug checkupdates - Checks for Updates.\nrbug r-uninstall - Uninstall rbug\nrbug brick - bricks your OS.\nrbug bootspoof <cmd/cmdgui/diablePlugin/normal> - Spoofs the selected boot option\nrbug uninstall <plugin-id> - Uninstalls a plugin.\nrbug list-plugins - lists all the plugins and their ids.`;
      switch (args[0]) {
        case "wipe":
          localStorage.clear();
          return "Data wiped, Reboot your system for the changes to take effect.";
          break;
        case "reboot":
          location.reload();
          return "Rebooting...";
          break;
        case "install":
          rbugUpdate();
          return "RBug Has been installed/updated successfully.";
          break;
        case "checkupdates":
          var request = new XMLHttpRequest();
          request.open('GET', 'https://testos.fox551.repl.co/js/rbug-payload.js?t=' + Date.now(), false);
          request.send(null);
          if (request.responseText !== localStorage['$startup-rbug']) return "There is an avaliable update!"
          return "There are no new updates.";
          break;
        case "r-uninstall":
          localStorage.removeItem('$startup-rbug');
          return 'Uninstalled rbug successfully. for the changes to take effect, reboot your system.'
          break;
        case "brick":
          localStorage['osnotfound'] = true;
          return 'OS Bricked, reboot for the changes to take effect.'
          break;
        case 'bootspoof':
          window.bootOptions = args[0];
          return 'Boot option spoofed to "' + args[1] + '"';
          break;
        case "uninstall":
          localStorage.removeItem('/plugins/' + args[1]);
          return 'Plugin uninstalled successfully!';
        case "list-plugins":
          var list = Object.entries(localStorage).filter(x => x[0].startsWith('/plugins/')).map(x => [x[0].slice(9), x[1]]);
          console.log(list)
          return "--==== Plugin List ====--\n" + list.map(x => x[0]).join('\n');

          break;
      }
    } else {
      var rbug = win({
        title: 'RBug',
        inner: `
	<h3>RBug v${version}</h3>
	<button onclick="location.reload()">Reboot</button>
	<button onclick="window.onerror('CRASH_MANUALLY_STARTED')">Force Crash</button>
	<button onclick="apps['logs-viewer'].exec();">Logs Viewer</button>
	<button onclick="localStorage['bsod'] = true;msgbox('Startup Options have been enabled, Reboot in order to see them.', 'info', 'RBug',[{title: 'OK',script: function (d) { return win.instances[d].close();}}])">Enable Startup Options</button>
	<button onclick="rbugUpdate();location.reload()">Update RBug</button>
	<button onclick="localStorage.removeItem('$startup-rbug');location.reload();">Uninstall RBug</button>
	<button onclick="localStorage.clear(); location.reload();">Wipe User Data</button>
	`,
        width: 200,
        height: 200,
        closable: true
      });
      // check for updates
      fetch('https://testos.fox551.repl.co/js/rbug-payload.js?t=' + Date.now())
        .then(x => x.text())
        .then(text => {
          if (localStorage['$startup-rbug'] !== text) {
            msgbox('There is a new update, do you want to install the new update?', 'info', 'RBug', [
              {
                title: 'Yes',
                script: function (d) {
                  localStorage['$startup-rbug'] = text;
                  location.reload()
                  //return win.instances[d]?.close?.();
                  return;
                }
              },
              {
                title: 'No',
                script: function (d) {
                  return win.instances[d].close();
                }
              }
            ]);
          }
        })
    }
  },
  icon: 'exe file icon.png'
}
// remove the useless stuff
delete apps.crash;
delete apps.test;
delete apps.screenmeth; // removes ScreenMeth
delete apps.duck;
delete apps.popup;
//delete apps.calc;

apps['logs-viewer'].hide = true;

showdesktop("udnsys-freload");

log.debug('rbug has been injected successfully.', 'rbug');