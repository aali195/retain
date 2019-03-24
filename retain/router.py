from rest_framework import routers

from api.views import ListCollectionsView, GetStatementsView, GetUserSettingsView

router = routers.DefaultRouter()
router.register('collections', ListCollectionsView, base_name='collections')
router.register(r'collections/(?P<collection_id>\d+)/statements', GetStatementsView, base_name='statements')
router.register('user/settings', GetUserSettingsView, base_name='statements')