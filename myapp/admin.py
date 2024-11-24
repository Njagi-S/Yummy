from django.contrib import admin
from myapp.models import BookTable, ContactTable,Member, ImageModel  # Importing the models to be registered in the admin panel

# Register your models here.

# Register the BookTable model in the Django admin interface
admin.site.register(BookTable)

# Register the ContactTable model in the Django admin interface
admin.site.register(ContactTable)

# Register the Member model with the admin site.
# Admin users can add, edit, and delete Member accounts directly from the admin interface.
admin.site.register(Member)

# Register the ImageModel model in the Django admin interface
admin.site.register(ImageModel)