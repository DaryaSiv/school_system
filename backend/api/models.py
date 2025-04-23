from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Учитель'),
        ('student', 'Ученик'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    email = models.EmailField("Электронная почта", unique=True)

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.role})"

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name='lessons')
    max_score = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Максимальная оценка"
    )

    def __str__(self):
        return self.title

class LessonContent(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='content')
    total_blocks = models.PositiveIntegerField()

    def __str__(self):
        return f"Контент для: {self.lesson.title}"

class ContentBlock(models.Model):
    LECTURE = 'lecture'
    PRACTICE = 'practice'
    FINAL = 'final'

    TASK_CHOICES = [
        ('test', 'Тест'),
        ('match', 'Сопоставление'),
        ('compare', 'Сравнение'),
        ('fill', 'Заполнение пропусков'),
        ('creative', 'Творческое задание'),
    ]

    BLOCK_TYPES = [
        (LECTURE, 'Лекционный'),
        (PRACTICE, 'Практический'),
        (FINAL, 'Завершающий'),
    ]

    lesson_content = models.ForeignKey(LessonContent, on_delete=models.CASCADE, related_name='blocks')
    order = models.PositiveIntegerField()
    block_type = models.CharField(max_length=10, choices=BLOCK_TYPES)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    media_url = models.URLField(blank=True, null=True)
    
    # Новое поле
    task_type = models.CharField(max_length=20, choices=TASK_CHOICES, blank=True, null=True)
    data = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.get_block_type_display()} #{self.order} — {self.title}"


class LessonProgress(models.Model):
    student = models.ForeignKey('User', on_delete=models.CASCADE, related_name='lesson_progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progress')
    grade = models.IntegerField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'lesson')

    def __str__(self):
        return f"{self.student.username} — {self.lesson.title} — {'✔' if self.completed else '✘'}"
