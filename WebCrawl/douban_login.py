# encoding: utf-8

import requests
from HTMLParser import HTMLParser

class DoubanClient(object):
    def __init__(self):
        object.__init__(self)
        # headers
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                   'Origin': 'https://www.douban.com'
                   }
        #create a session
        self.session = requests.Session()
        self.session.headers.update(headers)

    def login(self, username, password,
              source='None',
              redir='http://www.douban.com',
              login='登录'):
        url = 'https://www.douban.com/accounts/login'
        r = self.session.get(url)
        (captcha_id, captcha_url) = _get_captcha(r.content)
        if(captcha_id):
            print(captcha_id)
            captcha_solution = raw_input("please input solution for [%s]" % captcha_url)
            print(captcha_solution)

        data = {'source': source,
                'redir': redir,
                'form_email': username,
                'form_password': password,
                'captcha_solution': captcha_solution,
                'captcha_id': captcha_id,
                'login': login
                 }
        # if captcha_id:
        #     data['captcha_id'] = captcha_id
        #     data['captcha_solution'] = captcha_solution

        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                    'Cookie': 'bid=2wsTdWEP-WA; gr_user_id=8772ef96-d20c-43ca-9d09-1b065baf7622; viewed="6113960_2016457_25809330_1058576"; _vwo_uuid_v2=862A91DAEAAA04A22ABA1BAB8B33CA01|aea65710897674facefa17d7e18a59b1; ll="108288"; ps=y; ct=y; __utmt=1; ue="leexw1994@gmail.com"; push_noty_num=0; push_doumail_num=0; __utma=30149280.1123973342.1471766588.1480473982.1480485663.6; __utmb=30149280.18.10.1480485663; __utmc=30149280; __utmz=30149280.1480485663.6.4.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.15447; ap=1; as="https://www.douban.com/people/154472688/"',
                    'Host': 'accounts.douban.com',
                    'Referer': 'https://www.douban.com/accounts/login',
                    'Upgrade-Insecure-Requests': 1
                   }

        r = self.session.post(url, data=data, headers=headers)
        print(self.session.cookies.items())

    def edit_signature(self, username, signature):
        url = 'https://www.douban.com/people/%s/' % username
        r = self.session.get(url)
        ck = _get_ck(r.content)

        url_sig = 'https://www.douban.com/j/people/%s/edit_signature' % username
        headers = {'Referer':url,
                   'Host': 'www.douban.com',
                   }
        data = {'ck': ck,
                'signature': signature
                }
        r_sig = requests.post(url, data=data, headers=headers)
        print(r_sig.content)


def _attr(attrs, attrname):
    for attr in attrs:
        if(attr[0] == attrname):
            return attr[1]
    return None


def _get_captcha(content):

    class CaptchaParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.captcha_id = None
            self.captcha_url = None

        def handle_starttag(self, tag, attrs):
            if tag == 'input' and _attr(attrs, 'type') == 'hidden' and _attr(attrs, 'name') == 'captcha-id':
                self.captcha_id = _attr(attrs, 'value')
            if tag == 'img' and _attr(attrs, 'id') == 'captcha_image' and _attr(attrs, 'class') == 'captcha_image':
                self.captcha_url = _attr(attrs, 'src')

    p = CaptchaParser()
    p.feed(content)
    return p.captcha_id, p.captcha_url

def _get_ck(content):

    class CKParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.ck = None

        def handle_starttag(self, tag, attrs):
            if tag == 'input' and _attr(attrs, 'type') == 'hidden' and _attr(attrs, 'name') == 'ck':
                self.ck = _attr(attrs, 'value')

    p = CKParser()
    p.feed(content)
    return p.ck

if __name__ == '__main__':
    c = DoubanClient()
    c.login('leexw1994@gmail.com', 'meng8023bei.')
    c.edit_signature('CowCoder', "test222")