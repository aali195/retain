from .models import Collection

def search_collections(request):
    
    queryset_list = order_collections(request)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(is_visible=True).filter(title__icontains=keywords)
            
    context = {
        'keywords': keywords,
        'collections': queryset_list,
        'values': request.GET
    }
    return context


def order_collections(request):
    if 'sorting' not in request.GET:
        criteria = 'rating'
    else:
        criteria = item_dict(request.GET['sorting'])
    
    ordered_list = Collection.objects.order_by(criteria)
    return ordered_list

def item_dict(arg):
    sorting = {
        'rating': '-rating',
        'upload_date': '-upload_date',
        'title': 'title',
        'creator': 'creator',
    }
    return sorting.get(arg, arg)