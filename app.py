#!/usr/bin/env python
# encoding: utf-8

import falcon
import logging
import base64

debug = False
_L = str
if debug:
    file_h = logging.FileHandler("log")
    logger = logging.getLogger('wrapweb.'+__name__)
    logger.addHandler(file_h)
    logger.setLevel(logging.DEBUG)
    _L = logger.debug

class WebResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        _L(req.params)
        b64url = req.params.get('url', '')
        _L(b64url)
        try:
            url = base64.b64decode(b64url)
        except:
            url = b64url
        _L("url:"+url)
        _L("UA"+req.user_agent)

        body_style = 'overflow:hidden; margin:0px; padding:0px;'
        iframe_style = 'width:100%; height:100%; border:0px; margin:0px; padding:0px;'

        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body= ( '<html>'
                     '<head>'
                     '  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
                     '  <meta name="viewport" content="width=device-width, initial-scale=1"/>'
                     '</head>'
                     '<body style="%s">'
                     '  <iframe src="%s" style="%s" seamless>'
                     '  </iframe>'
                     '</body>'
                     '</html>' % (body_style, url, iframe_style))


app = falcon.API()

web = WebResource()

app.add_route('/wrapweb', web)
