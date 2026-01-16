from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.templatetags.static import static

from .models import Account, UserProfile

# Register your models here.
# modifying the account info on admin page
class AccountAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "username",
                    "last_login", "date_joined", "is_active", )
    list_display_links = ("email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")
    ordering = ("-date_joined",)

    # To override default UserAdmin behavior which considers default Django Model
    # It will also make password read only just like standard Django user model
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    # getting the profile image for displaying in admin panel
    def thumbnail(self, object):
        # since we are using signals to auto create userprofile when account is created,
        # there might be no profile picture. Without profile picture, the dashboard and admin userprofile
        # view will break, hence we give a default profile picture
        if object.profile_picture:
            image_url = object.profile_picture.url
        else:
            image_url = static("images/avatars/dummy-avatar.jpg")

        return format_html('<img src="{}" width="30" style="border-radius:50%;">', image_url)

    thumbnail.short_description = 'Profile Picture'
    
    list_display = ("user", "city", "state", "country", "thumbnail")


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
