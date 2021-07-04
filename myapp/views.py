from django.shortcuts import render
from myproject.celery import debug_task
from django.http import HttpResponseServerError, HttpResponse,JsonResponse
from celery.result import AsyncResult
import time
def view_data(request):
	# get data by catagory
	url='__enterurlhere__'
	url=str(url)
	data=debug_task.delay(url,kwargs['catagory'],kwargs['value'])
	if data.status =='SUCCESS':
		data2=AsyncResult(data.id)
		print(data2.get())
		return JsonResponse(data2.get())
	else:
		time.sleep(2)
		data2=AsyncResult(data.id)
		return JsonResponse(data2.get())
	return HttpResponseServerError('something went wrong')
