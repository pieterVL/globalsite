from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Create your views here.
def index(request):
	# return HttpResponse("<h2>Hey</h2>")
	if request.method == 'GET':
		return render(request, 'forum/index.html', {'topics':getTopics()})
	elif request.method == 'POST':
		subject = request.POST['subject']; 
		addTopic(subject)
		addPost(subject, request.POST['post'])
		return redirect('.')

def topic(request, topic_para):
	if request.method == 'GET':
		return render(request, 'forum/topic.html', {'topic':topic_para, 'posts':getPosts(topic_para)})
	elif request.method == 'POST':
		addPost(topic_para,request.POST['post'])
		return redirect(request.get_full_path())

def topic_delete(request, topic_para):	
	if request.method == 'POST':
		deleteTopic(topic_para)
		return redirect('./..')

def topic_post_delete(request, topic_para):
	if request.method == 'POST':
		deleletePost(topic_para, request.POST['key'])
		return redirect('./../'+topic_para)



def addTopic(subject):
	r.lpush('subjects',subject)
def addPost(subject, post):
	r.rpush('subjects:'+subject, post)
def getTopics():
	return r.lrange('subjects',0,-1)
def getPosts(subject):
	return r.lrange('subjects:'+subject,0,-1)
def deleteTopic(subject):
	r.lrem('subjects',0,subject)
	r.delete('subjects:'+subject)
def deleletePost(subject,key):
	r.lrem('subjects:'+subject,0,key)