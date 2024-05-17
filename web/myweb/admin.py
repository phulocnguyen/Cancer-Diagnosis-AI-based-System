from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )


class OtpTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "otp_code")


admin.site.register(OtpToken, OtpTokenAdmin)
admin.site.register(CustomUser, CustomUserAdmin)


class PredictionResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'prediction_method', 'result', 'diagnosis_type', 'created_at')
    search_fields = ('user__email', 'result', 'prediction_method', 'diagnosis_type')

admin.site.register(PredictionResult, PredictionResultAdmin)
