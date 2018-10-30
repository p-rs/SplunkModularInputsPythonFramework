from requests.auth import AuthBase
import hmac
import base64
import hashlib
import urlparse
import urllib


'''
    Add your custom auth handler class to this module
'''


class MyEncryptedCredentialsAuthHandler(AuthBase):
    def __init__(self, **args):
        # setup any auth-related data here
        # self.username = args['username']
        # self.password = args['password']
        pass

    def __call__(self, r):
        # modify and return the request
        # r.headers['foouser'] = self.username
        # r.headers['foopass'] = self.password
        return r


# template
class MyCustomAuth(AuthBase):
    def __init__(self, **args):
        # setup any auth-related data here
        # self.username = args['username']
        # self.password = args['password']
        pass

    def __call__(self, r):
        # modify and return the request
        # r.headers['foouser'] = self.username
        # r.headers['foopass'] = self.password
        return r


class MyCustomOpsViewAuth(AuthBase):
    def __init__(self, **args):
        self.username = args['username']
        self.password = args['password']
        self.url = args['url']
        pass

    def __call__(self, r):

        # issue a PUT request (not a get) to the url from self.url
        payload = {'username': self.username, 'password': self.password}
        auth_response = requests.put(self.url,
                                     params=payload,
                                     verify='false')
        # get the auth token from the auth_response.
        # I have no idea where this is in your response
        tokenstring = "mytoken"
        headers = {'X-Opsview-Username': self.username,
                   'X-Opsview-Token': tokenstring}

        r.headers = headers
        return r


'''
    Example of adding a client certificate
'''


class MyAzureCertAuthHAndler(AuthBase):
    def __init__(self, **args):
        self.cert = args['certPath']
        pass

    def __call__(self, r):
        r.cert = self.cert
        return r

# example of adding a client certificate


class GoogleBigQueryCertAuthHandler(AuthBase):
    def __init__(self, **args):
        self.cert = args['certPath']
        pass

    def __call__(self, r):
        r.cert = self.cert
        return r

# cloudstack auth example


class CloudstackAuth(AuthBase):
    def __init__(self, **args):
        # setup any auth-related data here
        self.apikey = args['apikey']
        self.secretkey = args['secretkey']
        pass

    def __call__(self, r):
        # modify and return the request

        parsed = urlparse.urlparse(r.url)
        url = parsed.geturl().split('?', 1)[0]
        url_params = urlparse.parse_qs(parsed.query)

        # normalize the list value
        for param in url_params:
            url_params[param] = url_params[param][0]

        url_params['apikey'] = self.apikey

        keys = sorted(url_params.keys())

        sig_params = []
        for k in keys:
            sig_params.append(
                k + '=' + urllib.quote_plus(url_params[k]).replace("+", "%20"))

        query = '&'.join(sig_params)

        signature = base64.b64encode(hmac.new(
            self.secretkey,
            msg=query.lower(),
            digestmod=hashlib.sha1
        ).digest())

        query += '&signature=' + urllib.quote_plus(signature)

        r.url = url + '?' + query

        return r
