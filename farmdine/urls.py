from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Farmdine Backend API",
      default_version='v1',
      description="Backend API for Farmdine, a B2B marketplace for food vendors and restaurants.",
      terms_of_service="https://www.farmdine.ioo/policies/terms/",
      contact=openapi.Contact(email="contact@farmdine.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # Simple-jwt urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API DOCS URL
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # APP urls
    path('api/accounts/', include('accounts.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/order/', include('order.urls')),
    path('api/payments/', include('payments.urls')),
    #Products app
    path('api/products/', include('products.urls')),
    #Comments app
    path('api/comments/', include('comments.urls')),
    #Likes app
    path('api/likes/', include('likes.urls')),
    #logistics app
    path('api/logistics/', include('logistics.urls')),
    # review app
    path('api/reviews/', include('reviews.urls')),
    # vendor_verification app
    path('api/vendor_verification/', include('vendor_verification.urls')),
    
]
