from django.db import models

class CraftPostManager(models.Manager):
	def active(self, *args, **kwargs):
		# CraftPost.objects.all() = super(CraftPostManager, self).all()
		return super(CraftPostManager, self)

class DjangoBoard(models.Model):
	id = models.IntegerField(primary_key=True)
	subject = models.CharField(max_length=50, blank=True)
	name = models.CharField(max_length=50, blank=True)
	created_date = models.DateField(null=True, blank=True)
	mail = models.CharField(max_length=50, blank=True)
	memo = models.CharField(max_length=200, blank=True)
	hits = models.IntegerField(null=True, blank=True)
	objects = CraftPostManager()
