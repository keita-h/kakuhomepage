
from django.shortcuts import render, redirect
from .form import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
# Create your views here.


# お問い合わせフォーム画面


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = []
            sender.append(form.cleaned_data['sender'])
            myself = form.cleaned_data['myself']
            recipients = [settings.EMAIL_HOST_USER]

            if myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)

            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            # return render(request, 'kakupage/complete.html')
            return redirect('kakupage:complete')

    else:
        form = ContactForm()
    return render(request, 'kakupage/kakupage.html', {'form': form})


# 送信完了画面


def complete(request):
    return render(request, 'kakupage/complete.html')