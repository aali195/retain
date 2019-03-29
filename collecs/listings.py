from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Collection

def list_collections(request):
    filtered_collecs = filter_collections(Collection)

    paged_collections = add_pagination(request, filtered_collecs)

    context = {
        'collections': paged_collections
    }
    return context


def filter_collections(collecs):
    filtered_collecs = Collection.objects.order_by('-upload_date').filter(is_visible=True).filter(size__gte=10)
    return filtered_collecs

def add_pagination(request, collecs):
    paginator = Paginator(collecs, 6)
    page = request.GET.get('page')
    paged_collections = paginator.get_page(page)
    return paged_collections