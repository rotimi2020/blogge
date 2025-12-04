from django.shortcuts import render
from django.views.generic import (TemplateView,CreateView,ListView,DetailView)
from .forms import ContactForm
from .models import Contact,Blog_Post
from django.urls import reverse_lazy
from django.contrib import messages




class HomeView(ListView):
    model = Blog_Post
    template_name = "BloggeApp/index.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 5
    def get_queryset(self):
        # Only non-featured posts will show in the main list
        return Blog_Post.objects.filter(is_top_post=False).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["top_post"] = Blog_Post.objects.filter(is_top_post=True).first()
        context["trending"] = Blog_Post.objects.filter(is_trending=True)[:5]
        return context





class AboutView(TemplateView):
    #model = ContactForm
    #form_class = ContactForm
    template_name = "BloggeApp/about.html"
    #success_url = reverse_lazy("about")



class ContactView(CreateView):
    #model = ContactForm
    form_class = ContactForm
    template_name = "BloggeApp/contact.html"
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        # save the object (creates Contact instance)
        response = super().form_valid(form)
        # add the flash message
        messages.success(self.request, "Message sent — thank you!")
        return response


class CategoryView(ListView):
    model = Blog_Post
    template_name = "BloggeApp/category.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        category = self.kwargs['category']   
        return Blog_Post.objects.filter(category=category)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']    
        return context


class SingleBlogView(DetailView):
    model = Blog_Post
    #form_class = ContactForm
    template_name = "BloggeApp/single-blog.html"
    context_object_name = "post"
    success_url = reverse_lazy("single_blog")

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            post = self.object

            # EXCLUDE TOP POSTS
            context["previous_post"] = Blog_Post.objects.filter(
                is_top_post=False,
                created_at__lt=post.created_at
            ).order_by("-created_at").first()

            context["next_post"] = Blog_Post.objects.filter(
                is_top_post=False,
                created_at__gt=post.created_at
            ).order_by("created_at").first()

            return context