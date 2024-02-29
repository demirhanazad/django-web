from django.contrib import admin
from .models import Hobies,Categories
class HobiesAdmin(admin.ModelAdmin):
    list_display=("title","image","is_showed","description","yol","kategori")
    list_editable=("image","is_showed","description","kategori")
    search_fields=("title","description")
    readonly_fields=("yol",)
    list_filter=("kategori","is_showed",)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=("name","yol")
    #list_editable=("image","is_showed","description")
    search_fields=("name","yol")
    readonly_fields=("yol",)
admin.site.register(Hobies,HobiesAdmin)
admin.site.register(Categories,CategoriesAdmin)
