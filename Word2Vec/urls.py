"""Word2Vec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from api import views
from rest_framework import routers
router=routers.DefaultRouter()
#router.register(r'stat/segment_stat/*$',views.segment_stat,'SegmentStat')
router.register(r'stat',views.BasicStats,'BasicStats')
router.register(r'run_task',views.RunTask,'RunTask')
router.register(r'add_custom_metric',views.AddCustomMetric,'AddCustomMetric')
router.register(r'action_measurer',views.ActionMeasurer,'ActionMeasurer')
router.register(r'diagram_stat',views.DiagBasicStats,'DiagBasicStats')
router.register(r'add_segment',views.AddSegment,'AddSegment')
urlpatterns = [
    url(r'^api/stat/segment_stat/*$', views.segment_stat, name='segment_stat'),
    url(r'^api/get_uniq_vals/', views.get_uniq_vals, name='get_uniq_vals'),
    url(r'^api/reload_adstat/', views.reload_adstat, name='reload_adstat'),
    url(r'^api/celery_run_task/$', views.celery_run_task, name='celery_run_task'),
    url(r'^api/configurator/', views.configurator, name='configurator'),
    url(r'^api/pp_tsv_log/', views.pp_tsv_log, name='pp_tsv_log'),
    url(r'^api/download_tsv_log/(?P<file>.+)/', views.download_tsv_log, name='download_tsv_log'),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'api/',include(router.urls)),

]
