from rest_framework import routers

from api.views import ExpenseViewSet

router = routers.DefaultRouter()
router.register("expenses", ExpenseViewSet)


urlpatterns = []
urlpatterns += router.urls
