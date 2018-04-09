
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.CommandLineAuth() #透過授權碼認證

drive = GoogleDrive(gauth)
file1 = drive.CreateFile({'title': 'Hello1.txt'})
file1.SetContentString('媽～我在這裡！')
file1.Upload() # Files.insert()
