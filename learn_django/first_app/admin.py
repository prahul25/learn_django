from django.contrib import admin
from .models import Chaia_Variety,Store,Chai_Review,ChaiCertificate


# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = Chai_Review
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ("name",'type','date_added','price','description')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ("name","location")
    filter_horizontal = ("chai_varities",)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ("chai", "certificate_number")
    
admin.site.register(Chaia_Variety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)