const konsole = {
	print(text) {
		let cssArgs = [];
		text = text.replace(/\{(\/?)(#?)([a-z0-9]+)\}/g, (str, isClosing, isHex, colorName) => {
			if (isClosing) {
				cssArgs.push('color: unset;');
			} else {
				cssArgs.push(`color: ${isHex}${colorName};`);
			}
			return '%c';
		})
		return console.log(text, ...cssArgs)
	},
	highlight(text, lang = "js") {
		return this.highlight_languages[lang].main(text);
	},
	highlight_languages: {
		js: {
			replacements: {
				//[/(-?)(\d+)\.(\d+)/g]: "cyan", // float number
				[/\d+/g]: "cyan", // number
				[/"(\\\\|\\"|[^"])*"/g]: "#ce9178", // string
				[/\/\/.*/g]: "gray", // comment
				[/(\s|^)(function|get|set|return|if|else|this|for|let|var|const|in)/g]: "blue", //keywords
				[/(={1,3})/g]: "yellow", // operations
				//[/(\*|\+|-|\/)=/g]: "yellow"
			},
			main(text) {
				for (let regexstr in this.replacements) {
					let color = this.replacements[regexstr];
					let regex_flags = regexstr.match(/\/(.*)\/([a-z]*)/)[2];
					let regex_i = regexstr.match(/\/(.*)\/([a-z]*)/)[1];
					let regex = new RegExp(regex_i, regex_flags);
					text = text.replace(regex, str => `{${color}}${str}{/${color}}`);
				}
				return text;
			}
		}
	}
}
