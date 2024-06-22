from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import user_dashboard, approve_products, home

urlpatterns = [
    path('', home, name='home'),
    path('user-dashboard/', user_dashboard, name='user_dashboard'),
    path('approve-products/', approve_products, name='approve_products'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)