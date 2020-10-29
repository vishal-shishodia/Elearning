from django.shortcuts import render,redirect

from .models import *
from .forms import *

def index(request):
	sub=Subject.objects.all()
	author=Author.objects.all()
	tutor=Tutor.objects.all()[:4]
	quiz=Quiz.objects.filter(listing=True)
	context={'sub':sub,'author':author,'tutor':tutor,'quiz':quiz}
	return render(request,'index.html',context)

def SubjectView(request,pk):
	sub=Subject.objects.get(pk=pk)
	classes=Class.objects.filter(subject=sub)
	context={'classes':classes}
	return render(request,'sub_home.html',context)

def ChapterView(request,pk):
	chapter=Chapter.objects.filter(pk=pk)
	context={'chapter':chapter}
	return render(request,'chapter_home.html',context)

def AuthorView(request,pk):
	author=Author.objects.get(pk=pk)
	books=Book.objects.filter(author=author)
	context={'books':books}
	return render(request,'author_home.html',context)

def Doubt(request):
	if request.POST:
		form=DoubtForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form=DoubtForm()
	return render(request,'doubt.html',{'form':form})

def AnswerView(request):
	if request.POST:
		form=AnswerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form=AnswerForm()
	context={'form':form}
	return render(request,'answer.html',context)

