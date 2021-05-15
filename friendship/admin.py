from django.contrib import admin
from .models import FriendRequest, FriendList


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(FriendList)
class FriendListeAdmin(admin.ModelAdmin):
    pass
