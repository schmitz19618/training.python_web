from django.contrib import admin
from myblog.models import Post
from myblog.models import Category
from myblog.models import PostAdmin
from myblog.models import CategoryAdmin
from myblog.models import CategoryInline

admin.site.register(Post, PostAdmin, )
admin.site.register(Category, CategoryAdmin)
# admin.site.register(CategoryInline, )

