from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def blog_number(request, id):
    return HttpResponse(f"placeholder to display blog number {id}")
def blog_number_edit(request, id):
    return HttpResponse(f"placeholder to display blog number {id} with a method 'edit'")
def destroy(request, id):
    return redirect("/")