import urllib

def url_querystring(url, clean=False, raw=False):
    if clean:
        return {}
    url = urllib.parse.urlparse(url)
    result = urllib.parse.parse_qs(url.query)
    if not raw:
        # Flatten the list values by using the "first" (usually only) value.
        result = { k:v[0] for k,v in result.items() }
    return result

def url_with_query(url, clean=False, **kw):
    url = urllib.parse.urlparse(url)
    query = url_querystring(url, clean=clean, raw=True)

    for key, val in kw.items():
        if val is not None:
            query[key] = val
        else:
            try:
                del query[key]
            except KeyError:
                pass
    query = urllib.parse.urlencode(query, doseq=True)
    url = urllib.parse.urlunparse((url.scheme, url.netloc, url.path, url.params, query, url.fragment))
    return url