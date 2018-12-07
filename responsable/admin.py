from django.contrib import admin
from .models import Profile, Responsable, Planner, NoGuest, Additional, FuneralService

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','birthday','city','phone')

class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('name','birthday','phone','email')

class PlannerAdmin(admin.ModelAdmin):
    list_display = ('ashes','venue','wish','user')

class NoGuestAdmin(admin.ModelAdmin):
    list = ('name')

class FuneralServiceAdmin(admin.ModelAdmin):
    list_display = ('name','description')

class AdditionalAdmin(admin.ModelAdmin):
    list_display = ('name','description')




admin.site.register(Profile,ProfileAdmin)
admin.site.register(Responsable,ResponsableAdmin)
admin.site.register(Planner,PlannerAdmin)
admin.site.register(NoGuest,NoGuestAdmin)
admin.site.register(FuneralService,FuneralServiceAdmin)
admin.site.register(Additional,AdditionalAdmin)


# Register your models here.
