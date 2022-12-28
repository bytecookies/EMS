from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.exceptions import NotFound  
from rest_framework.exceptions import APIException

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except Exception as exc:
            # Here it is
            msg = {
                #"code": 400, # you can remove this line as now the status code will be 400 by default as we have override it in `NotFound` class(see above)
                "error": "Page out of range"
            }
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)
    






class NotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ('bad_request.')
    default_code = 'bad_request'
