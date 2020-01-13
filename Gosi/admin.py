from django.contrib import admin
from .models import Gosi

# Register your models here.
@admin.register(Gosi)
class GosiAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'Gosiname',
        'morning',
        'lunch',
        'dinner',
        'date',
        'created_at',
        'updated_at')
    
    list_display_links = (
        'Gosiname',
    )
    
    search_fields = [
        'Gosiname',
        'created_at'] # 검색기능