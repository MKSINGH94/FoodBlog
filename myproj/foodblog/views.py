from django.shortcuts import render,get_object_or_404
from .models import Post

def post_list(request):
	post=Post.objects.all()
	return render(request,
			 'foodblog/post/list.html',
			  {'posts':posts})

def post_detail(request,year,month,day,post):
	post=get_object_or_404(Post,slug=post,
	                status='published',
					publish_year=year,
					publish_month=month,
					publish_day=day)
        return render(request,
                    'foodblog/post/detail.html',
					{'post':post})


# Create your views here.
