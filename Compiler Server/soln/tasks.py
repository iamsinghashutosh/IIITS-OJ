#!/usr/bin/python

import subprocess
# class compile:
# 	def compilers(self):
# 		print ("start")
# 		subprocess.call("/home/zeff/Desktop/app/bunty/soln/run.sh",shell=True)
# 		print ("end")'


#------------------------------------------------------------------------------------


# class compile:
# 	def compilers(self,language):
# 		print(language)
# 		print ("start")
# 		var=""
# 		if(language=="c" or language=="c++"):
# 			var=var+subprocess.call("/home/zeff/Desktop/app/bunty/soln/c++.sh",shell=False)

# 		if(language=="java"):
# 			var=var+subprocess.call("/home/zeff/Desktop/app/bunty/soln/java.sh",shell=False)

# 		if(language=="python3"):
# 			var=var+subprocess.call("/home/zeff/Desktop/app/bunty/soln/python3.sh",shell=False)

# 		print(var)
# 		print ("end")

# 		return(var)




# class compile:
# 	def compilers(self,sol_name,language,idx):
# 		# print(idx)
# 		# print(language)
# 		# print ("start")
# 		ra=str(idx)
# 		# print(k)
# 		if(language=="c" or language=="c++"):
# 			subprocess.call(['/home/zeff/Desktop/app/bunty/soln/c++.sh',ra,sol_name],shell=False)

# 		if(language=="java"):
# 			subprocess.call(['/home/zeff/Desktop/app/bunty/soln/java.sh',ra,sol_name],shell=False)

# 		if(language=="python3"):
# 			subprocess.call(['/home/zeff/Desktop/app/bunty/soln/python3.sh',ra,sol_name],shell=False)
# 		# print ("end")



class compile:
	def compilers(self,sol_name,language,idx):

		if(language=="c" or language=="c++"):
			subprocess.call(['/home/zeff/Desktop/app/bunty/soln/c++.sh',idx,sol_name],shell=False)

		if(language=="java"):
			subprocess.call(['/home/zeff/Desktop/app/bunty/soln/java.sh',idx,sol_name],shell=False)

		if(language=="python3"):
			subprocess.call(['/home/zeff/Desktop/app/bunty/soln/python3.sh',idx,sol_name],shell=False)
		# print ("end")
