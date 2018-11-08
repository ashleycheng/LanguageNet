from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='split')
def split(value):
    return value.split(',')

@register.filter(name='split2')
def split2(value):
	value = eval(value)
	return '; '.join(value[:13])+'...'

@register.filter(name='get_sysnonym')
def get_sysnonym(sys, query):
	if "_" in sys:
		res = sys.replace("_", " ")
		# if query in res:
		# 	return ""
		# else:
		return res
	else:
		return sys

@register.filter(name='highlight')
def highlight(text, word):
	return mark_safe(text.replace(word, "<span class='highlight' style='color:#cc2900'>%s</span>" % word))

@register.filter(name='location')
def get_location(data, loc):
	sysnonyms = data.values_list("location", flat=True)
	if loc in list(sysnonyms):
		return 123
	return 0

@register.filter(name='get_example')
def get_exp(data, wd):
	print (data,wd)
	if wd in data:
		return 123
	return 0	
