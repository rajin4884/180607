from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models
from PIL import Image
from sorl.thumbnail import ImageField, get_thumbnail
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.conf import settings

class Multa(models.Model):
	persona = models.ForeignKey( 'Persona' )

class Persona(models.Model):
    nom = models.CharField( max_length=200 )
    cognom = models.CharField( max_length=200 )

    def __str__(self):
        return self.nom + ' ' + self.cognom

class CraftPostManager(models.Manager):
	def active(self, *args, **kwargs):
		# CraftPost.objects.all() = super(CraftPostManager, self).all()
		return super(CraftPostManager, self)

class CraftPost(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=200)
	career = models.CharField(max_length=10, null = False, blank=False)
	money= models.PositiveIntegerField(null = False, blank=False)
	text = tinymce_models.HTMLField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	published_date = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(blank=True, null=True)
	link = models.URLField(max_length=200, blank=True, null=True)
	category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
	objects = CraftPostManager()


	def save(self):
        # Opening the uploaded image
		im = Image.open(self.photo)
		im = im.convert('RGB')
		output = BytesIO()

        # Resize/modify the image
        # im = im.resize((500, 500))

        # after modifications, save it to the output
		im.save(output, format='JPEG', quality=30)
		output.seek(0)

        # change the imagefield value to be the newley modifed image value
		self.photo = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		print(self.photo)
		super(CraftPost, self).save()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

	def unapproved_comments(self):
		return self.comments.filter(approved_comment=False)


class Comment(models.Model):
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, default="anon")
    craftpost = models.ForeignKey(CraftPost, related_name='comments')
    text = tinymce_models.HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Category(models.Model):
    order = models.PositiveIntegerField(help_text="Enter a number.")
    title = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    order = models.PositiveIntegerField(help_text="Enter a number.")
    title = models.CharField(null=True, max_length=100)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
