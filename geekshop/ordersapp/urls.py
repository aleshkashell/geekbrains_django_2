import ordersapp.views as ordersapp
from django.urls import path

app_name="ordersapp"

urlpatterns = [
   path(r'', ordersapp.OrderList.as_view(), name='orders_list'),
   path(r'forming/complete/<int:pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),
   path(r'create/', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
   path(r'read/<int:pk>/', ordersapp.OrderRead.as_view(), name='order_read'),
   path(r'update/<int:pk>/', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
   path(r'delete/<int:pk>/', ordersapp.OrderDelete.as_view(), name='order_delete'),
]