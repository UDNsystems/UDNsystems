function loadScript(url) {
	let s = document.createElement('script');
	s.src = url;
	document.body.appendChild(s);
	return s;
}

loadScript('https://gildas-lormeau.github.io/zip.js/demos/lib/zip.min.js');

let UPEX = (function() {
	let isTerminal = location.hostname === "terminal.udnsystems.repl.co";
	class UPEXError extends Error {
		constructor(message = "", ...args) {
			super(message, ...args);
		}
	}
	const model = (() => {

		return {
			getEntries(file, options) {
				return (new zip.ZipReader(new zip.BlobReader(file))).getEntries(options);
			},
			async getData(entry, options) {
				return await entry.getData(new zip.BlobWriter(), options);
			}
		};

	})();
	return {
		async compileFromLocalFile() {
			let file = new Blob([await (await showOpenFilePicker())[0].getFile()],{type: 'zip'});
			return await this.compile(file);
		},
		async compile(blob) {
			console.log('[upex] unzipping upex file...');
			let entries = await model.getEntries(blob);
			console.log('[upex] unzipped');
			
			let manifestFile = null;
			console.log('[upex] looking for the index.js file')
			for (let file of entries) {
				console.log(file)
				if (file.filename === "index.js") {
					manifestFile = file;
				}
			}
			if (!manifestFile) throw new UPEXError('unable to find index.js');
			console.log('[upex] setting up vfs...');
			let vfs = {}; 
			for (let file of entries) {
				vfs[file.filename] = await (await model.getData(file)).text();
			}
			console.log('[upex] compiling to js function...');
			return (new Function('vfs',vfs['index.js'])).bind(this, vfs);
		}
	}
})();