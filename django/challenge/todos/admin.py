from django.contrib import admin

from todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'order', 'description', 'is_completed', 'effort',)
    fieldsets = (
        ('Info', {
            'fields': (
                'date',
                'description',
                'is_completed',
                'order',
            )
        }),
    )
