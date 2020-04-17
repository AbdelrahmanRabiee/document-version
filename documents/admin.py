from django.contrib import admin

from documents.models import UserDocument, VersionControlPloicy
# Register your models here.

admin.site.register(UserDocument)
admin.site.register(VersionControlPloicy)