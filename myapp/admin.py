from django.contrib import admin
from myapp.models import BookTable, ContactTable  # Importing the models to be registered in the admin panel

# Register your models here.

# Register the BookTable model in the Django admin interface
admin.site.register(BookTable)

# Register the ContactTable model in the Django admin interface
admin.site.register(ContactTable)