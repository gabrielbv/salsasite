from django.http import HttpResponse
from django.shortcuts import render
from news.forms import NewsForm
from news.models import News

# Create your views here.

def add(request):

	
	form = NewsForm()

	if request.method == "POST":

		form = NewsForm(request.POST)
		
		if form.is_valid():

			user = request.user
			
			news = form.save(commit=False)
			
			news.user=user

			news.save()


			return HttpResponse("thanks")



	return render(request, 'news/add.html', {'form':form})



def list(request):

	news = News.objects.all()


	return render(request, 'news/list.html', {'news':news})