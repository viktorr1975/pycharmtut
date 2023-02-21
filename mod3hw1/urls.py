from rest_framework.routers import DefaultRouter
from .views import TasksViewSet

# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter()

app_name = "tasksapp"


router.register(
    prefix="tasks",
    viewset=TasksViewSet,
    basename="tasks",
)

urlpatterns = router.urls
