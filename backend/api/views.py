from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import DestroyAPIView
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.generics import RetrieveAPIView


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Привет от Django API!'})

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    return Response({
        'first_name': user.first_name,
        'last_name': user.last_name,
    })

class TeacherProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = TeacherProfileSerializer(user)
        return Response({'user': serializer.data, 'lessons': serializer.data['lessons']})
    
class LessonListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
    
class LessonCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        lesson_data = {
            'title': data.get('title'),
            'description': data.get('description'),
            'max_score': data.get('max_score'),
            'teacher': request.user.id
        }

        lesson = Lesson.objects.create(
            title=lesson_data['title'],
            description=lesson_data['description'],
            max_score=lesson_data['max_score'],
            teacher=request.user
        )

        content = LessonContent.objects.create(
            lesson=lesson,
            total_blocks=len(data.get('blocks', []))
        )

        for i, block in enumerate(data.get('blocks', []), start=1):
            ContentBlock.objects.create(
                lesson_content=content,
                order=i,
                block_type=block['block_type'],
                title=block['title'],
                text=block.get('text', ''),
                media_url=block.get('media_url', ''),
                task_type=block.get('task_type', ''),       # <-- добавлено
                data=block.get('data', {})                  # <-- добавлено
            )

        return Response({'message': 'Урок успешно создан'})
    
class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class LessonDeleteAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
