from django.contrib import admin
from forum.models import Board, Thread, Post

class BoardAdmin(admin.ModelAdmin):
  list_display = ['title']
  class Meta: 
    model = Board

class ThreadAdmin(admin.ModelAdmin):
  list_display = ['title', 'creator', 'board', 'timestamp']
  class Meta:
    model = Thread

class PostAdmin(admin.ModelAdmin):
  list_display = ['creator', 'thread', 'timestamp']
  class Meta:
    model = Post

admin.site.register(Board, BoardAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
