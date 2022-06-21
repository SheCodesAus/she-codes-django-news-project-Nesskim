from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from users.models import CustomUser
from .forms import StoryForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date').all()[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class SearchResultsView(generic.ListView):
    model = NewsStory
    template_name = 'news/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        author_id= CustomUser.objects.get(username = query).id
        object_list = NewsStory.objects.filter(author = author_id)
        return object_list



class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)