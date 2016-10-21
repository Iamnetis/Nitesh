import requests

url= "https://nikhil.info.np"

newname = requests.get(url)

if  newname.status_code == 200:
	print (newname.text)

else:
	print("pThere was an error loading the page")
	print("status code:%d %  newname.status.code")
