from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile, SocialMedia, ProfileSocialMedia, Category, Comment, Technology, Project, TypesTechnology, Qualities, Occupation

@admin.register(Occupation)
class OcuppationAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

@admin.register(Qualities)
class QualitiesAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ["name", "link"]

@admin.register(TypesTechnology)
class TypesTechnologyAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

@admin.register(ProfileSocialMedia)
class ProfileSocialMediaAdmin(admin.ModelAdmin):
    list_display = ["profile", "social_media", "identification"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["profile", "comment"]

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "timestamp", "link"]

class SocialMediasInline(admin.StackedInline):
    model = ProfileSocialMedia

class ProfileInline(admin.StackedInline):
    model = Profile
    inlines = [SocialMediasInline]

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'password', 'last_name']
    list_display = ['username', 'first_name']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)



