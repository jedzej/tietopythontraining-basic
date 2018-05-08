# Remove ALL spaces in a strings, even between words:

import re
sentence = re.sub(r"\s+", "", sentence, flags=re.UNICODE)

# Remove spaces in the BEGINNING of a string:

import re
sentence = re.sub(r"^\s+", "", sentence, flags=re.UNICODE)

# Remove spaces in the END of a string:

import re
sentence = re.sub(r"\s+$", "", sentence, flags=re.UNICODE)

# Remove spaces both in the BEGINNING and in the END of a string:

import re
sentence = re.sub("^\s+|\s+$", "", sentence, flags=re.UNICODE)

# Remove ONLY DUPLICATE spaces:

import re
sentence = " ".join(re.split("\s+", sentence, flags=re.UNICODE))


# symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None