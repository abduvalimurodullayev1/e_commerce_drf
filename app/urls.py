from django.urls import path

from app.views.MyProducts import MyFavoriteView, MyFavoriteCreate
from app.views.category_products import CategoryView, CategoryCreate, ProductView, ProductCreate, CategoryUpdate, \
    CategoryDestroy, ProductDestroy, ProductUpdate
from app.views.user_auth import UserRegisterView, LoginView, LogoutAPIView, UpdateProfileApiView, ProfileRetrieveAPIView

urlpatterns = [
    # User
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path("Logout", LogoutAPIView.as_view(), name="Logout"),
    # Category
    path("CategoryList", CategoryView.as_view(), name='CategoryList'),
    path("CategoryCreate", CategoryCreate.as_view(), name="create_category"),
    path("CategoryUpdate", CategoryUpdate.as_view(), name="update"),
    path("CategoryDestroy", CategoryDestroy.as_view(), name="delete"),
    # Product
    path("ProductList", ProductView.as_view(), name="list_product"),
    path("ProductCreate", ProductCreate.as_view(), name="product-create"),
    path("ProductDestroy", ProductDestroy.as_view(), name="destroy"),
    path("UpdateProduct", ProductUpdate.as_view(), name="destroy"),
    # Profile
    path("UserProfile", UpdateProfileApiView.as_view(), name="profile"),
    path("UserProfile", ProfileRetrieveAPIView.as_view(), name="profile"),
    # Favorites
    path("MyFavoriteCreate", MyFavoriteCreate.as_view(), name="crate-my-product"),
    path("MyFavorites", MyFavoriteView.as_view(), name="MyProducts")


]
