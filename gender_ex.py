import re

def gegendert(wort):
    gender_pattern = re.compile('[a-zA-Z]+[*_:I][a-zA-Z]+')
    return not gender_pattern.match(wort) is None

def entgendere(wort):
    mittlerer_wortteil = wort[1:-1]
    entgendert = mittlerer_wortteil.replace('*', '')
    entgendert = entgendert.replace('_', '')
    entgendert = entgendert.replace(':', '')
    entgendert = entgendert.replace('I', 'i')
    return wort[0] + entgendert + wort[-1]

def gender_ex(text):
    entgenderter_text = ''
    wortliste = text.split()
    for wort in wortliste:
        if gegendert(wort):
            entgenderter_text += entgendere(wort)
        else:
            entgenderter_text += wort
        entgenderter_text += ' '
    return entgenderter_text
