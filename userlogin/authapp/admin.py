from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Project, Skill, Achievement, ContactForm

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_by',)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'created_by')
    search_fields = ('name',)
    list_filter = ('created_by',)


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_by',)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(ContactForm, ContactFormAdmin)