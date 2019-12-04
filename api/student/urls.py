from rest_framework import routers


from .viewsets import StudentViewSet

router= routers.SimpleRouter()
router.register('Students',StudentViewSet)


urlpatterns= router.urls