from browser import document

def duck():
	on = lang.get('on');
	off = lang.get('off');
	lc = Win('sus mode',f'''<h1>HOW DID YOU GET HERE SUS MODE IS MOVED TO THEME MENU</h1><!--
	<p class="font">sus mode</p>
	<select id="sus694220">
		<option value="True">{on}</option>
		<option value="False">{off}</option>
	</select>
	<a href="#" class="btn round" onclick="localStorage['sus_mode']=document.querySelector('#sus694220').value;location.reload();">Sus</button> -->
	''',300,200)
  
duck();