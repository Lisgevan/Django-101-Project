#for function based views
#==>from django.shortcuts import render

#for class based views
from django.views.generic import TemplateView

from.models import Post

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
