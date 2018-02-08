from django.conf.urls import url

from .views import (
    
    ClientViewSet,
    ClientDetailsViewSet,

    )


urlpatterns = [

    url(
        r'^api/v1/client/(?P<pk>[0-9]+)$',
        ClientDetailsViewSet.as_view(),
        name='get_delete_update_client'
    ),

    url(
        r'^api/v1/client/$',
        ClientViewSet.as_view(),
        name='get_post_client'
    ),

]