import requests
import shutil
#public pic index range in {   47-----441442    <at least>   }  
#rejected pic example: http://www.caoporn.com/media/photos/441119.jpg
 
def getpics(url,index):
	r = requests.get(url, stream=True)
	path=str(index) + '.jpg'
	#print(r.status_code)
	if r.status_code == 200:
		with open(path, 'wb') as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f)
			print(index,'has been saved')
	else: print(index,'rejected')

def auto_count(start,ending):
	for index in range(start,ending):
		url='http://www.caoporn.com/media/photos/'+ str(index)
		#url='http://www.caoporn.com/media/photos/'+ str(index) + 'jpg'
		getpics(url,index)
	print('pics from: ',start,' to ',ending,' finished! ')

auto_count(?,?)
