from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from pymongo import MongoClient

client = MongoClient()
# db = client['primer']
# coll = db['dataset']
db = client['Recepten']

# Create your views here.
def index(request):
	if request.method == 'GET':
		cursor = getAll()
		cursor.sort('calorien')
		cursor.sort('naam')
		return render(request, 'forum/index.html', {'recepten':cursor})
	elif request.method == 'POST':
		obj = {
				'naam':	request.POST['naam'],
				'calorien':	request.POST['calorien'],
				'ingredienten':	request.POST['ingredienten'],
				'tijd':	request.POST['tijd'],
			}
		if not exists(obj):
			insert(obj)

		return redirect("./")

def getAll():
	return db['res'].find()

def exists(obj):
	cursor = getAll()
	for r in cursor:
		if r['naam'] == obj['naam'] and r['calorien'] == obj['calorien'] and r['ingredienten'] == obj['ingredienten'] and r['tijd'] == obj['tijd']:
			return True
	return False

def insert(obj):
	# result = db['test'].insert_one({'key':'value'})
	result = db['res'].insert_one(obj)
	return result
