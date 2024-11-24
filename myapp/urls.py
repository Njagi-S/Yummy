from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # Admin interface route
    path('admin/', admin.site.urls),  
    
    # Homepage route
    path('index/', views.index, name='index'),  
    
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
    
     # URL for the registration page (default landing page).
    path('', views.register, name='register'),  # Calls the `register` view, which is the default route, named 'register'.

    # URL for the login page.
    path('login/', views.login, name='login'),  # Calls the `login` view, named 'login'
    
    # URL pattern for the image upload page.
    path('uploadimage/', views.upload_image, name='upload'),  
    # Maps the '/uploadimage/' URL to the `upload_image` view function.
    # The name 'upload' allows you to reference this URL easily in templates or code.
    # This route enables users to upload images using a form.

    # URL pattern for displaying all uploaded images.
    path('showimage/', views.show_image, name='image'),  
    # Maps the '/showimage/' URL to the `show_image` view function.
    # The name 'image' is used to refer to this URL in templates or for reverse lookups.
    # This route allows users to view a list or gallery of uploaded images.

    # URL pattern for deleting a specific image by its ID.
    path('imagedelete/<int:id>', views.imagedelete),  
    # Maps the '/imagedelete/<int:id>' URL to the `imagedelete` view function.
    # Captures the integer `id` from the URL and passes it as a parameter to the view.
    # This route enables the deletion of an image record identified by its unique ID.
]
