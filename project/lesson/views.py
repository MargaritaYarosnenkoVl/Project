from django.contrib.auth.models import User
from rest_framework import  mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.models import Sum

from .models import Lesson, Product
from .serializers import LessonSerializer, ProductSerializer,  ProductStatisticsSerializer


# Класс для просмотра списка доступных уроков
class LessonListView(mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.filter(access=True)

# Класс для просмотра уроков по конкретному продукту
class ProductLessonsListView(mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(product_id=product_id, access=True)


# Класс для просмотра статистики по продуктам
class ProductStatisticsViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = ProductStatisticsSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        product_statistics = []

        for product in queryset:
            # Количество просмотренных уроков от всех учеников
            viewed_lessons_count = Lesson.objects.filter(product=product, access=True).count()
            # Сколько в сумме все ученики потратили времени на просмотр роликов
            total_watched_duration = Lesson.objects.filter(product=product, access=True).aggregate(total_duration=Sum('watched_video'))['total_duration']
            # Количество учеников занимающихся на продукте
            students_count = User.objects.filter(lesson__product=product).distinct().count()
            # Процент приобретения продукта
            total_users_count = User.objects.count()
            if total_users_count > 0:
                purchase_percentage = (students_count / total_users_count) * 100
            else:
                purchase_percentage = 0

            product.viewed_lessons_count = viewed_lessons_count
            product.total_watched_duration = total_watched_duration
            product.students_count = students_count
            product.purchase_percentage = purchase_percentage

            product_statistics.append(product)

        serializer = ProductStatisticsSerializer(product_statistics, many=True)
        return Response(serializer.data)