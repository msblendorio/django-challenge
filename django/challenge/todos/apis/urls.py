from rest_framework import routers

from todos.apis.viewsets import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)
urlpatterns = router.urls
