from django.db import models

class Example(models.Model):
	exp_id = models.TextField()
	eng_sent = models.TextField()
	chi_sent = models.TextField() 

	def __str__(self):
		return '%s,%s,%s' %(self.exp_id, self.eng_sent, self.chi_sent)

class Example_all(models.Model):
	exp_id = models.TextField()
	eng_sent = models.TextField()
	chi_sent = models.TextField() 

	def __str__(self):
		return '%s,%s,%s' %(self.exp_id, self.eng_sent, self.chi_sent)

class Sense(models.Model):
	en_wd = models.TextField()
	ch_wd = models.TextField()
	pos = models.TextField()
	location = models.TextField()
	number = models.TextField()

	def __str__(self):
		return '%s,%s,%s,%s,%s,%s' %(self.id, self.en_wd, self.ch_wd, self.pos, self.location, self.number)

class Sense2(models.Model):
	en_wd = models.TextField()
	ch_wd = models.TextField()
	pos = models.TextField()
	location = models.TextField()
	number = models.TextField()
	sense = models.TextField()

	def __str__(self):
		return '%s,%s,%s,%s,%s,%s,%s' %(self.id, self.en_wd, self.ch_wd, self.pos, self.location, self.number, self.sense)

class Sense_all(models.Model):
	en_wd = models.TextField()
	ch_wd = models.TextField()
	pos = models.TextField()
	location = models.TextField()
	number = models.TextField()
	sense = models.TextField()

	def __str__(self):
		return '%s,%s,%s,%s,%s,%s,%s' %(self.id, self.en_wd, self.ch_wd, self.pos, self.location, self.number, self.sense)

class Sense_all2(models.Model):
	en_wd = models.TextField()
	ch_wd = models.TextField()
	pos = models.TextField()
	location = models.TextField()
	number = models.TextField()
	sense = models.TextField()

	def __str__(self):
		return '%s,%s,%s,%s,%s,%s,%s' %(self.id, self.en_wd, self.ch_wd, self.pos, self.location, self.number, self.sense)

class Sense_wn(models.Model):
	location = models.TextField()
	sense = models.TextField()

	def __str__(self):
		return '%s,%s' %(self.location, self.sense)

class Sense_exp(models.Model):
	en_wd = models.TextField()
	ch_wd = models.TextField()
	pos = models.TextField()
	location = models.TextField()
	number = models.TextField()
	example = models.TextField()

	def __str__(self):
		return '%s,%s,%s,%s,%s,%s,%s' %(self.id, self.en_wd, self.ch_wd, self.pos, self.location, self.number, self.example)

class Align(models.Model):
	en_wd = models.TextField()
	ch_wd = models.TextField()
	pos = models.TextField()
	sense_id = models.IntegerField()
	inv_index = models.TextField()
	count = models.IntegerField()
	similarity = models.TextField()

	def __str__(self):
		return '%s,%s,%s,%s,%s,%s' %(self.en_wd, self.sense_id, self.ch_wd, \
			self.inv_index, self.count, self.similarity)

class Align_new(models.Model):
	en_wd = models.TextField()
	ch_wd = models.TextField()
	pos = models.TextField()
	sense_id = models.IntegerField()
	inv_index = models.TextField()
	count = models.IntegerField()
	similarity = models.TextField()

	def __str__(self):
		return '%s,%s,%s,%s,%s,%s' %(self.en_wd, self.sense_id, self.ch_wd, \
			self.inv_index, self.count, self.similarity)


class Align_all(models.Model):
	en_wd = models.TextField()
	ch_wd = models.TextField()
	pos = models.TextField()
	sense_id = models.IntegerField()
	inv_index = models.TextField()
	count = models.IntegerField()
	similarity = models.FloatField()
	en_prob = models.FloatField()
	ch_prob = models.FloatField()

	def __str__(self):
		return '%s,%s,%s,%s,%s,%s,%s,%s' %(self.en_wd, self.sense_id, self.ch_wd, \
			self.inv_index, self.count, self.similarity, self.en_prob, self.ch_prob)

class Align_wn(models.Model):
	en_wd = models.TextField()
	ch_wd = models.TextField()
	pos = models.TextField()
	sense_id = models.IntegerField()
	location = models.TextField()
	count = models.IntegerField()
	inv_index = models.TextField()
	

	def __str__(self):
		return '%s,%s,%s,%s,%s,%s,%s' %(self.en_wd, self.ch_wd, self.pos,\
			self.location, self.sense_id, self.inv_index, self.count)			

class Sense_group(models.Model):
	en_wd = models.TextField()
	location = models.TextField()
	ch_words = models.TextField()
	

	def __str__(self):
		return '%s,%s,%s' %(self.en_wd, self.location, self.ch_words)