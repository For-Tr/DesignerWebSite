from functools import wraps
from django.utils import timezone
from django.http import HttpRequest
from notes.models import AccessLog, Note

def log_access(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.method == 'GET':
            visitor_ip = request.META.get('REMOTE_ADDR', None)
            access_time = timezone.now()

            pk = kwargs.get('pk', None)
            note = Note.objects.get(pk=pk)
            author = note.user

            AccessLog.objects.create(ip_address=visitor_ip, access_time=access_time, author=author)

        return view_func(request, *args, **kwargs)

    return wrapper