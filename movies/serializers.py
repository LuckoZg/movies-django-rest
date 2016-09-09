from rest_framework import serializers
from .models import *

class CriticSerializer(serializers.ModelSerializer):
	author = serializers.CharField(source='author.name', read_only=True)
	publisher = serializers.CharField(source='publisher.name', read_only=True)

	class Meta:
		model = Critic
		fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Genre
		fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Person
		fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
	genre = GenreSerializer(many=True, read_only=True)
	director = PersonSerializer(many=True, read_only=True)
	author = PersonSerializer(many=True, read_only=True)
	actor = PersonSerializer(many=True, read_only=True)
	production_company = serializers.CharField(source='production_company.name', read_only=True)

	class Meta:
		model = Movie
		fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
	critics = CriticSerializer(many=True, read_only=True)
	genre = GenreSerializer(many=True, read_only=True)
	director = PersonSerializer(many=True, read_only=True)
	author = PersonSerializer(many=True, read_only=True)
	actor = PersonSerializer(many=True, read_only=True)
	production_company = serializers.CharField(source='production_company.name', read_only=True)

	class Meta:
		model = Movie
		fields = '__all__'