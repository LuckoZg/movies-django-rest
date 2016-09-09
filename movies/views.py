from django.views import generic
from .models import Movie, Critic

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer, MovieDetailSerializer

class ApiIndexView(APIView):

	def get(self, request):
		movies = Movie.objects.order_by('position')[:5]
		serializer = MovieSerializer(movies, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class ApiListView(APIView):

	def get(self, request):
		movies = Movie.objects.order_by('position')
		serializer = MovieSerializer(movies, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class ApiDetailView(APIView):

	def get(self, request, pk):
		movie = Movie.objects.filter(pk=pk)
		serializer = MovieDetailSerializer(movie, many=True)
		return Response(serializer.data)

	def post(self):
		pass