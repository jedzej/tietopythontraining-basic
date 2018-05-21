def comma_code(strings):
    string_coma = ", ".join(s for s in strings[:-1]) + ', and ' + strings[-1]
    return string_coma


string_in = input()
lista_string = string_in.split()
print(comma_code(lista_string))
