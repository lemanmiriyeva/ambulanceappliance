from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied

class BlackListIPMiddleware(MiddlewareMixin):

    BLACK_LIST_IP=[
        '127.0.0.1',
        '192.168.10.247'
    ]

    def process_request(self,request):
        if request.META.get('REMOTE_ADDR') in self.BLACK_LIST_IP:
            raise PermissionDenied()