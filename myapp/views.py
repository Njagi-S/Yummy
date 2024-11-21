from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import BookTable, ContactTable
from myapp.forms import BookTableForm, ContactTableForm

# Render the homepage
def index(request):
    return render(request, 'index.html')

# Render the starter page
def starter(request):
    return render(request, 'starter-page.html')

# Render the about page
def about(request):
    return render(request, 'about.html')

# Render the chefs page
def chefs(request):
    return render(request, 'chefs.html')

# Render the events page
def events(request):
    return render(request, 'events.html')

# Render the menu page
def menu(request):
    return render(request, 'menu.html')

# Render the gallery page
def gallery(request):
    return render(request, 'gallery.html')

# Handle table booking form submission
def booking(request):
    if request.method == 'POST':  # If the form is submitted
        mybooking = BookTable(
            name=request.POST['name'],         # Retrieve 'name' field
            email=request.POST['email'],       # Retrieve 'email' field
            phone=request.POST['phone'],       # Retrieve 'phone' field
            date=request.POST['date'],         # Retrieve 'date' field
            time=request.POST['time'],         # Retrieve 'time' field
            guests=request.POST['guests'],     # Retrieve 'guests' field
            message=request.POST['message'],   # Retrieve 'message' field
        )
        mybooking.save()  # Save the booking to the database
        return redirect('/showbookings')  # Redirect to the bookings list
    else:
        return render(request, 'booking.html')  # Render the booking form

# Display all bookings
def showbookings(request):
    allbookings = BookTable.objects.all()  # Retrieve all bookings
    return render(request, 'showbookings.html', {'bookings': allbookings})  # Pass bookings to the template

# Handle contact form submission
def contact(request):
    if request.method == 'POST':  # If the form is submitted
        mycontact = ContactTable(
            name=request.POST['name'],       # Retrieve 'name' field
            email=request.POST['email'],     # Retrieve 'email' field
            subject=request.POST['subject'], # Retrieve 'subject' field
            message=request.POST['message'], # Retrieve 'message' field
        )
        mycontact.save()  # Save the contact message to the database
        return redirect('/showcontacts')  # Redirect to the contacts list
    else:
        return render(request, 'contact.html')  # Render the contact form

# Display all contact messages
def showcontacts(request):
    allcontacts = ContactTable.objects.all()  # Retrieve all contact messages
    return render(request, 'showcontacts.html', {'mycontacts': allcontacts})  # Pass messages to the template

# Delete a specific booking
def deletebookings(request, id):
    book = BookTable.objects.get(id=id)  # Get the booking by ID
    book.delete()  # Delete the booking
    return redirect('/showbookings')  # Redirect to the bookings list

# Delete a specific contact message
def deletecontacts(request, id):
    mycon = ContactTable.objects.get(id=id)  # Get the contact message by ID
    mycon.delete()  # Delete the contact message
    return redirect('/showcontacts')  # Redirect to the contacts list

# Render the booking editing form
def editbookings(request, id):
    editbooking = BookTable.objects.get(id=id)  # Get the booking by ID
    return render(request, 'editbookings.html', {'bookings': editbooking})  # Pass the booking to the template

# Render the contact editing form
def editcontacts(request, id):
    editcontact = ContactTable.objects.get(id=id)  # Get the contact message by ID
    return render(request, 'editcontacts.html', {'contacts': editcontact})  # Pass the message to the template

# Update a specific booking
def updatebookings(request, id):
    updatebookinginfo = BookTable.objects.get(id=id)  # Get the booking by ID
    form = BookTableForm(request.POST, instance=updatebookinginfo)  # Bind form data to the existing instance
    if form.is_valid():  # Check if the form is valid
        form.save()  # Save the updated booking
        return redirect('/showbookings')  # Redirect to the bookings list
    else:
        return render(request, 'editbookings.html')  # Re-render the editing form if invalid

# Update a specific contact message
def updatecontacts(request, id):
    updatecontactinfo = ContactTable.objects.get(id=id)  # Get the contact message by ID
    form = ContactTableForm(request.POST, instance=updatecontactinfo)  # Bind form data to the existing instance
    if form.is_valid():  # Check if the form is valid
        form.save()  # Save the updated contact message
        return redirect('/showcontacts')  # Redirect to the contacts list
    else:
        return render(request, 'editcontacts.html')  # Re-render the editing form if invalid