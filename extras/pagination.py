from typing import Type

from tortoise.queryset import QuerySet
from extras.context_request import request


class PageNumberPagination:
    page_size = 10
    page_size_query_param = "pageSize"
    page = 1
    page_query_param = "pageNo"

    def __init__(
        self,
        page_size: int = None,
        page: int = None,
        page_query_param: str = None,
        page_size_query_param: str = None,
    ):
        if page_size is not None:
            self.page_size = page_size
        elif page_size_query_param is not None:
            self.page_size_query_param = page_size_query_param

        if page is not None:
            self.page = page
        elif page_query_param is not None:
            self.page_query_param = page_query_param

    def get_page_size(self) -> int:
        return int(request.query_params.get(self.page_size_query_param, self.page_size))

    def get_page(self) -> int:
        return int(request.query_params.get(self.page_query_param, self.page))

    async def paginate_queryset(self, queryset: QuerySet):
        page_size = self.get_page_size()
        page = self.get_page()
        offset = (int(page) - 1) * page_size
        page_queryset = await queryset.offset(offset).limit(page_size).all()
        return page_queryset
