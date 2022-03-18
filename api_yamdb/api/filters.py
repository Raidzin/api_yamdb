class TitleFilter:

    def get_filter_fields(self, view, request):
        return getattr(view, 'filter_fields', dict())

    def filter_by_field(self, queryset, field, value):
        return queryset.filter(**{field + '__contains': value})

    def filter_queryset(self, request, queryset, view):
        filter_fields = self.get_filter_fields(view, request)
        for field in filter_fields:
            query_param = request.query_params.get(field.split('__')[0])
            if query_param is not None:
                queryset = self.filter_by_field(queryset, field, query_param)
        return queryset
