from django.urls import path
from . import views

urlpatterns = [
     path('exchanges/<str:currency>/<str:date>', views.AverageRate.as_view(), name="avg_rate"),
     path('exchanges/average/<str:currency>/<int:N>', views.MinMaxAverage.as_view(), name="avg_min_max_rate"),
     path('exchanges/difference/<str:currency>/<int:N>', views.Difference.as_view(), name="diff_rate"),
]