from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.db.models import Count
from .models import Example, Sense, Align, Sense2, Example_all, Sense_all, Sense_exp, Align_all, Sense_all2, Sense_wn, Align_wn,Sense_group
from datetime import datetime
import re, json, calendar

from nltk.corpus import wordnet

def add_exp(request):
	for line in open('gdex.one.txt'):
		expid, eng_sent, chi_sent = line.strip().split('\t')
		example = Example_all()
		if Example_all.objects.filter(exp_id=expid).exists() == False:
			example.exp_id = expid
			example.eng_sent = eng_sent
			example.chi_sent = chi_sent
			example.save()
			print(expid, eng_sent, chi_sent)

	return HttpResponse("Successfully add example sentences")

def add_sense(request):
	change_pos = {'v':'verb', 'n':'noun', 'j':'adjective', 'r':'adverb'}
	for line in open('bwn2.sense.defi.new.txt'):
		try:
			en, ch, pos, loc, num, sen = line.strip().split('||')
			sens = Sense_all2()
			sens.en_wd = en
			sens.ch_wd = ch
			sens.pos = change_pos[pos]
			sens.location = loc
			sens.number = num
			sens.sense = sen
			sens.save()
			print(en, ch, pos, loc, num, sen)
		except: continue
	return HttpResponse("Successfully add senses")
	# for line in open('wn.sense.defi.txt'):
	# 	loc, sen = line.strip().split('||')
	# 	sens = Sense_wn()
	# 	sens.location = loc
	# 	sens.sense = sen
	# 	sens.save()
	# 	print(loc, sen)		
	

def add_wnexp(request):
	for line in open('sense_group.noun.txt'):
		try:
			en, loc, wd = line.strip().split('\t')
			if Sense_group.objects.filter(en_wd=en, location=loc).exists() == False:
				sensgp = Sense_group()
				sensgp.en_wd = en
				sensgp.location = loc
				sensgp.ch_words = wd
				sensgp.save()
				print(en, loc, wd)
		except: continue	
	# change_pos = {'v':'verb', 'n':'noun', 'j':'adjective', 'r':'adverb'}
	# for line in open('wordnet_exp.txt'):
	# 	try:
	# 		en, ch, pos, loc, num, exp = line.strip().split('||')
	# 		sens = Sense_exp()
	# 		sens.en_wd = en
	# 		sens.ch_wd = ch
	# 		sens.pos = change_pos[pos]
	# 		sens.location = loc[1:]
	# 		sens.number = num
	# 		sens.example = exp
	# 		sens.save()
	# 		print(en, ch, pos, loc, num, exp)
	# 	except: continue

	return HttpResponse("Successfully add wordnet examples")

def add_align(request):
	for line in open('result.noun.one.txt'):
		print (line)
		try:
			en, ch, pos, loc, count, inv = line.strip().split('\t')
			# print (en, ch, pos)
			sen_id = Sense_all2.objects.filter(en_wd=en, pos=pos, location=loc).values_list("id", flat=True).distinct("id")[0]
			# print (123,sen_id)
			if Align_wn.objects.filter(en_wd=en, ch_wd=ch, pos=pos).exists() == False:
				align = Align_wn()
				align.en_wd = en
				align.ch_wd = ch
				align.pos = pos
				align.sense_id = sen_id
				align.location = loc
				align.count = count
				align.inv_index = inv
				align.save()
				print(en, ch, pos, loc, inv, count)
		except: continue
	return HttpResponse("Successfully add align")
	# for line in open('align2sense.gdex.txt'):
	# 	try:
	# 		en, ch_sense, loc, num, ch, pos, inv, count, sim, en_p, ch_p = line.strip().split('\t')
	# 		sen_id = Sense_all.objects.get(en_wd=en, ch_wd=ch_sense, pos=pos, location=loc, number=num).id
	# 		# if Align.objects.filter(en_wd=en, ch_wd=ch_sense, sense_id=sense_id, pos=pos).exists() == False:
	# 		align = Align_all()
	# 		align.en_wd = en
	# 		align.ch_wd = ch
	# 		align.pos = pos
	# 		align.sense_id = sen_id
	# 		align.inv_index = inv
	# 		align.count = count
	# 		align.similarity = sim
	# 		align.en_prob = en_p
	# 		align.ch_prob = ch_p
	# 		align.save()
	# 		print(en, ch_sense, loc, num, ch, inv, count, sim, en_p, ch_p)
			
	# 	except:
	# 		pass

	

