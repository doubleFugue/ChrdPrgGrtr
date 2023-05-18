
# This module contains three dictionaries that will be used in generator.py

# Dictionary containing lists of the basic triad chords of every (major) scale
chordsTriads = {
    'A': ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim'],
    'Bb': ['Bb', 'Cm', 'Dm', 'Eb', 'F', 'Gm', 'Adim'],
    'B': ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'],
    'C': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'],
    'C#': ['C#', 'D#m', 'E#m', 'F#', 'G#', 'A#m', 'B#dim'],
    'Db': ['Db', 'Ebm', 'Fm', 'Gb', 'Ab', 'Bbm', 'Cdim'],
    'D': ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'],
    'Eb': ['Eb', 'Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Ddim'],
    'E': ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'],
    'F': ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'],
    'F#': ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'E#dim'],
    'Gb': ['Gb', 'Abm', 'Bbm', 'Cb', 'Db', 'Ebm', 'Fdim'],
    'G': ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'],
    'Ab': ['Ab', 'Bbm', 'Cm', 'Db', 'Eb', 'Fm', 'Gdim']
}

# Dictionary containing lists of the seventh chords of every (major) scale
chordsSevenths = {
    'A': ['Amaj7', 'Bmin7', 'C#min7', 'Dmaj7', 'E7', 'F#min7', 'G#min7b5'],
    'Bb': ['Bbmaj7', 'Cmin7', 'Dmin7', 'Ebmaj7', 'F7', 'Gmin7', 'Amin7b5'],
    'B': ['Bmaj7', 'C#min7', 'D#min7', 'Emaj7', 'F#7', 'G#min7', 'A#min7b5'],
    'C': ['Cmaj7', 'Dmin7', 'Emin7', 'Fmaj7', 'G7', 'Amin7', 'Bmin7b5'],
    'C#': ['C#maj7', 'D#min7', 'E#min7', 'F#maj7', 'G#7', 'A#min7', 'B#min7b5'],
    'Db': ['Dbmaj7', 'Ebmin7', 'Fmin7', 'Gbmaj7', 'Ab7', 'Bbmin7', 'Cmin7b5'],
    'D': ['Dmaj7', 'Emin7', 'F#min7', 'Gmaj7', 'A7', 'Bmin7', 'C#min7b5'],
    'Eb': ['Ebmaj7', 'Fmin7', 'Gmin7', 'Abmaj7', 'Bb7', 'Cmin7', 'Dmin7b5'],
    'E': ['Emaj7', 'F#min7', 'G#min7', 'Amaj7', 'B7', 'C#min7', 'D#min7b5'],
    'F': ['Fmaj7', 'Gmin7', 'Amin7', 'Bbmaj7', 'C7', 'Dmin7', 'Emin7b5'],
    'F#': ['F#maj7', 'G#min7', 'A#min7', 'Bmaj7', 'C#7', 'D#min7', 'E#min7b5'],
    'Gb': ['Gbmaj7', 'Abmin7', 'Bbmin7', 'Cbmaj7', 'Db7', 'Ebmin7', 'Fmin7b5'],
    'G': ['Gmaj7', 'Amin7', 'Bmin7', 'Cmaj7', 'D7', 'Emin7', 'F#min7b5'],
    'Ab': ['Abmaj7', 'Bbmin7', 'Cmin7', 'Dbmaj7', 'Eb7', 'Fmin7', 'Gmin7b5']
}

# Dictionary containing lists of the ninth chords of every (major) scale
chordsNinths = {
    'A': ['Amaj9', 'Bmin9', 'C#min7b9', 'Dmaj9', 'E9', 'F#min9', 'G#min7b5b9'],
    'Bb': ['Bbmaj9', 'Cmin9', 'Dmin7b9', 'Ebmaj9', 'F9', 'Gmin9', 'Amin7b5b9'],
    'B': ['Bmaj9', 'C#min9', 'D#min7b9', 'Emaj9', 'F#9', 'G#min9', 'A#min7b5b9'],
    'C': ['Cmaj9', 'Dmin9', 'Emin7b9', 'Fmaj9', 'G9', 'Amin9', 'Bmin7b5b9'],
    'C#': ['C#maj9', 'D#min9', 'E#min7b9', 'F#maj9', 'G#9', 'A#min9', 'B#min7b5b9'],
    'Db': ['Dbmaj9', 'Ebmin9', 'Fmin7b9', 'Gbmaj9', 'Ab9', 'Bbmin9', 'Cmin7b5b9'],
    'D': ['Dmaj9', 'Emin9', 'F#min7b9', 'Gmaj9', 'A9', 'Bmin9', 'C#min7b5b9'],
    'Eb': ['Ebmaj9', 'Fmin9', 'Gmin7b9', 'Abmaj9', 'Bb9', 'Cmin9', 'Dmin7b5b9'],
    'E': ['Emaj9', 'F#min9', 'G#min7b9', 'Amaj9', 'B9', 'C#min9', 'D#min7b5b9'],
    'F': ['Fmaj9', 'Gmin9', 'Amin7b9', 'Bbmaj9', 'C9', 'Dmin9', 'Emin7b5b9'],
    'F#': ['F#maj9', 'G#min9', 'A#min7b9', 'Bmaj9', 'C#9', 'D#min9', 'E#min7b5b9'],
    'Gb': ['Gbmaj9', 'Abmin9', 'Bbmin7b9', 'Cbmaj9', 'Db9', 'Ebmin9', 'Fmin7b5b9'],
    'G': ['Gmaj9', 'Amin9', 'Bmin7b9', 'Cmaj9', 'D9', 'Emin9', 'F#min7b5b9'],
    'Ab': ['Abmaj9', 'Bbmin9', 'Cmin7b9', 'Dbmaj9', 'Eb9', 'Fmin9', 'Gmin7b5b9']
}
