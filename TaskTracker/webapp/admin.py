from django.contrib import admin

from webapp.models import Task, State, Type


class TaskAdmin(admin.ModelAdmin):
    fields = ('summary', 'description', 'state', 'type')

    def get_state(self, obj):
        return "\n".join([s.name for s in obj.state.all()])

    def get_type(self, obj):
        return "\n".join([t.name for t in obj.type.all()])


class StateAdmin(admin.ModelAdmin):
    fields = ('name',)


class TypeAdmin(admin.ModelAdmin):
    fields = ('name',)


admin.site.register(Task, TaskAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Type, TypeAdmin)
