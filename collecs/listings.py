from .models import Collection

def collections():
    collecs = Collection.objects.all()
    
    context = {
        'collections': collecs
    }

    return context