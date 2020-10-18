from django import forms
from blog.models import Comment

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '') # remove the colon from form labels
        super(ContactForm, self).__init__(*args, **kwargs)
    name = forms.CharField(
        label='Name',
        max_length=100,
        required=True)
    email = forms.EmailField(
        label='Email',
        required=True)
    subject = forms.CharField(
        label='Subject',
        max_length=100,
        required=False)
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(),
        required=True)
    cc = forms.BooleanField(
        label='Send me a copy of the message?',
        required=False,
        initial=True)

    required_css_class = 'required'


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '') # remove the colon from form labels
        super(CommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    required_css_class = 'required'