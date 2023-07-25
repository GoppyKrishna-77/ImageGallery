from django.views.generic import TemplateView, DetailView, FormView
from django.contrib import messages
from django.shortcuts import render

from .models import Post
from .forms import PostForm

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by("-id")
        return context
    
class DetailPageView(DetailView):

    template_name = "detail.html"
    model = Post
    
class PostView(FormView):
    template_name = "post.html"
    form_class = PostForm
    success_url = "/"
    
    def dispatch(self, request, *args, **kwargs):

        self.request = request

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        
        new_obj = Post.objects.create(
            text=form.cleaned_data["text"],
            image=form.cleaned_data["image"],
        )

        messages.add_message(self.request, messages.SUCCESS, "You have a New Message!")
    
        return super().form_valid(form)

def delete_post(request):
    print(request)
    print("you clicked delete")
    return render(request, "home.html")