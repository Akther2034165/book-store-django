from django import forms 
from book_app.models import BookStoreModel
class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = ['id','book_name','author','category']
        labels = {
            'id' : 'BOOK ID',
            'book_name' : 'BOOK NAME',
            'author' : 'AUTHOR',
            'category' : 'CATEGORY',
            'first_published' : 'FIRST_PUBLISHED',
            'last_published' : 'LAST_PUBLISHED'
        }
        