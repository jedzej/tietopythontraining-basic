n = int(input())
whole_range = set()
for x in range(n):
    whole_range.add(str(x + 1))
read_data = True
beatrice_guess_entries = []
while read_data:
    beatrice_entry = input().split(' ')
    if beatrice_entry[0] == "NO" or beatrice_entry[0] == "YES":
        beatrice_guess_entries.extend(beatrice_entry)
    elif beatrice_entry[0] == "HELP":
        read_data = False
    else:
        beatrice_guess_entries.append(set(beatrice_entry))

set_ok = {}
set_nok = {}
for x in range(0, len(beatrice_guess_entries), 2):
    if beatrice_guess_entries[x + 1] == "YES":
        if set_ok == {}:
            set_ok = beatrice_guess_entries[x]
        else:
            set_ok = set_ok & beatrice_guess_entries[x]
    elif beatrice_guess_entries[(x + 1)] == "NO":
        if set_nok == {}:
            set_nok = beatrice_guess_entries[x]
        else:
            set_nok = set_nok | beatrice_guess_entries[x]
if set_ok != {}:
    if set_nok != {}:
        set_ok = set_ok - set_nok
else:
    if set_nok != {}:
        set_ok = whole_range - set_nok
    else:
        set_ok = whole_range

set_ok = sorted(set_ok, reverse=False)
print(' '.join(set_ok))
