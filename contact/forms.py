from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}), max_length=100)
    message = forms.CharField(label="Message",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your message'}), required=True, max_length=1000)