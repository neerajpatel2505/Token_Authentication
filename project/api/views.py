from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from rest_framework.permissions import AllowAny
# from rest_framework.permissions import IsAdminUser
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# create a viewset
# class MovieViewSet(viewsets.ReadOnlyModelViewSet):
class MovieViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	# permission_classes = [AllowAny]
	# permission_classes = [IsAdminUser]
	# permission_classes = [IsAuthenticatedOrReadOnly]
	
	# define queryset
	queryset = MovieModel.objects.all()

	serializer_class = MovieSerializer

class StudentViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = StudentModel.objects.all()
	serializer_class = StudentSerializer
