from django.shortcuts import render, redirect
from myapp.models import BookTable

# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def chefs(request):
    return render(request, 'chefs.html')

def contact(request):
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')

def menu(request):
    return render(request, 'menu.html')

def gallery(request):
    return render(request, 'gallery.html')

def booking(request):
    if request.method == 'POST':
        mybooking = BookTable(
            name = request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            time=request.POST['time'],
            guests=request.POST['guests'],
            message=request.POST['message'],
            )
        mybooking.save()
        return redirect('/showbookings')
    else:
        return render(request, 'booking.html')

def showbookings(request):
    allbookings = BookTable.objects.all()
    return render(request, 'showbookings.html', {'bookings': allbookings})