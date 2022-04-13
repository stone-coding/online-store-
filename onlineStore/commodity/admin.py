from django.contrib import admin

# Register your models here.
from commodity.models import BookInfo,PeopleInfo

#register the model
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)

#restart the django
