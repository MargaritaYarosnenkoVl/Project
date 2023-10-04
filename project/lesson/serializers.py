from rest_framework import serializers
from .models import Lesson, Product


# Сериализатор для просмотра списка доступных уроков
class LessonSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = Lesson
        fields = ('user_name', 'product_name', 'name', 'watched_video', 'status')


# Сериализатор для просмотра уроков по конкретному продукту
class ProductSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = Lesson
        fields = ('user_name', 'product_name', 'name', 'watched_video', 'status', 'view_date')


# Сериализатор для просмотра статистики по продуктам
class ProductStatisticsSerializer(serializers.ModelSerializer):
    viewed_lessons_count = serializers.IntegerField()
    total_watched_duration = serializers.IntegerField()
    students_count = serializers.IntegerField()
    purchase_percentage = serializers.FloatField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'viewed_lessons_count', 'total_watched_duration', 'students_count', 'purchase_percentage')