from django_hosts import patterns, host
host_patterns = patterns('',
    host(r'bp', 'bp.urls', name='bp'),
    host(r'api', 'api.urls', name='api'),
    host(r'news', 'news.urls', name='news'),
    host(r'forum', 'forum.urls', name='forum'),
)