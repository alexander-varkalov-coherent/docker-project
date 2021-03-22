import requests
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse

from web1.forms import CommentForm

API_NAME = 'api1'
API_PORT = '5000'

LIST_URL = 'http://{}:{}/api/comments/'
DETAIL_URL = 'http://{}:{}/api/comments/{}/'


def all_comments(request):
    comments = requests.get(LIST_URL.format(API_NAME, API_PORT)).json()
    return render(request, 'comments.html', {'comments': comments})


def create_comment(request):
    if request.method == 'GET':
        return render(request, 'create_comment.html', {'form': CommentForm()})
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            response = requests.post(LIST_URL.format(API_NAME, API_PORT), data=cd)
            print(response.status_code)
            return redirect('comments')
        errors = form.errors
        return HttpResponse(f'errors in {errors}')


def edit_comment(request, pk):
    if request.method == 'GET':
        comment = requests.get(DETAIL_URL.format(API_NAME, API_PORT, pk)).json()
        return render(request, 'edit_comment.html', {'form': CommentForm(initial=comment)})
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            response = requests.put(DETAIL_URL.format(API_NAME, API_PORT, pk), data=cd)
            print(response.status_code)
            return redirect('comments')
        errors = form.errors
        return HttpResponse(f'errors in {errors}')


def delete_comment(request, pk):
    response = requests.delete(DETAIL_URL.format(API_NAME, API_PORT, pk))
    print(response.status_code)
    return redirect('comments')
