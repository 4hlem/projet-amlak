from django.urls import path,re_path
from .views import *
from rest_framework import routers


urlpatterns=[
    path('main/', AnnouncementList.as_view()),#fonctionne
    path('announcements/', SearchAnnouncementList.as_view()), #fonctionne
    path('announcements/filter', FilterAnnouncementList.as_view()),#fonctionne
    path('new-post/',AnnouncementCreate.as_view()), #fonctionne
    path('announcement/<int:pk>', AnnouncementDetail.as_view(http_method_names=['get'])), #fonctionne
    path('announcement/<int:pk>/similar', SimilarAnnouncements.as_view(http_method_names=['get'])), #non
    path('announcement/<int:pk>/update', AnnouncementDetail.as_view(http_method_names=['put'])),#fonctionne
    path('announcement/<int:pk>/delete', AnnouncementDetail.as_view(http_method_names=['delete'])), #fonctionne
    path('profile/<int:pk>', UserProfile.as_view()),   # FONCTIONNE
    path('profile/<int:pk>/announcements', UserAnnouncements.as_view()),  #NON
    path('myprofile/profile/',MyProfile.as_view()),#fonctionne
    path('myprofile/profile/update',UpdateProfile.as_view()),#fonctionne
    path('change-password/', change_password, name='change password'),#fonctionne
    path('myprofile/announcements',MyAnnouncements.as_view()), #fonctionne
    path('myprofile/favorites',Myfavorites.as_view()), #fonctionne
    path('announcement/<str:pk>/add-to-fav/',FavoriteView.as_view(http_method_names=['post']),name='add fav'),#fonctionne
    path('announcement/<str:pk>/add-to-fav/',FavoriteView.as_view(http_method_names=['delete']),name='delete fav'),#fonctionne
    path('register/', register_user, name='register'), #fonctionne ( doit envoyer email password plus est ce agence (true) ou particulier ( false) plus dans profile info  )  #exemple {"email": "jacob@esmith.fr", "password": "test7","is_company" : true ,"profile":{ "telnumber": "3929773", "nom" : "agence adrar", "location" : "Adrar rue du nananinani"}}
    path('login/', LoginAPIView.as_view(), name='login'), #FONCTIONNE
    path('logout/', user_logout, name='logout'),#fonctionne
    ]