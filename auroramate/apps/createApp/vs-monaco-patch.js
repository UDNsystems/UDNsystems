document.addEventListener('DOMContentLoaded',() => {
	setTimeout(_ => {
		document.querySelectorAll('.slider')[1].style.left = "471px";
		document.querySelector('div[widgetid="editor.contrib.quickInputWidget"]').style.position = "fixed";
		document.querySelector('div[widgetid="editor.contrib.quickInputWidget"]').style.top = "5px";
		
	},500)
	
})
document.querySelector('#container').addEventListener('keydown', function(ev) {
	if (ev.key === "F1") {
		document.querySelectorAll('.slider')[3].style.left = "362px";
	}
});
document.body.onkeydown = function(ev) {
	if (ev.key === "F1") {
		ev.preventDefault();
	}
}