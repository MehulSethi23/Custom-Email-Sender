from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    print("YY")
    if request.method == "POST":
        print("XXX")
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        # contact = Contact(name=name, email=email,
        #                   desc=desc, date=datetime.today())
        # contact.save()
        send_mail(
            name,
            desc,
            email,
            ['swagsy2000@gmail.com'],
        )

        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')
