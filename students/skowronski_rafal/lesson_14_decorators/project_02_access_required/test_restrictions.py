from restrictions import AuthorizationError
import restrictions
import pytest


def test_restricted_print_on_access_granted(monkeypatch):
    monkeypatch.setattr('authorization.has_access', lambda: True)
    try:
        restrictions.restricted_print()
    except Exception:
        pytest.fail('Unexpected exception')


def test_restricted_print_on_access_denied(monkeypatch):
    monkeypatch.setattr('authorization.has_access', lambda: False)
    with pytest.raises(AuthorizationError):
        restrictions.restricted_print()
