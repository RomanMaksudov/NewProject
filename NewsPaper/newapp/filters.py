from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Post, Category


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    Category = ModelChoiceFilter(
        field_name='PostCategory',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='ALL',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }