from django.urls import path
from product.views import create_product, get_products, update_product, delete_product

urlpatterns = [path("", get_products, name="get_all"),
               path("save", create_product, name="save"),
               path("update/<int:id>", update_product, name="update"),
               path("delete/<int:id>", delete_product, name="remove"),
               # path('save', create_product, name="save")
              ]






