
from django.shortcuts import render
from search.models import music, movie, hobbies, health, spend, userfeature
from account.models import User, Profile
from django.core.paginator import Paginator
# Create your views here.


def searchresult(request):

#	profile_list = profile.objects.all()

	gender = request.GET.get('gender','')
	if gender != 'both':
		profile_list = Profile.objects.filter(gender = gender)
	else:
		profile_list = Profile.objects.all()

	onlychild = request.GET.get('onlychild','')
	if onlychild == 'false':
		profile_list = profile_list.filter(only_child = False)
	if onlychild == 'true':
		profile_list = profile_list.filter(only_child = True)

	af = request.GET.get('age_from','')
	at = request.GET.get('age_to','')
	if af != '':
		profile_list = profile_list.filter(age__gte = af)
	if at != '':
		profile_list = profile_list.filter(age__lte = at)

	wf = request.GET.get('weight_from','')
	wt = request.GET.get('weight_to','')
	if wf != '':
		profile_list = profile_list.filter(weight__gte = wf)
	if wt != '':
		profile_list = profile_list.filter(weight__lte = wt)

	hf = request.GET.get('height_from','')
	ht = request.GET.get('height_to','')
	if hf != '':
		profile_list = profile_list.filter(height__gte = hf)
	if ht != '':
		profile_list = profile_list.filter(height__lte = ht)

	eduf = request.GET.get('eduf','')
	edut = request.GET.get('edut','')
	if eduf != '':
		profile_list = profile_list.filter(education__gte = eduf)
	if edut != '':
		profile_list = profile_list.filter(education__lte = edut)

	location = request.GET.get('location','')
	locationlist = request.GET.get('locationlist','')
	if locationlist != '':
		locationlist = locationlist.split(',')
		profile_list = profile_list.filter(location__in = locationlist)
	else:
		if location != '0':
			profile_list = profile_list.filter(location__exact = location)


	def getuid (userid,list):
		for p in list:
			userid.append(p.user.id)
		return userid

	userid = []
	userid = getuid(userid,profile_list)

	user_list = User.objects.filter(id__in = userid)

	health_list = health.objects.filter(user__in = userid)
	spend_list = spend.objects.filter(user__in = userid)
	ufeature_list = userfeature.objects.filter(user__in = userid)

#category search
	# Love music
	lmusic_checked = request.GET.getlist('lmusic')
	#check if all-choosed
	lmusic_need_length = len(lmusic_checked)

	lmusic_need_check = (lmusic_need_length>0) and (lmusic_need_length < music.objects.count())

	lmusic_ids=[]
	for m in lmusic_checked:
		try:
			lmusic_ids.append(int(m))
		except:
			pass

	if lmusic_need_check:
		ufeature_list = ufeature_list.filter(musicloved__in = lmusic_ids)
		ufeature_list = ufeature_list.distinct()

	# Hate music
	hmusic_checked = request.GET.getlist('hmusic')
	#check if all-choosed
	hmusic_need_length = len(hmusic_checked)

	hmusic_need_check = (hmusic_need_length>0) and (hmusic_need_length < music.objects.count())

	hmusic_ids=[]
	for m in hmusic_checked:
		try:
			hmusic_ids.append(int(m))
		except:
			pass

	if hmusic_need_check:
		ufeature_list = ufeature_list.filter(musichated__in = hmusic_ids)
		ufeature_list = ufeature_list.distinct()

	# Love movie
	lmovie_checked = request.GET.getlist('lmovie')
	#check if all-choosed
	lmovie_need_length = len(lmovie_checked)

	lmovie_need_check = (lmovie_need_length>0) and (lmovie_need_length < movie.objects.count())

	lmovie_ids=[]
	for m in lmovie_checked:
		try:
			lmovie_ids.append(int(m))
		except:
			pass

	if lmovie_need_check:
		ufeature_list = ufeature_list.filter(movieloved__in = lmovie_ids)
		ufeature_list = ufeature_list.distinct()

	# Hate movie
	hmovie_checked = request.GET.getlist('hmovie')
	#check if all-choosed
	hmovie_need_length = len(hmovie_checked)

	hmovie_need_check = (hmovie_need_length>0) and (hmovie_need_length < movie.objects.count())

	hmovie_ids=[]
	for m in hmovie_checked:
		try:
			hmovie_ids.append(int(m))
		except:
			pass

	if hmovie_need_check:
		ufeature_list = ufeature_list.filter(moviehated__in = hmovie_ids)
		ufeature_list = ufeature_list.distinct()

	#hobbies
	hobby_checked = request.GET.getlist('hobby')
	#check if all-choosed
	hobby_need_length = len(hobby_checked)

	hobby_need_check = (hobby_need_length>0) and (hobby_need_length < hobbies.objects.count())

	hobby_ids=[]
	for m in hobby_checked:
		try:
			hobby_ids.append(int(m))
		except:
			pass

	if hobby_need_check:
		ufeature_list = ufeature_list.filter(hobbies__in = hobby_ids)
		ufeature_list = ufeature_list.distinct()

#update userlist
	userid = []
	for p in ufeature_list:
		userid.append(p.user.id)
	userid = getuid (userid,ufeature_list)

	user_list = User.objects.filter(id__in = userid)
	profile_list = Profile.objects.filter(user__in = userid)
	# user_list = Paginator(user_list, 20)

#return data
	data = {}
	data["music"] = music.objects.all()
	data["movie"] = movie.objects.all()
	data["hobbies"] = hobbies.objects.all()
	data['profile_list'] = profile_list
	# data['page'] = user_list

	return render(request, 'search/searchresult.html', data)

def search(request):
	data = {}
	data["music"] = music.objects.all()
	data["movie"] = movie.objects.all()
	data["hobbies"] = hobbies.objects.all()
	return render(request, 'search/search.html', data)


