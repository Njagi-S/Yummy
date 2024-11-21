from django.contrib import admin
from myapp.models import BookTable, ContactTable
# Register your models here.
admin.site.register(BookTable)
admin.site.register(ContactTable)
