from django.shortcuts import render,redirect
from .models import Photo
from twilio.rest import Client

# Create your views here.
def index(request):
    if request.method == 'POST':
        new_photo = Photo(
            file = request.FILES['img']
        )
        new_photo.save()
        new_url=str('https://xeroxfin.herokuapp.com'+new_photo.file.url)
        sid='ACc536c7fac505fff2f410b3d6d31f876f'
        authToken='0cb21332809498875ab1ebb2e99cb7f7'

        client=Client(sid,authToken)

        from_whatsapp_number='whatsapp:+14155238886'
        to_whatsapp_number='whatsapp:+919774141994'

        message=client.messages.create(body=new_url,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
        return redirect("https://arghajit08.github.io/lastpage/")
    else:
        return render(request, 'index.html')
