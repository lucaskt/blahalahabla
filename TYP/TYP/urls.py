from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register(r'patients', viewsets.PatientViewSet)
router.register(r'doctor', viewsets.DoctorViewSet)
router.register(r'medicine', viewsets.MedicineViewSet)
router.register(r'recurrenttreatment', viewsets.RecurringTreatmentViewSet)
router.register(r'pilltaken', viewsets.PillTakenViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', 'core.views.index', name='index'),
    url(r'^doctorview/patients/$', 'core.views.patients', name='patients'),
    url(r'^doctorview/scoreboard/$', 'core.views.scoreboard', name='scoreboard'),
]
