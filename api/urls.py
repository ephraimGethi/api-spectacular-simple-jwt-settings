from django.urls import path,include
from .views import import_dummy_data,numProducts
from rest_framework.routers import DefaultRouter
from .views import *
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router.register(r"products",ProductViewset)

urlpatterns = [
    # path('import-data/',import_dummy_data),
    path('get-product-count/',numProducts,name='get products count'),
    path('',include(router.urls),name='products'),
    # path('token',obtain_auth_token)
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view())
]