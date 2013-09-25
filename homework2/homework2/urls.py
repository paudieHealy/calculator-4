from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('calculator.urls')),
	url(r'^calculator/show_calculator$', include('calculator.urls')),
    # Examples:
    # url(r'^$', 'homework2.views.home', name='home'),
    # url(r'^homework2/', include('homework2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
