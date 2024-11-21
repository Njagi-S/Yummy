from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # Admin interface route
    path('admin/', admin.site.urls),  
    
    # Homepage route
    path('', views.index, name='index'),  
    
    # Static pages
    path('starter/', views.starter, name='starter'),  # Starter page
    path('about/', views.about, name='about'),        # About page
    path('chefs/', views.chefs, name='chefs'),        # Chefs page
    path('events/', views.events, name='events'),     # Events page
    path('menu/', views.menu, name='menu'),           # Menu page
    path('gallery/', views.gallery, name='gallery'),  # Gallery page
    
    # Contact-related routes
    path('contact/', views.contact, name='contact'),              # Contact form
    path('showcontacts/', views.showcontacts, name='showcontacts'),  # Display all contacts
    path('deletecontacts/<int:id>', views.deletecontacts),          # Delete a specific contact
    path('editcontacts/<int:id>', views.editcontacts, name='editcontacts'),  # Edit a specific contact
    path('updatecontacts/<int:id>', views.updatecontacts, name='updatecontacts'),  # Update a specific contact
    
    # Booking-related routes
    path('booking/', views.booking, name='booking'),                # Booking form
    path('showbookings/', views.showbookings, name='showbookings'),  # Display all bookings
    path('deletebookings/<int:id>', views.deletebookings),           # Delete a specific booking
    path('editbookings/<int:id>', views.editbookings, name='editbookings'),  # Edit a specific booking
    path('updatebookings/<int:id>', views.updatebookings, name='updatebookings'),  # Update a specific booking
]
