from django.contrib import admin
from .models import User, Post, Comment, Reactor

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "name", "bio"]

class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "description"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["writer", "description"]

class ReactorAdmin(admin.ModelAdmin):
    list_display = ["reactor", "post"]

# Registering
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reactor, ReactorAdmin)