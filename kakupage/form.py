from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    sender = forms.EmailField(label='Email', help_text='※ご確認の上、正しく入力してください。')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    # myself = forms.BooleanField(label='同じ内容を受け取る', required=False)
