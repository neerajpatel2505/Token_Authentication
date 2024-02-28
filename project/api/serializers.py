# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import MovieModel,StudentModel

# ----------------------ModelSerializer-------------------
# The ModelSerializer class is the same as a regular Serializer class, except that:
# It will automatically generate a set of fields for you, based on the model.
# It will automatically generate validators for the serializer, such as unique_together validators.
# It includes simple default implementations of .create() and .update().
class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = MovieModel
		fields = ('id','title', 'description')

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentModel
		fields = ('id','name', 'email','city')

# class MovieSerializer(serializers.HyperlinkedModelSerializer):
# 	# specify model and fields
# 	class Meta:
# 		model = MovieModel
# 		fields = ('id','title', 'description')


# class MovieSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length = 200)
#     description = serializers.CharField(max_length = 200)