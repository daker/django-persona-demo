# -*- coding: utf-8 -*-

# Copyright 2013, Adnane Belmadiaf <adnane002@gmail.com>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('demo.urls')),
    (r'^browserid/', include('django_browserid.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.STATIC_SERVE:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            dict(
                document_root=settings.MEDIA_ROOT,
                show_indexes=True
            )
        ),
        (r'^(robots.txt)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
        (r'^(opensearch.xml)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

