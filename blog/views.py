from django.views.generic import ListView, TemplateView

from blog.models import Post


class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     context['posts'] = [
    #         {'title': 'The Big Thing',
    #          'content': 'This is a journey into sound!',
    #          'author': 'Stinky Wizzleteats',
    #          'date_posted': 'December 27, 2018'},
    #         {'title': 'Second Sighting!',
    #          'content': 'This is the second posting.',
    #          'author': 'Stinky Wizzleteats',
    #          'date_posted': 'December 28, 2018'}
    #     ]
    #     return context


class AboutView(TemplateView):
    template_name = 'blog/about.html'
