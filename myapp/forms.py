from django import forms
from myapp.models import BookTable, ContactTable, ImageModel


class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = '__all__'

class ContactTableForm(forms.ModelForm):
    class Meta:
        model = ContactTable
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel  # Link this form to the ImageModel
        fields = ['image', 'title', 'price']  # Specify the fields to include in the form
        # This form will allow users to upload an image file, set a title, and provide a price.