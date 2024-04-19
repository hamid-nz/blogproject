from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import(
    View,
    TemplateView,
    CreateView, 
    ListView,
    UpdateView,
    DeleteView,
    DetailView
    )

# Create your views here.


class HomeView(TemplateView):
    template_name = 'blogapp/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_post= BlogPost.objects.all()
        all_category= Category.objects.all()
        context["all_post"]= all_post
        context["all_category"]= all_category
        return context
        

class SinglePostView(TemplateView):
    template_name = 'blogapp/single_post.html'
    context_object_name = 'single_post'

    def get(self, request, post_url):
        single_post = get_object_or_404(BlogPost, post_url= post_url)
        return render(request, self.template_name, {'single_post': single_post})


# class SingleCategoryView(TemplateView):
#     template_name = 'blogapp/single_category.html'
#     context_object_name = 'single_category'

#     def get(self, request, category_url):
#         single_category = get_object_or_404(Category, category_url= category_url)
#         return render(request, self.template_name, {'single_category': single_category})


def get_blog_by_category(request, category_url):
    cats= Category.objects.get(category_url= category_url)
    blogs= BlogPost.objects.filter(category= cats)
    context= { 'blogs': blogs }
    return render(request, 'blogapp/single_category.html', context )

    
# user authentication Login and register
@login_required(login_url='sign-in')
def Account(request):
    return render(request,'blogapp/account.html' )  

def sign_in(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        pass1= request.POST.get('pass1')
        user= authenticate(request, username= username, password= pass1)
        if user is not None:
            login(request, user)
            return redirect(Account)
        else:
            return HttpResponse(" <h3>Username or Password is incorrect! Try again</h3>")
    
    return render (request, 'blogapp/sign-in.html')

def sign_up(request):
    if request.method == 'POST':
        name= request.POST.get('Name')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('pass1')
        pass2= request.POST.get('pass2')
        if password!= pass2:
            return HttpResponse("Your password does'nt match")
        else:       
         new_user = User.objects.create_user(username, email,  password )
         new_user.save()     
         return redirect('sign-in')
    
    return render (request, 'blogapp/sign-up.html')
    
def sign_out(request):
     logout(request)
     return redirect('sign-in')
