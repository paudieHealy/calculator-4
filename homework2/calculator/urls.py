from django.conf.urls import patterns, include, url

#calculator.urls

# Generates the routes for the Controller.
# Typical use is a regular expression for a URL pattern, and then the
# action to call to process requests for that URL pattern.
urlpatterns = patterns('',
    url(r'^$', 'calculator.views.show_calculator'),
)
