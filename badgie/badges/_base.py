_BADGES = {}


def register_badge(klass):
    assert klass.name not in _BADGES
    _BADGES[klass.name] = klass
    return klass


def register_badges(badges):
    for token, badge in badges.items():
        assert token not in _BADGES
        _BADGES[token] = badge


def get_badge(token):
    assert _BADGES[token]
