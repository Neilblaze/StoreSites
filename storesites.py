import sys
import datetime
import pathlib #pip install pathlib
import webbrowser #comes bundled with python 3.6

class OpenLinks:
	def open_urls_in_browser(self, fname):
		with open(fname, 'r') as file:
			#urls = savelink.get_urls()
			line = file.readline().strip()
			while(line != ''):
			#for url in urls:
				webbrowser.open_new_tab(line)



class SaveLinks:

	def append_urls_to_file(self):
		now = datetime.datetime.now()
		fname=str('links')+'-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt'
		print(fname)
	
		with open(fname, "a") as file:
			urls = self.get_urls()
			for url in urls:
				print("URL: ", url, "\n")
				file.write(url+'\n\n') 
		#file.close() 
	
	
if __name__ == "__main__":
	main()
