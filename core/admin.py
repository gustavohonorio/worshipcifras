from django.contrib import admin
from .models import CardDestaque


@admin.register(CardDestaque)
class CardDestaqueAdmin(admin.ModelAdmin):
    pass
