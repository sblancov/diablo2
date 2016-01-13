from django.contrib import admin

from models import Helm


@admin.register(Helm)
class HelmAdmin(admin.ModelAdmin):
    pass
