from django import forms
from .models import Articles, Tag

class ContactForm(forms.Form):
    name=forms.CharField(label='название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='сообщение')

class PostForm(forms.ModelForm):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control'}))

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model=Articles
        fields = ['published', 'name', 'url', 'image', 'category']
        #exclude=('user',)