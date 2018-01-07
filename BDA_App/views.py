##########################################################
#Import Statements 
##########################################################
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View 
from django.template import Context, loader

import json
import csv
import elasticsearch

##########################################################
#Global Variables
##########################################################
ES_URL = "http://localhost:9200/"

##########################################################
#Views
##########################################################


##########################################################
#API: To push to ES
#Return: 
#URL: http://localhost:8000/BDA/ES/pushData/
##########################################################
class PushData(View):

	def get(self,request):
		res = {}
		obj_list = []
		message = None
		try:
				filepath = request.GET.get('filepath')
				index = request.GET.get('index')
				#filepath = 'C:\\Users\\monu\\Desktop\\python\\data_file.csv'
				#index = 'bda1'
				print("Inside")
				print(filepath,index)
				obj_list = self.parseFile(filepath)
				self.pushData(obj_list,index)

				status = 'Success'
		except Exception as e:
				status = 'Failure, Error: ' + str(e)

		res['message'] = obj_list 
		res['status'] = status
		return HttpResponse(json.dumps(res))


	def parseFile(self,filepath):
		
		obj_list = []

		csvfile = open(filepath,'r')
		csv_reader = csv.reader(csvfile)
		title = next(csv_reader)

		for row_arr in csv_reader:
			mydict = {
						title[0]:row_arr[0], title[1]:row_arr[1], title[2]:row_arr[2],
						title[3]:row_arr[3], title[4]:row_arr[4], title[5]:row_arr[5],
						title[6]:row_arr[6], title[7]:row_arr[7]
					 }
			obj_list.append(mydict)
		return obj_list


	def pushData(self,obj_list,index_name):

		es = elasticsearch.Elasticsearch(ES_URL)
		
		for mydict in obj_list:			

			es.index(
				index = index_name,
				doc_type = "Data",
				#id = 1,
				body = mydict
			)
		print("Data Sent Successfully")




##########################################################
#API: UI
#Return: 
#URL: http://localhost:8000/BDA/ES/BDA.html
##########################################################
def BDA(request):
	template = loader.get_template("BDA.html")
	return HttpResponse(template.render())