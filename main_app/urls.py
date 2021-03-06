from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('trails/', views.trails_index, name='trails_index'),
    path('trails/<int:trail_id>/', views.trails_detail, name='trails_detail'),
    path('trails/create/', views.TrailCreate.as_view(), name='trails_create'),
    path('trails/<int:pk>/update/', views.TrailUpdate.as_view(), name='trails_update'),
    path('trails/<int:pk>/delete/', views.TrailDelete.as_view(), name='trails_delete'),
    path('trails/<int:trail_id>/add_review/', views.add_review, name='add_review'),
    path('reviews/<int:review_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]