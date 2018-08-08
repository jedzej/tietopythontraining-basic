import re


def regex_strip(strng, strip='\s'):
    """
    Examples
    --------
    regex_strip('  qq ryq   ')              # 'qq ryq'
    regex_strip('qq ryq na patyq','yq')     # ' ryq na pat'
    regex_strip('qq ryq na patyq','yqr')    # ' ryq na pat'
    regex_strip('qq ryq na patyq','yqr ')   # 'na pat'
    """

    regex = re.compile(r'(^[' + strip + ']*)|([' + strip + ']*$)')
    return regex.sub('', strng)