def index(request):	
	if 'search' in request.POST:
		query = request.POST['search']
		language = 'en'
		print(query)
		if wordnet.synsets(query.split()[0]):
			language = 'en'
			align = Align_wn.objects.filter(en_wd=query).order_by('sense_id','-count')
			print("align",align)
			# align = Align.objects.filter(en_wd=query).extra({'count_uint': "Align(count as UNSIGNED)"}).order_by('-count_uint')
			get_sense = Align_wn.objects.filter(en_wd=query).order_by('sense_id','-count').values_list("sense_id", flat=True).distinct("sense_id")
			# sense = Sense_all.objects.filter(id__in=get_sense).order_by("location",'pos').distinct("location")
			sense = Sense_all2.objects.filter(en_wd=query).order_by("location",'pos').distinct("location")
			wn_exp = Sense_exp.objects.filter(en_wd=query).order_by("location",'pos').distinct("location")
			sense2 = Sense_all2.objects.filter(id__in=get_sense).order_by("location",'pos')
			get_location = Sense_all2.objects.filter(id__in=get_sense).order_by('pos').values_list("location", flat=True)
			print ('get_location',get_location)
			group = Sense_group.objects.filter(location__in=get_location).distinct("location")
			print ('group',group)
			sysnonym = Sense_all2.objects.filter(location__in=get_location).distinct("en_wd").exclude(en_wd=query)
			sysnonym_wd = Sense_all2.objects.filter(location__in=get_location).values_list("en_wd", flat=True).distinct("en_wd")

			pos = Sense_all2.objects.filter(id__in=get_sense).values('pos').annotate(Count('pos'))
			# align = align.order_by('count')

			get_exp = Align_wn.objects.filter(en_wd__in=sysnonym_wd).order_by('sense_id','-count').values_list("inv_index", flat=True)
			print(get_exp)
		else:
			language = 'ch'
			align = Align_wn.objects.filter(ch_wd=query).order_by('sense_id','en_wd','-count').distinct('sense_id',"en_wd")
			print(align)
			get_sense = Align_wn.objects.filter(ch_wd=query).order_by('sense_id','-count').values_list("sense_id", flat=True).distinct("sense_id")
			sense = Sense_all2.objects.filter(id__in=get_sense).order_by("location",'pos').distinct("location")
			wn_exp = Sense_exp.objects.filter(ch_wd=query).order_by("location",'pos').distinct("location")
			sense2 = Sense_all2.objects.filter(id__in=get_sense).order_by("location",'pos')
			# print (sense)
			get_location = Sense_all2.objects.filter(id__in=get_sense).order_by('pos').values_list("location", flat=True)
			sysnonym = Sense_all2.objects.filter(location__in=get_location).distinct("ch_wd").exclude(ch_wd=query)
			sysnonym_wd = Sense_all2.objects.filter(location__in=get_location).values_list("ch_wd", flat=True).distinct("ch_wd")	
			pos = Sense_all2.objects.filter(id__in=get_sense).values('pos').annotate(Count('pos'))
			group = {}
			get_exp = Align_wn.objects.filter(ch_wd__in=sysnonym_wd).order_by('sense_id','-count').values_list("inv_index", flat=True)
			# print(get_exp)
		exp = set()
		for i, ex in enumerate(get_exp):
			if ex != "none":
				a = ex.split(',')[0]
				exp.add(a)
		example = Example_all.objects.filter(exp_id__in=list(exp)).distinct("exp_id")
		return render(request, 'web/search.html', {'align':align, 'sense':sense, 'sense2':sense2, 'example':example,'pos':pos, 'query':query ,'sysnonym':sysnonym, 'language':language, 'wnexp': wn_exp, 'group':group})
	else:
		return render(request, 'web/search.html')		




