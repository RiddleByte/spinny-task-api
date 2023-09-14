from datetime import datetime, timedelta

import django_filters.rest_framework
from django.utils import timezone
from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .constants import A1, L1, L2, V1
from .filters import ListBoxFilter, MyBoxFilter
from .models import Box
from .permissions import IsStaffUser
from .serializers import AdminBoxSerializer, GuestBoxSerializer


class BoxViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Box.objects.all()
    serializer_class = GuestBoxSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_class = ListBoxFilter

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.validated_data.pop("created_by", None)
        serializer.validated_data.pop("created_at", None)
        super().perform_update(serializer)

    def create(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated, IsStaffUser]
        self.serializer_class = AdminBoxSerializer
        request.data["created_by"] = request.user.id
      
        length = float(request.data.get("length", 0))  
        breadth = float(request.data.get("breadth", 0))
        height = float(request.data.get("height", 0))

        average_area = (length * breadth) if length > 0 and breadth > 0 else 0
        average_volume = (length * breadth * height) if length > 0 and breadth > 0 and height > 0 else 0
        
        if average_area >= A1:
            return Response(
                {"error": "Average area of all boxes exceeds A1"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if average_volume >= V1:
            return Response(
                {"error": "Average volume of user's boxes exceeds V1"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        current_week_start = timezone.now() - timedelta(days=timezone.now().weekday())
        current_week_end = current_week_start + timedelta(days=6)
        week_boxes_count = Box.objects.filter(
            created_at__range=(current_week_start, current_week_end)
        ).count()

        if week_boxes_count >= L1:
            return Response(
                {"error": "Total boxes added in a week exceeds L1"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_week_boxes_count = Box.objects.filter(
            created_by=request.user,
            created_at__range=(current_week_start, current_week_end)
        ).count()

        if user_week_boxes_count >= L2:
            return Response(
                {"error": "Total boxes added in a week by the user exceeds L2"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated, IsStaffUser]
        self.serializer_class = AdminBoxSerializer
        request.data["updated_by"] = request.user.id

        length = float(request.data.get("length", 0))  
        breadth = float(request.data.get("breadth", 0))
        height = float(request.data.get("height", 0))

        average_area = (length * breadth) if length > 0 and breadth > 0 else 0
        average_volume = (length * breadth * height) if length > 0 and breadth > 0 and height > 0 else 0
        
        if average_area >= A1:
            return Response(
                {"error": "Average area of all boxes exceeds A1"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if average_volume >= V1:
            return Response(
                {"error": "Average volume of user's boxes exceeds V1"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        current_week_start = timezone.now() - timedelta(days=timezone.now().weekday())
        current_week_end = current_week_start + timedelta(days=6)
        week_boxes_count = Box.objects.filter(
            created_at__range=(current_week_start, current_week_end)
        ).count()

        if week_boxes_count >= L1:
            return Response(
                {"error": "Total boxes added in a week exceeds L1"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_week_boxes_count = Box.objects.filter(
            created_by=request.user,
            created_at__range=(current_week_start, current_week_end)
        ).count()

        if user_week_boxes_count >= L2:
            return Response(
                {"error": "Total boxes added in a week by the user exceeds L2"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated, IsStaffUser]
        self.serializer_class = AdminBoxSerializer

        length = float(request.data.get("length", 0))  
        breadth = float(request.data.get("breadth", 0))
        height = float(request.data.get("height", 0))

        average_area = (length * breadth) if length > 0 and breadth > 0 else 0
        average_volume = (length * breadth * height) if length > 0 and breadth > 0 and height > 0 else 0
        
        if average_area >= A1:
            return Response(
                {"error": "Average area of all boxes exceeds A1"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if average_volume >= V1:
            return Response(
                {"error": "Average volume of user's boxes exceeds V1"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        current_week_start = timezone.now() - timedelta(days=timezone.now().weekday())
        current_week_end = current_week_start + timedelta(days=6)
        week_boxes_count = Box.objects.filter(
            created_at__range=(current_week_start, current_week_end)
        ).count()

        if week_boxes_count >= L1:
            return Response(
                {"error": "Total boxes added in a week exceeds L1"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_week_boxes_count = Box.objects.filter(
            created_by=request.user,
            created_at__range=(current_week_start, current_week_end)
        ).count()

        if user_week_boxes_count >= L2:
            return Response(
                {"error": "Total boxes added in a week by the user exceeds L2"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        return super().destroy(request, *args, **kwargs)


    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated]
        self.serializer_class = (
            AdminBoxSerializer if request.user.is_staff else GuestBoxSerializer
        )
        self.filterset_class = ListBoxFilter
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=["GET"], name="List my boxes", url_path="my")
    def list_my_boxes(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated]
        self.queryset = Box.objects.filter(created_by=request.user)
        self.serializer_class = (
            AdminBoxSerializer if request.user.is_staff else GuestBoxSerializer
        )
        self.filterset_class = MyBoxFilter
        return super().list(request, *args, **kwargs)
