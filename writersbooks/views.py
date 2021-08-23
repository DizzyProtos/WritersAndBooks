from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Writer, Book
import json


def get_writer(request, id=None):
    if id is None:
        return HttpResponse('{}')

    try:
        writer_model = Writer.objects.prefetch_related('book_set').get(id=id)
    except ObjectDoesNotExist as e:
        return HttpResponse('{}')

    writer_dict = writer_model.to_dict()
    writer_dict['books'] = []
    for book in writer_model.book_set.all():
        writer_dict['books'].append(book.to_dict())
    return HttpResponse(json.dumps(writer_dict))
