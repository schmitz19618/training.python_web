from django.contrib import admin
from myblog.models import Post
from myblog.models import Category
from myblog.models import PostAdmin
from myblog.models import CategoryAdmin

admin.site.register(Post, PostAdmin, )
admin.site.register(Category, CategoryAdmin, )


