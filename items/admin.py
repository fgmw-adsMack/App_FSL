from django.contrib import admin
from .models import Item, Evaluation


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'seasons')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'rating', 'comment')
