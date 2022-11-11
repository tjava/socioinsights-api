from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "pkid",
        "user",
        "gender",
        "country",
        "state",
        "payment_status",
        "package",
        "expired_at",
        "num_of_months",
    ]
    list_filter = ["gender", "country", "payment_status", "package"]
    list_display_links = ["id", "pkid", "user"]


admin.site.register(Profile, ProfileAdmin)
