from django.shortcuts import render,render_to_response,HttpResponse,redirect
from app01 import models

import json
import datetime
from django.core import serializers
# Create your views here.
def login(request):
	if request.method == 'POST':
		user = request.POST.get('username')
		password = request.POST.get('password')
		print(user,password)
		try:
			currentobj = models.Admin.objects.get(user=user,password=password)
			print(currentobj)
		except Exception as e:
			currentobj=None
		if currentobj:
			request.session['current_user_id']=currentobj.id
			return redirect('/index/')
		else:
			return render_to_response('login.html')
	return render_to_response('login.html')
def index(request):
	data_all = models.News.objects.all()
	return render_to_response('index.html',{'data':data_all})

def add_favor(request):
	ret = {'statue':0,'data':'','massage':''}
	try:
		id = request.POST.get('nid')

		news_object = models.News.objects.get(id=id)

		temp=news_object.favor_count
		news_object.favor_count =temp+1
		print(news_object.favor_count)
		news_object.save()
		ret['statue']=1
		ret['data']=news_object.favor_count
	except Exception as e:
		ret['statue'] = 0
		ret['massage'] = e.__repr__()
	return HttpResponse(json.dumps(ret))
class CJsonEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o,datetime.datetime):
			return o.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(o,datetime.date):
			return o.strftime('%Y-%m-%d')
		else:return json.JSONEncoder.default(self,o)

def comment(request):
	id = request.POST.get('nid')
	reply_list=list(models.Reply.objects.filter(news__id=id).values('id','content','user__user','create_date'))
	reply_data = json.dumps(reply_list,cls=CJsonEncoder)
	return HttpResponse(reply_data)

def add_comment(request):
	ret = {'status' : 0,'e':''}
	nid = request.POST.get('nid')
	contents = request.POST.get('ncomments')
	obj = models.Reply.objects.create(content=contents,user=models.Admin.objects.get(id=request.session['current_user_id']),news=models.News.objects.get(id=nid))
	ret['status'] = 1
	return HttpResponse(json.dumps(str(ret['status'])))