import re


def regex_strip(str, strip='\s'):
    """
    Examples
    --------
    regex_strip('  qq ryq   ')
    regex_strip('qq ryq na patyq','yq')
    regex_strip('qq ryq na patyq','yqr')
    regex_strip('qq ryq na patyq','yqr ')
    """
    regex = re.compile(r'(^[' + strip + ']*)|([' + strip + ']*$)')
    return regex.sub('', str)
