
from django.urls import path
from commodity.views import index
# formula as urlpatterns = []
urlpatterns = {
    # path(routing, view function name)
    path('index/', index)
}