
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView

#The format_suffix_pattern allows us to specify the data format
# (raw json or even html) when we use the URLs.
# It appends the format to be used to every URL in the pattern.

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name = "details"),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)

