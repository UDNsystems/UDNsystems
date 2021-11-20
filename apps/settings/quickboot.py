from browser import document

def quickboot():
	apply = lang.get('apply')
	title = lang.get('UDNCFG_quickboot')
	on = lang.get('on');
	off = lang.get('off');
	lc = Win(title,f'''
	<p class="font">{title}</p>
	<select id="quickbsel">
		<option value="True">{on}</option>
		<option value="False">{off}</option>
	</select>
	<a href="#" class="btn round" onclick="localStorage['quick-boot'] = document.querySelector('#quickbsel').value; location.reload();">{apply}</button>
	''',300,200)
quickboot();
