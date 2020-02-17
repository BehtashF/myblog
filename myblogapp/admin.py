from django.contrib import admin
from django.db import models
from myblogapp.models import Post,Category,Profile
# from pagedown.widgets import AdminPagedownWidget



class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','category',]

class CatAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    prepopulated_fields = {'slug':('title',)}

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['author',]
    # prepopulated_fields = {'slug':('author',)}

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CatAdmin)
admin.site.register(Profile,ProfileAdmin)




# class AlbumAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': AdminPagedownWidget },
#     }

