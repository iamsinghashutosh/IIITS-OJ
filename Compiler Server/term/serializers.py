from rest_framework import serializers
from term.models import program
from term.models import author

class programSerializer(serializers.ModelSerializer):
	class Meta:
		model=program
		fields='__all__'

class authorSerializer(serializers.ModelSerializer):
	class Meta:
		model=author
		fields='__all__'
