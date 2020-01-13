from django.contrib import admin
from .models import Honbab, Like

# Register your models here.
@admin.register(Honbab)
class HonbabAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'restraunt',
        'img',
        'level',
        'menu',
        'created_at',
        'updated_at')
    
    list_display_links = (
        'restraunt',
    )
    
    search_fields = [
        'restraunt',
        'created_at'] # 검색기능
    
    
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at']
    list_display_links = ['post', 'user']