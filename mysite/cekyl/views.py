from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys 

# Create your views here.
def count(request, var_a, var_b):
	var_a = start
	var_b = step
	stop = 100
    count_list = []
	try:
    	while(start<stop):
        	count_list.append(start)
       	 	start = start + step
    return count_list
		return JsonResponse(count_list)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})