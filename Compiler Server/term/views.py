from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import program
from .models import author
from .serializers import programSerializer
from .serializers import authorSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import json
import os
import random
import time


ip_list=[]
check_time=time.time()
def user_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return (ip)


def filter_address(ip,start_time):
	
	flag=0
	d=dict()
	d[ip]=start_time
	print("chandu")
	if ip_list:
		print("hi chandu")
		for var in ip_list:
			if ip in var:
				if start_time-list(var.values())[0] < 6:
					print("cooldown for this ip {}".format(ip))
					var[ip]=start_time
				else:
					var[ip]=start_time
					flag=1
			else:
				ip_list.append(d)
				flag=1

		if time.time()-check_time>20:
			for var in ip_list:
				if time.time()-list(var.values())[0]>20:
					ip_list.remove(var)
			check_time=time.time()
	else:
		print("adding")
		ip_list.append(d)
		flag=1


	print("flag={}".format(flag))
	return flag

# Create your views here.
class ProgramList(APIView):

	def get(self,request,format=None):
		program_list=program.objects.all()
		serializer=programSerializer(program_list,many=True)
		# print("hello1")
		return Response(serializer.data)



	# def post(self):
	# 	pass

	# def post(self, request, format=None):
	#         if request.method=='POST':
	#         	print("Submitting solution")
	# 	        serializer = programSerializer(data=request.data)
	# 	        if serializer.is_valid():
	# 	            print("hello0")
	# 	            serializer.save()
	# 	            from soln.tasks import compile
	# 	            #print("hello3")
	# 	            Compile=compile()
	# 	            Compile.compilers()
	# 	            return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	##################################################################################################

	def post(self, request, format=None):
	        if request.method=='POST':
	        	start_time=time.time()
	        	if(filter_address(user_ip_address(request),start_time)==0):
	        		return Response({'status':'cooldown time'},status=status.HTTP_400_BAD_REQUEST)
		        serializer = programSerializer(data=request.data)
		        if serializer.is_valid():
		            serializer.save()
		            idx=request.data['sol_id']
		            from soln.tasks import compile
		            Compile=compile()
		            Compile.compilers(idx,request.data['language'])
                    send="/soln/"+idx+".send"

		            myfile=open(send,"rt")
		            Lines=myfile.readlines()
		            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		            verdict=""
		            timer=""
		            message=""

		            if(Lines[0].strip()=="ce"):
		            	verdict=verdict+Lines[0].strip()
		            	verdict=verdict.replace("\n","")
		            	for line in Lines[1:]:
		            		message=message+line
		            	message=message.replace("\n","")

		            if(Lines[0].strip()=="wa" or Lines[0].strip()=="ac"):
		            	verdict=verdict+Lines[0].strip()
		            	verdict=verdict.replace("\n","")
		            	timer=timer+Lines[1].strip()
		            	timer=timer.replace("\n","\n")

		            if(Lines[0].strip()=="tle"):
		            	verdict=verdict+Lines[0].strip()
		            	verdict=verdict.replace("\n","")

		            # result={'verdict': verdict , 'time': time , 'message': message}

		            os.remove(send)
		            return Response({'verdict': verdict , 'time': timer , 'message': message}, status=status.HTTP_201_CREATED)
		        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class AuthorList(APIView):

	def get(self,request,format=None):
		author_list=author.objects.all()
		serializer=authorSerializer(author_list,many=True)
		# print("hello1")
		return Response(serializer.data)

	def post(self,request,format=None):
		if request.method=='POST':
			start_time=time.time()
			if(filter_address(user_ip_address(request),start_time)==0):
				return Response({'status':'cooldown time'},status=status.HTTP_400_BAD_REQUEST)
			print("submitting question")
			serializer=authorSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				obj=author.objects.get(sol_id=request.data['sol_id'])
				
				#input rename
				input_rename="media/input/"+request.data['sol_id']+".input"
				os.rename(obj.sol_in.name,input_rename)


				#output rename
				output_rename="media/output/"+request.data['sol_id']+".output"
				# print(obj.sol_out.name)
				os.rename(obj.sol_out.name,output_rename)



				return Response({'status':'Question uploaded'},status=status.HTTP_201_CREATED)
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




