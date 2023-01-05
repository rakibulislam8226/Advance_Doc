
from django.contrib import admin
from django.urls import path,include
from model_manager import views as query_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Advance Doc",
      default_version='v1',
      description="Advance Doc",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="abc@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('student/',query_views.StudentView, name='student'),
    path('employee/',query_views.EmploeeView, name='employee'),
    
    path('aggregation/',include('aggregation.urls')),
    path('abstraction/',include('model_abstraction.urls')),
    path('learn_signals/',include('learn_signals.urls')),
    path('country_city_api/',include('country_city_api.urls')),
    path('social_add_block/',include('social_add_block.urls')),
    path('model_manager/',include('model_manager.urls')),
    
    
]
