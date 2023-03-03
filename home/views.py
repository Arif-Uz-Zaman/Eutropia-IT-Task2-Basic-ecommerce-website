from django.shortcuts import render
from django.http import JsonResponse
from itertools import zip_longest


from .models import TCloths,SCloths,WCloths,Laptop,Mobile,Computer,Jumkas,Kangans,Necklaces


# Create your views here.

def index(request):
    # return JsonResponse({'foo':'bar'})
    jumka=Jumkas.objects.all()
    kangan=Kangans.objects.all()
    Necklace=Necklaces.objects.all()
    computer= Computer.objects.all()
    laptop =Laptop.objects.all()
    mobile = Mobile.objects.all()
    tcloths =TCloths.objects.all()
    wcloths =WCloths.objects.all()
    scloths =SCloths.objects.all()
    zipped = zip_longest(tcloths, scloths,wcloths)
    electronics=zip_longest(laptop,mobile,computer)
    Jewellery =zip_longest(jumka,Necklace,kangan)

    context = {
        "zipped":zipped,
        "electronics":electronics,
        "Jewellery":Jewellery 

    }
    return render(request, 'index.html', context=context)

