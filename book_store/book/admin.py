from django.contrib import admin
from book.models import BookStoreModel

# Register your models here.
# admin.site.register(BookStoreModel)
class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','book_name','author','category')
    
admin.site.register(BookStoreModel, BookStoreModelAdmin)