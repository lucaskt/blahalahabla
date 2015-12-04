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

    url(r'^$', 'core.views.patients', name='index'),

    url(r'^patient/pilltaken$', 'core.views.pill_taken', name='pill_taken'),
    url(r'^patient/(?P<device_key>\S+)', 'core.views.get_info_for_patient', name='patient_info'),

    url(r'^doctorview/patients/$', 'core.views.patients', name='patients'),
    url(r'^doctorview/add_patient/$', 'core.views.add_patient', name='add_patient'),
    url(r'^doctorview/add_treatment/(?P<patient_pk>\d+)$', 'core.views.add_treatment', name='add_treatment'),

    url(r'^doctorview/patient/(?P<patient_pk>\d+)$', 'core.views.patient', name='patient'),
    url(r'^doctorview/scoreboard$', 'core.views.scoreboard', name='scoreboard'),
]
