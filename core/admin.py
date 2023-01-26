from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Quotes,Contact,Reviews,Service,Works])

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    search_fields=('title','small_desc' )
    list_filter=('title','small_desc')
    list_display=('title','small_desc','large_desc')
    # fields=('title','small_desc',)
    fieldsets = (
      ('Standard info', {
          'fields': ('title',)
      }),
      ('Address info', {
          'fields': ('small_desc','large_desc',)
      }),
      
   )