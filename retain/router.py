from rest_framework import routers

from api.views import (ListCollectionsView,
    StatementsView,
    UserSubscriptionsView,
    CreatedCollectionsView,
    LearnStatementView,
)

router = routers.DefaultRouter()
router.register('collections', ListCollectionsView, base_name='collections')
router.register(r'collections/(?P<collection_id>\d+)/statements', StatementsView, base_name='statements')
router.register('user/subscriptions', UserSubscriptionsView, base_name='subscriptions')
router.register('user/collections', CreatedCollectionsView, base_name='createdcollections')
router.register('user/progress/learn', LearnStatementView, base_name='learning')
