import re
import copy
import enum


class PostalCodeKind(enum.Enum):
    POLISH = 1,
    AMERICAN = 2


def strip(text: str, chars: str=None) -> str:
    if chars is None:
        chars = r'\s'

    regex = re.compile('^([{0}])*(.*?)([{0}])*$'.format(chars))
    match = regex.search(text)
    if match is None:
        return copy.copy(text)

    return match.group(2)


def is_password_strong(text: str) -> bool:
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})')
    match = regex.match(text)

    return match is not None


def _is_local_part_valid(local_part: str) -> bool:
    local_part_regex = re.compile(r'''
        (?=^.{1,64}$)
        ^[^\.][A-Za-z0-9!#\$%&'\*\+-/=\?\^_`{\|}~\.]+[^\.]$''', re.VERBOSE)

    return local_part_regex.match(local_part) is not None


def _is_domain_valid(domain: str) -> bool:
    domain_regex = re.compile(r'''
        (?=^.{,255}$)
        ^[A-Za-z0-9-]{1,63}
        (\.[A-Za-z0-9-]{1,63})+
        $''', re.VERBOSE)

    return domain_regex.match(domain) is not None


def is_valid_email_address(email_address: str) -> bool:
    regex = re.compile(r'^(?P<local_part>.*?)@(?P<domain>.*)$')
    match = regex.match(email_address)
    if match is None:
        return False

    local_part = match.group('local_part')
    domain = match.group('domain')

    return _is_local_part_valid(local_part) and _is_domain_valid(domain)


def is_valid_postal_code(
        postal_code: str,
        kind: PostalCodeKind=PostalCodeKind.POLISH) -> bool:

    if kind == PostalCodeKind.POLISH:
        polish_regex = re.compile(r'^\d{2}-\d{3}$')
        return polish_regex.match(postal_code) is not None

    if kind == PostalCodeKind.AMERICAN:
        american_regex = re.compile(r'^(\d{4}|\d{5}-\d{4})$')
        return american_regex.match(postal_code) is not None

    raise ValueError('Incorrect postal code kind')


def is_valid_mobile_phone_number(mobile_phone_number: str) -> bool:
    mobile_regex = re.compile(r'''^
        (?:(\+\d{2}|00\d{2})\s)?
        \d{3}
        (?:-|\s)?
        \d{3}
        (?:-|\s)?
        \d{3}
        $''', re.VERBOSE)

    return mobile_regex.match(mobile_phone_number) is not None
