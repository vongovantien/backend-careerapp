from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_size = 10
    page_query_description = ("")
