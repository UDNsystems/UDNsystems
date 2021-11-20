from browser import document

abouthtmlcode = '''
<h2>why does this exist<h2>
AuroraMATE is a development and testing enviroment. You can register apps here and experiment with the filesystem. Though the filesystem wont be reset so be careful! Other custom made apps will be reset.'''

def about(ev):
  Win("About", abouthtmlcode, 200, 200)