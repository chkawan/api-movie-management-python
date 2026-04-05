from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #ADMIN
    path('admin/', admin.site.urls),

    #GENRES
    path('api/v1/', include('genres.urls')),
   
    #ACTOR
    path('api/v1/', include('actors.urls')),

    #MOVIES
    path('api/v1/', include('movies.urls')),

    #REVIEWS
    path('api/v1/', include('reviews.urls')),
    
]

