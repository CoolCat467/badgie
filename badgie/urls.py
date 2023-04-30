from urllib.parse import urlencode, urlparse


def add_to_query(url: str, params: dict[str, str]):
    parsed = urlparse(url)

    _params = {}
    for param in parsed.query.split("&"):
        try:
            key, value = param.split("=")
            _params[key] = value
        except ValueError:
            pass

    _params.update(params)

    query = urlencode(_params)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{query}"
