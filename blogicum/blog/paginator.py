from django.core.paginator import Paginator


paginate_default_value = 10


def get_page_obj(list, page_number, paginate_default_value):
    paginator = Paginator(list, paginate_default_value)
    page_obj = paginator.get_page(page_number)
    return page_obj
