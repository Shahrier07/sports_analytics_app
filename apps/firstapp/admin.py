from django.contrib import admin

from .views import volleyball_view
from .models import Match, MatchView, Player, Team, User, MatchExtra
from .models import School, VolleyBallModel,FootBallModel

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =('id','name','mobile_number')

@admin.register(School)
class Useradmin(admin.ModelAdmin):
    list_display =("schoolID","schoolName", "schoolAddress","schoolThana","postCode","subDistrict","district","phoneNo","email","contPerName","schlUname","password","schoolType","studentType")


admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(MatchExtra)
admin.site.register(MatchView)
admin.site.register(VolleyBallModel)
admin.site.register(FootBallModel)
