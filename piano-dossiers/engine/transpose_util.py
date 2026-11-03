"""Transpone notas de Do mayor a Fa mayor (una 4a justa hacia arriba), diatonicamente."""
LETTER_MAP = {'C':'F','D':'G','E':'A','F':'Bb','G':'C','A':'D','B':'E'}
OCTAVE_BUMP = {'C':0,'D':0,'E':0,'F':0,'G':1,'A':1,'B':1}

def transpose_pitch(p):
    letter = p[0]
    rest = p[1:]
    acc = ''
    if rest and rest[0] in ('#','b'):
        acc = rest[0]
        rest = rest[1:]
    octv = int(rest)
    new_letter_full = LETTER_MAP[letter]  # may be 2 chars e.g. 'Bb'
    new_octv = octv + OCTAVE_BUMP[letter]
    return f'{new_letter_full}{new_octv}'

if __name__ == '__main__':
    tests = ['C4','D4','E4','F4','G4','A4','B4','C5','G2','C3','F2']
    for t in tests:
        print(t, '->', transpose_pitch(t))
