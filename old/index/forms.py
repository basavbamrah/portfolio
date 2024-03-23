from django import forms

# contact form

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='name')
    email = forms.EmailField(label='email')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, label='message')

# comment form

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

