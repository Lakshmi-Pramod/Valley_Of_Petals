from django.contrib import admin
from .models import flora
from .models import habitat
from .models import characteristics
from .models import can_view
from .models import viewer_email
from .models import Viewer
from .models import marketValue
from .models import Notification
# Register your models here.
class floraAdmin(admin.ModelAdmin):
    list_display=("flora_id","species","region","evaluated_date")

class habitatAdmin(admin.ModelAdmin):
    list_display=("climate","altitude_range","season","soil","flora_id")

class characteristicsAdmin(admin.ModelAdmin):
    list_display=("b_name","utility","avail","flora_id")

class can_viewAdmin(admin.ModelAdmin):
    list_display=("flora_id","v_id")

class viewer_emailAdmin(admin.ModelAdmin):
    list_display=("v_id","email")

class ViewerAdmin(admin.ModelAdmin):
    list_display=("v_id","uname","psd","city","state","pin")

class marketValueAdmin(admin.ModelAdmin):
    list_display=("item_id","cons","exp","cost","flora_id")

class NotificationAdmin(admin.ModelAdmin):
    list_display=("n_id","flora_s","login_date","t_in","t_out","v_id")

admin.site.register(flora,floraAdmin)
admin.site.register(habitat,habitatAdmin)
admin.site.register(characteristics,characteristicsAdmin)
admin.site.register(can_view,can_viewAdmin)
admin.site.register(viewer_email,viewer_emailAdmin)
admin.site.register(Viewer,ViewerAdmin)
admin.site.register(marketValue,marketValueAdmin)
admin.site.register(Notification,NotificationAdmin)