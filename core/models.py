from django.db import models
from django.urls import reverse

class Subject(models.Model):
	name=models.CharField(max_length=50)
	description=models.CharField(max_length=500,null=True,blank=True)
	def __str__(self):
		return self.name

class Author(models.Model):
	name=models.CharField(max_length=50)
	about=models.CharField(max_length=500,null=True,blank=True)
	def __str__(self):
		return self.name


class Book(models.Model):
	name=models.CharField(max_length=50)
	description=models.CharField(max_length=500)
	subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='book_sub')
	author=models.ForeignKey(Author,on_delete=models.CASCADE,default=None,related_name='book_author')
	file=models.FileField(upload_to='files')
	def __str__(self):
		return self.name

class Tutor(models.Model):
	name=models.CharField(max_length=50)
	about=models.CharField(max_length=500,null=True,blank=True)
	profile_pic=models.ImageField(upload_to='images')
	def __str__(self):
		return self.name


class Doubt(models.Model):
	name=models.CharField(max_length=50,null=True,blank=True)
	email=models.EmailField(max_length=50)
	doubt=models.CharField(max_length=500)
	image=models.ImageField(upload_to='doubt',null=True,blank=True)
	def __str__(self):
		return self.name


class Class(models.Model):
	name=models.IntegerField()
	subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='class_sub')

	def __str__(self):
		return str(self.name)

class Chapter(models.Model):
	name=models.IntegerField()
	subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='chapter')
	classes=models.ForeignKey(Class,on_delete=models.CASCADE,related_name='chapter')
	description=models.TextField()

	def __str__(self):
		return f"{self.subject.name} Class {self.classes.name} chapter {str(self.name)} "
	def get_absolute_url(self):
		return reverse('chapter_view',kwargs={'pk':self.pk})

class Quiz(models.Model):
	name=models.CharField(max_length=50)
	content=models.CharField(max_length=200)
	listing=models.BooleanField(default=False)
	

	def __str__(self):
		return self.name

class Answer(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	reply=models.CharField(max_length=300)
	def __str__(self):
		return f"replied by {self.email}"