from django.contrib import admin
from .models import Item, Evaluation


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'seasons')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'rating', 'comment','total_likes','created')

    def total_likes(self,obj):
        return obj.likes.count()


# @admin.register(Evaluation)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ('user', 'evaluation', 'created')
