from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.indexBlog,name="indexBlog"),
    path('tierList/',views.tierList,name="tierList"),
    path('news/',views.news,name="news"),
    path('comunity/',views.comunity,name="comunity"),
]