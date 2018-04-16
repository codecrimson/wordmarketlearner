from urllib2 import Request, urlopen, URLError, HTTPError


def page_downloader(url):
    print("pageDownloader: %s" % url)
    req = Request(url)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print("pageDownloader HTTP error")
        print e.code
        print e.read()
        return None
    except URLError as e:
        print("pageDownloader URL error")
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
        return None
    else:
        html = response.read()
        return html
