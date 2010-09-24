# -*- coding: utf-8 -*-
#!/usr/bin/env python2.5
import urllib
import urllib2
import time
import md5

class OpenTaobao:
    def __init__(self,app_key,sercet_code):
        self.app_key = app_key
        self.sercet_code = sercet_code
    def get_time(self):
        t = time.localtime()
        return time.strftime('%Y-%m-%d %X', t)
    def get_sign(self,params):
        params.update({'app_key':self.app_key,'timestamp':self.get_time(),'v':'2.0'})
        src = self.sercet_code + ''.join(["%s%s" % (k, v) for k, v in sorted(params.iteritems())])
        return md5.new(src).hexdigest().upper()
    def get_result(self,params):
        params['sign'] = self.get_sign(params)
        form_data = urllib.urlencode(params)
        return urllib2.urlopen('http://gw.api.taobao.com/router/rest', form_data).read()




