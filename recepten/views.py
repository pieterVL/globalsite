from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from pymongo import MongoClient

client = MongoClient()
# db = client['primer']
# coll = db['dataset']
db = client['Recepten']
coll = db['test']
# Create your views here.
def index(request):
	vari =  insert(0)
	print vari
	print vari.inserted_id
	return HttpResponse("<h2>Hey</h2>")

	# if request.method == 'GET':
	# 	return render(request, 'forum/index.html', {'topics':getTopics()})
	# elif request.method == 'POST':
	# 	subject = request.POST['subject']; 
	# 	addTopic(subject)
	# 	addPost(subject, request.POST['post'])
	# 	return redirect('.')

def insert(obj):
	result = db['test'].insert_one({'key':'value'})
	return result
