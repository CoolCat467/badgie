from badgie import tokens

assert isinstance(tokens.TOKENS, list)
for token in tokens.TOKENS:
    assert isinstance(token, tuple)
    assert not token[0].startswith("_")
    assert token[0] == token[1].upper()
