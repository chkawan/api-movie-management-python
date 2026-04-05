from rest_framework import serializers
from movies.models import Movie




class MovieSeriealizer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'