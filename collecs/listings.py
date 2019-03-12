from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Collection

def collections(request):
    collecs = Collection.objects.order_by('-upload_date').filter(is_visible=True)

    paginator = Paginator(collecs, 6)
    page = request.GET.get('page')
    paged_collections = paginator.get_page(page)
    
    context = {
        'collections': paged_collections
    }

    return context