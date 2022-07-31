from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Articles
from .forms import ContactForm
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.
def main_view(request):
    posts = Articles.objects.all()
    return render (request, 'hhapp/index.html', context={'posts': posts})

def create_post(request):
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
            return render(request, 'hhapp/create.html', context={'form': form})
    else:
        form=ContactForm()
        return render(request, 'hhapp/create.html', context={'form': form})


def post(request, id):
    post=get_object_or_404(Articles, id=id)
    return render(request, 'hhapp/post.html', context={'post': post})
