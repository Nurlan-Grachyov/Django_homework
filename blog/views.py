from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, DetailView, UpdateView, DeleteView

from blog.forms import ContactForm
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = "articles"


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = [
        "name",
        "description",
        "image",
        "is_created",
        "viewing"
    ]
    success_url = reverse_lazy("blog:home")


class ContactsFormView(FormView):
    template_name = 'blog_contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'article'
    success_url = reverse_lazy("blog:del_article")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = [
        "name",
        "description",
        "image",
        "is_created",
        "viewing"
    ]
    template_name = 'blog_create.html'


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy("blog:home")
