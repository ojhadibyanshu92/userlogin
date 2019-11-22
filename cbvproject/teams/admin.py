from django.contrib import admin

from . import models


class PlayerInline(admin.TabularInline):
    model = models.Player

class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'team', 'position', 'age']

admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.Player, PlayerAdmin)
