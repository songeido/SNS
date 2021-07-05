from django.urls import path
from .views import signupfunc,loginfunc,logoutfunc,listfunc,detailfunc,goodfunc,readfunc,deletefunc,BoardCreate,BoardUpdate

urlpatterns = [
    path('signup/',signupfunc,name="signup"),
    path('login/',loginfunc,name="login"),
    path('list/',listfunc,name="list"),
    path('logout/',logoutfunc, name="logout"),
    path('detail/<int:pk>',detailfunc,name="detail"),
    path('good/<int:pk>',goodfunc,name="good"),
    path('read/<int:pk>',readfunc,name="read"),
    #path('create/',create,name="create"),
    path('create/',BoardCreate.as_view(),name="create"),
    path('edit/<int:pk>',BoardUpdate.as_view(),name="edit"),
    path('delete/<int:pk>',deletefunc,name="delete")
]
