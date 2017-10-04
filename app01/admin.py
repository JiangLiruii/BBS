from django.contrib import admin

# Register your models here.
from app01 import models
#
# class News_Info_Admin(admin.ModelAdmin):
# 	list_display = ('title','favor_count','reply_count')


admin.site.register(models.User_type)
admin.site.register(models.Admin)
admin.site.register(models.Chat)
admin.site.register(models.NewsType)
admin.site.register(models.News)
admin.site.register(models.Reply)
