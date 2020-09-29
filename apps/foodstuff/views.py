from apps.common.pagination import StandardPagination, paginate
from apps.foodstuff.models import Food, Activity, FoodCategory, ActivityCategory, FoodPortion
from rest_framework.views import *
from rest_framework.generics import *
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from apps.calorie_api.serializers import (
    FoodCreateSerializer,
    FoodDetailSerializer,
    ActivityCreateSerializer,
    ActivityDetailSerializer,
    FoodPortionCreateSerializer,
    FoodPortionDetailSerializer,
    FoodCategoryCreateSerializer,
    FoodCategoryDetailSerializer,
)


class FoodStuffActivityCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ActivityCreateSerializer)
    def post(self, request):
        serializer = ActivityCreateSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        activity = Activity.objects.create(
            user_id=request.user.id,
            **serializer.validated_data
        )
        return Response(ActivityDetailSerializer(activity).data)

    def get(self, request):
        instance = Activity.objects.all()
        return Response(ActivityDetailSerializer(instance, many=True).data)


class FoodStuffActivityDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ActivityCreateSerializer)
    def patch(self, request, pk):
        instance = Activity.objects.get(id=pk)
        serializer = ActivityCreateSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return Response(ActivityDetailSerializer(instance).data)

    def delete(self, request, pk):
        instance = Activity.objects.get(id=pk)
        instance.delete()

        return Response('deleted')

    def get(self, request, pk):
        instance = Activity.objects.get(id=pk)
        return Response(ActivityDetailSerializer(instance).data)


class FoodStuffFoodCreateView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodCreateSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class FoodStuffFoodDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=FoodCreateSerializer)
    def patch(self, request, pk):
        instance = Food.objects.get(id=pk)
        serializer = FoodCreateSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return Response(FoodDetailSerializer(instance).data)

    def delete(self, request, pk):
        instance = Food.objects.get(id=pk)
        instance.delete()
        return Response('deleted')

    def get(self, request, pk):
        instance = Food.objects.get(id=pk)
        return Response(FoodDetailSerializer(instance).data)


class FoodStuffFoodCategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=FoodCategoryCreateSerializer)
    def post(self, request):
        serializer = FoodCategoryCreateSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        category = FoodCategory.objects.create(
            user_id=request.user.id,
            **serializer.validated_data
        )
        return Response(FoodCategoryDetailSerializer(category).data)

    def get(self, request):
        instance = FoodCategory.objects.all()
        return Response(FoodCategoryDetailSerializer(instance, many=True).data)


class FoodStuffFoodCategoryDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=FoodCategoryCreateSerializer)
    def patch(self, request, pk):
        instance = FoodCategory.objects.get(id=pk)
        serializer = FoodCategoryCreateSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return Response(FoodCategoryDetailSerializer(instance).data)

    def delete(self, request, pk):
        instance = FoodCategory.objects.get(id=pk)
        instance.delete()
        return Response('deleted')

    def get(self, request, pk):
        instance = FoodCategory.objects.get(id=pk)
        return Response(FoodCategoryDetailSerializer(instance).data)


class FoodStuffFoodPortionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=FoodPortionCreateSerializer)
    def post(self, request):
        serializer = FoodPortionCreateSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        portion = FoodPortion.objects.create(
            user_id=request.user.id,
            **serializer.validated_data
        )
        return Response(FoodPortionDetailSerializer(portion).data)

    def get(self, request):
        instance = FoodPortion.objects.all()
        return Response(FoodPortionDetailSerializer(instance, many=True).data)


class FoodStuffFoodPortionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=FoodPortionCreateSerializer)
    def patch(self, request, pk):
        instance = FoodPortion.objects.get(id=pk)
        serializer = FoodPortionCreateSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return Response(FoodPortionDetailSerializer(instance).data)

    def delete(self, request, pk):
        instance = FoodPortion.objects.get(id=pk)
        instance.delete()
        return Response('deleted')

    def get(self, request, pk):
        instance = FoodPortion.objects.get(id=pk)
        return Response(FoodPortionDetailSerializer(instance).data)

