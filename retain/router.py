from rest_framework import routers

from api.views import ListCollectionsView

router = routers.DefaultRouter()
router.register('collections', ListCollectionsView, base_name='collections')