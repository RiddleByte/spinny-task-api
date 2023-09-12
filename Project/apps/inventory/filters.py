import django_filters
from .models import Box
from django.db.models import F


class ListBoxFilter(django_filters.FilterSet):
    length_more_than = django_filters.NumberFilter(field_name='length', lookup_expr='gt')
    length_less_than = django_filters.NumberFilter(field_name='length', lookup_expr='lt')
    
    breadth_more_than = django_filters.NumberFilter(field_name='breadth', lookup_expr='gt')
    breadth_less_than = django_filters.NumberFilter(field_name='breadth', lookup_expr='lt')
    
    height_more_than = django_filters.NumberFilter(field_name='height', lookup_expr='gt')
    height_less_than = django_filters.NumberFilter(field_name='height', lookup_expr='lt')
    
    area_more_than = django_filters.NumberFilter(method='filter_by_area_more_than')
    area_less_than = django_filters.NumberFilter(method='filter_by_area_less_than')
    
    volume_more_than = django_filters.NumberFilter(method='filter_by_volume_more_than')
    volume_less_than = django_filters.NumberFilter(method='filter_by_volume_less_than')
    
    created_by = django_filters.CharFilter(field_name='created_by')
    
    created_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lt')
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gt')
    
    class Meta:
        model = Box
        fields = []

    def filter_by_area_more_than(self, queryset, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            area=F('length') * F('breadth')
        ).filter(area__gt=value)
    
    def filter_by_area_less_than(self, queryset, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            area=F('length') * F('breadth')
        ).filter(area__lt=value)

    def filter_by_volume_more_than(self, queryset, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            volume=F('length') * F('breadth') * F('height')
        ).filter(volume__gt=value)

    def filter_by_volume_less_than(self, queryset, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            volume=F('length') * F('breadth') * F('height')
        ).filter(volume__lt=value)
    


class MyBoxFilter(django_filters.FilterSet):
    length_more_than = django_filters.NumberFilter(field_name='length', lookup_expr='gt')
    length_less_than = django_filters.NumberFilter(field_name='length', lookup_expr='lt')
    
    breadth_more_than = django_filters.NumberFilter(field_name='breadth', lookup_expr='gt')
    breadth_less_than = django_filters.NumberFilter(field_name='breadth', lookup_expr='lt')
    
    height_more_than = django_filters.NumberFilter(field_name='height', lookup_expr='gt')
    height_less_than = django_filters.NumberFilter(field_name='height', lookup_expr='lt')
    
    area_more_than = django_filters.NumberFilter(method='filter_by_area_more_than')
    area_less_than = django_filters.NumberFilter(method='filter_by_area_less_than')
    
    volume_more_than = django_filters.NumberFilter(method='filter_by_volume_more_than')
    volume_less_than = django_filters.NumberFilter(method='filter_by_volume_less_than')

    class Meta:
        model = Box
        fields = []

    def filter_by_area_more_than(self, queryset, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            area=F('length') * F('breadth')
        ).filter(area__gt=value)
    
    def filter_by_area_less_than(self, queryset, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            area=F('length') * F('breadth')
        ).filter(area__lt=value)

    def filter_by_volume_more_than(self, queryset, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            volume=F('length') * F('breadth') * F('height')
        ).filter(volume__gt=value)

    def filter_by_volume_less_than(self, queryset, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            volume=F('length') * F('breadth') * F('height')
        ).filter(volume__lt=value)