from django.contrib import admin

from blog.models import Article, Tag, Comment
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class ArticleAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    list_display  = ['title', 'get_tags', 'datetime']
    list_filter   = ['tags', 'datetime']
    search_fields = ['title', 'content']
    ordering      = ['-datetime']

'''
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ['title', 'get_tags', 'datetime']
    list_filter   = ['tags', 'datetime']
    search_fields = ['title', 'content']
    ordering      = ['-datetime']
'''


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'weight']
    ordering     = ['weight']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'to_article', 'to_comment', 'datetime']
    list_filter  = ['datetime']
    raw_id_fields = ('to_article', 'to_comment',)



admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)







