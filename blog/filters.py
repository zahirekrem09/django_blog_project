import django_filters
from django_filters import DateFilter
from django import forms
from blog.models import Post


class PostFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = DateFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Post
        fields = ("title", "is_favorite",
                  'created_at', 'category')
        #fields = '__all__'
        widgets = {
            'category': forms.CheckboxSelectMultiple,
            'is_favorite': forms.RadioSelect
        }
        exclude = ['created_at']
