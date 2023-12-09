
from django.urls import path
from.import views
app_name='serailapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('serail/<int:serail_id>/',views.detail,name='detail'),
    path('add/',views.add_serail,name='add_serail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]