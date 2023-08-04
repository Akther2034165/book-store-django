from django.contrib import admin

# Register your models here.
from book_app.models import BookStoreModel

# admin.site.register(BookStoreModel)

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','book_name','author','category','first_published','last_published')

admin.site.register(BookStoreModel,BookStoreModelAdmin)
