#!/usr/bin/env python
# encoding: utf-8

import falcon
import logging

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class WebResource:
    def __init__(self):
        self.logger = logging.getLogger('wrapweb.'+__name__)

    def on_get(self, req, resp):
        """Handles GET requests"""
        url = req.params.get('url', '')
        self.logger.error(req.params)
        self.logger.info(url)

        body_style = "overflow:hidden; margin:0px; padding:0px; "
        iframe_style = 'width:100%; height:100%; border:0px; margin:0px; padding:0px;'

        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        resp.body= ('<html>'
                     '<head>'
                     '  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
                     '</head>'
                     '<body style="%s">'
                     '  <iframe src="%s" style="%s">'
                     '  </iframe>'
                     '</body>'
                     '</html>' % (body_style, url, iframe_style))

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
web = WebResource()

# things will handle all requests to the '/wrapweb' URL path
app.add_route('/wrapweb', web)
