from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Articles, Tag
from .forms import ContactForm, PostForm
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class main_view(ListView):
    posts=Articles.active_objects.all()
    model=Articles
    paginate_by = 2
    template_name='hhapp/index.html'

def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail(
                'Contact message',
                message,
                'from@example.com',
                ['serg190496@mail.ru'],
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('hh:index'))
        else:
            return render(request, 'hhapp/contact.html', context={'form': form})
    else:
        form=ContactForm()
        return render(request, 'hhapp/contact.html', context={'form': form})


class post(UserPassesTestMixin,DetailView):
    model=Articles
    template_name = 'hhapp/post.html'
    raise_exception = False
    def test_func(self):
        return self.request.user.is_superuser


class create_post(LoginRequiredMixin,CreateView):
    fields = ['published', 'name', 'url', 'image',]
    # exclude = ('user',)
    model=Articles
    success_url = reverse_lazy('hh:index')
    template_name = 'hhapp/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NameContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        context['name']='Теги'
        return context

class TagListView(ListView, NameContextMixin):
    model=Tag
    template_name='hhapp/tag_list.html'
    context_object_name = 'tags'

    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        context['name']='Теги'
        return context

    def get_queryset(self):

        return Tag.active_objects.all()

class TagDetailView(DetailView):
    model=Tag
    template_name = 'hhapp/tag_detail.html'

    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        context['name']='Теги'
        return context

class TagCreateView(LoginRequiredMixin,CreateView):
    fields='__all__'
    model=Tag
    success_url = reverse_lazy('hh:tag_list')
    template_name = 'hhapp/tag_create.html'

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)

class TagUpdateView(UpdateView):
    fields='__all__'
    model=Tag
    success_url = reverse_lazy('hh:tag_list')
    template_name = 'hhapp/tag_create.html'

class TagDeleteView(DeleteView):
    template_name = 'hhapp/tag_delete_confirm.html'
    model=Tag
    success_url = reverse_lazy('hh:tag_list')