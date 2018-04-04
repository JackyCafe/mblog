from _datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from mainsite.models import Post

# Create your views here.


# def homepage(request):
#     return HttpResponse('媽！我在這裡')


# def homepage(request):
#     posts = Post.objects.all()
#     post_list = list()
#     for count,post in enumerate(posts):
#         post_list.append("NO {}".format(str(count))+" ")
#         post_list.append(str(post.title +"<br>"))
#
#     return HttpResponse(post_list)


def homepage(request):
    temp = get_template('index.html');
    posts = Post.objects.all()
    current_time = datetime.now
    html = temp.render(locals())
    return HttpResponse(html)

def about(request,year,month,date):
    html = "現在時間 :{0}/ {1}/ {2} ".format(year,month,date)
    return HttpResponse(html)

def tv(request,tv_no='0'):
    tv_list = [{'name':'三數取大的','tvcode':'_PUTDIxpToM'},
               {'name': 'GPA', 'tvcode': 'S5WpALExjiw'},
               {'name': '閏年問題', 'tvcode': 'XtVJBP-QN-M'},
               {'name': '零錢解法', 'tvcode': 'rgu0-tvw8uI'},
               ]
    template = get_template('tv_index.html')
    now = datetime.now()
    tv = tv_list[int(tv_no)]
    html = template.render(locals())
    return HttpResponse(html)
