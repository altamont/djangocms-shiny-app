from django.conf.urls import url
from cms_shiny.views import ShinyAppListView, ShinyAppDetailView

urlpatterns = [
               url(r'^$', ShinyAppListView.as_view(), name='shiny_list'),
               url(r'^(?P<slug>[^/]+)/$', ShinyAppDetailView.as_view(), name='shiny_detail'),
               ]
