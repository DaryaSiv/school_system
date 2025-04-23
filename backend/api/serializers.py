from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from .models import *

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LessonSerializer(serializers.ModelSerializer):
    blocks = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'max_score', 'blocks']

    def get_blocks(self, obj):
        try:
            content = obj.content  # LessonContent
            blocks = content.blocks.all().order_by('order')  # ContentBlock
            return ContentBlockSerializer(blocks, many=True).data
        except LessonContent.DoesNotExist:
            return []

class TeacherProfileSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, source='lessons')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'lessons']

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ['order', 'block_type', 'title', 'text', 'task_type', 'data']

class LessonContentSerializer(serializers.ModelSerializer):
    blocks = ContentBlockSerializer(many=True, read_only=True)

    class Meta:
        model = LessonContent
        fields = ['total_blocks', 'blocks']

class LessonDetailSerializer(serializers.ModelSerializer):
    content = LessonContentSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'max_score', 'content']