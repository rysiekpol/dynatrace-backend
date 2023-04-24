from django.urls import path, re_path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="NBP API",
      default_version='v1',
      description="API documentation for NBP API",
   ),
   public=True,
)


urlpatterns = [
     path('exchanges/<str:currency>/<str:date>', views.AverageRate.as_view(), name="avg_rate"),
     path('exchanges/average/<str:currency>/<int:N>', views.MinMaxAverage.as_view(), name="avg_min_max_rate"),
     path('exchanges/difference/<str:currency>/<int:N>', views.Difference.as_view(), name="diff_rate"),
     path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]