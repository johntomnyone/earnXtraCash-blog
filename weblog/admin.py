from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# class PostAdmin(SummernoteModelAdmin):
# 	summernote_fields = ('content')


class PostAdmin(SummernoteModelAdmin):# admin.ModelAdmin):
	list_display = ('title', 'slug', 'created_on', 'author', 'status')
	list_filter = ('status', 'created_on',)
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)} 
	summernote_fields = ('content')


admin.site.register(Post, PostAdmin)

@admin.register(Comment)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'post', 'created_on', 'active')
	list_filter = ('active', 'created_on')
	search_fields = ('name', 'email', 'body')
	actions = ['appove_comments']


	def approve_comments(sef, request, queryset):
		queryset.update(active=True)

