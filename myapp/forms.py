from django import forms
from myapp.models import BookTable, ContactTable


class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = '__all__'

class ContactTableForm(forms.ModelForm):
    class Meta:
        model = ContactTable
        fields = '__all__'