import os
def cls():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])
cls()
banner = '\n ###################################\n'
banner += ' # ZIP Password Recover#\n'
banner += ' ###################################\n'
banner += ' # Modded By Foysal Ahmed#\n'
banner += ' # Facebook: Foysal Tips And Tricks#\n'
banner += ' # Bangladesh Cyber Security#\n'
banner += ' # YouTube:Foysal Tips And Tricks#\n'
banner += ' ###################################\n'
banner += ' \n'
banner += '\n\n'
banner += ' [1] Zip Password Recover\n'
banner += ' [0] Exit\n'
print banner

a=input(" [?] Enter Number : ")
if a==0:
 import os
 cls()
 print " [!] Good Bye :)"
 quit()
elif a==1:
 #!/usr/bin/python

 import zipfile
 import os
 from time import time
 
 cls()
 textzippass = '''
 #########################################
 # Zip Password Recover (High Speed) #
 #########################################
 # Modded By Foysal Ahmed#
 # Bangladesh Cyber Security#
 # Foysal Tips And Tricks#
 #########################################
 '''
 print textzippass
 file_path = raw_input (" [+] ZIP File Address: ")
 print ""
 word_list = raw_input (" [+] Password List Address: ")
 def main(file_path, word_list):
	try:
		zip_ = zipfile.ZipFile(file_path)
	except zipfile.BadZipfile:
		print " [!] Please check the file's Path. It doesn't seem to be a ZIP file."
		quit()

	password = None 
	i = 0 
	c_t = time()
	with open(word_list, "r") as f: 
		passes = f.readlines() 
		for x in passes:
			i += 1
			password = x.split("\n")[0]  
			try:
				zip_.extractall(pwd=password)
				t_t = time() - c_t 
				print "\n [*] Password Found :)\n" + " [*] Password: "+password+"\n" 
				print " [***] Took %f seconds to Srack the Password. That is, %i attempts per second." % (t_t,i/t_t)
				quit()
			except Exception:
				pass
		print " [X] Sorry, Password Not Found :("
		quit()
 main(file_path, word_list)
