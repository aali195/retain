from collecs.models import Collection

def featured_collecs():
    filtered_collecs = filter_collections(Collection)

    context = {
        'collections': filtered_collecs
    }
    return context


def filter_collections(collecs):
    filtered_collecs = Collection.objects.order_by('-rating').filter(is_visible=True)[:3]
    return filtered_collecs