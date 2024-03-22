from django.contrib import admin
from .models import Reaction

# Register your models here.
@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    pass