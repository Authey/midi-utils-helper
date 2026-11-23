"""Fingerstyle guitar arrangement from Notes/点点糖指弹版 (two pages).

The tablature is recorded as beat/string/fret events. String 1 is high E.
Slide, hammer-on and pull-off targets are approximated by softer re-plucks;
standard General MIDI cannot reproduce every guitar articulation exactly.
"""
from pathlib import Path
from midiutil import MIDIFile

TEMPO = 65
OPEN_STRINGS = (40, 45, 50, 55, 59, 64)  # standard tuning, low E first

# Each token is beat=string.fret[,string.fret...]; times are quarter-note
# beats within a 4/4 bar. Simultaneous notes belong to different strings.
INTRO = [
    '0=6.3 .5=4.0 1=2.0 1.5=4.0 2=6.2,3.2 2.5=4.0 3=2.0 3.5=4.0',
    '0=6.0,3.0 .5=4.2 1=4.4 1.5=3.0 2=4.4 2.5=4.2 3=4.0',
    '0=5.3 .5=4.2 1=2.3 1.5=4.2 2=5.5 2.5=4.4 3=2.5 3.5=3.0',
    '0=6.3 .5=4.0 1=3.2 1.5=2.0 2=4.0 2.5=3.2 3=4.0 3.5=3.2',
    '0=6.3 .5=4.0 1=2.0 1.5=4.0 2=6.2,3.2 2.5=4.0 3=2.0 3.5=4.0',
    '0=6.0,3.0 .5=4.2 1=4.4 1.5=3.0 2=4.4 2.5=4.2 3=4.0',
    '0=5.3 .5=4.2 1=2.3 1.5=4.2 2=5.5 2.5=4.4 3=2.5 3.5=4.0',
    '0=6.3 .5=4.0 1=3.2 1.5=2.0 2=2.0',
]
# Main verse: the upper-string notes carry the song's melody, while the
# lower-string notes supply the accompaniment. Beat fractions represent the
# sixteenth-note rhythms shown in the tablature.
VERSE = [
    '0=6.3 .5=2.0 .75=4.0 1=2.0 1.25=2.0 1.5=4.0 1.75=2.0 2=6.2,3.2 3=2.0 3.5=3.2',
    '0=6.0,3.0 .5=4.2 1=4.4 1.5=3.0 2=4.4 2.5=4.2 3=4.0 3.5=2.3 3.75=2.3',
    '0=5.3,1.0 .5=2.3 .75=1.0 1.25=2.3 2=4.0 2.5=3.2 3=3.2 3.5=2.3',
    '0=6.3 .5=2.3 .75=2.0 1=3.2 1.5=2.0 2=4.0 2.5=3.2 3=4.0 3.5=3.2',
    '0=6.3 .5=2.0 .75=2.0 1=2.0 1.5=4.0 1.75=2.0 2=6.2 2.25=3.2 3=2.0 3.5=3.2 3.75=3.0',
    '0=6.0 .5=4.2 1=4.4 1.5=3.0 2=4.4 2.5=4.2 3=4.0 3.5=3.0 3.75=3.0',
    '0=5.3,3.2 .5=3.0 .75=4.2 1=3.2 1.25=3.0 1.5=4.0 1.75=4.0 2.5=3.2 3=3.0 3.5=3.0',
    '0=6.0,3.2 .5=3.0 1=4.2 1.5=3.0 2=1.0 3.5=2.3 3.75=2.3',
]
CHORUS = [
    '0=5.3,1.3 .5=4.2 1=3.0 1.5=1.3 1.75=1.3 2=5.5,1.5 2.5=1.0 3=3.0 3.5=1.0 3.75=1.0',
    '0=6.0,1.7 .5=1.2 1=1.2 1.5=1.0 1.75=1.0 2=4.0 2.25=2.3 2.5=1.0 3=3.2 3.5=1.0 3.75=2.3',
    '0=5.3,1.0 .5=2.3 .75=1.3 1=1.3 1.75=1.3 2=4.0,1.3 2.25=1.5 2.75=1.5 3=1.5 3.5=1.7',
    '0=6.3 .5=2.3 .75=2.0 1=3.2 1.5=4.0 2=3.2 2.5=2.0 3=1.3 3.5=2.3 3.75=2.3',
    '0=5.3,1.3 .5=4.2 1=1.3 1.333333=1.0 1.666667=1.0 2=4.0,1.5 2.75=1.5 3=1.0 3.25=1.0 3.5=1.0',
    '0=6.0,1.7 .5=1.2 1=1.2 1.5=1.0 1.75=2.3 2=4.0 2.25=1.0 3=3.2 3.5=1.0 3.75=2.3',
    '0=5.3,1.0 .5=2.3 .75=1.3 1.25=1.0 1.5=1.0 1.75=4.0 2=2.3 2.5=3.2 3=3.2 3.5=3.0',
    '0=6.0 .5=4.2 1=3.0 1.5=2.0 2=1.0',
]
BRIDGE_TO_SOLO = [
    '0=6.3 .5=2.0 .75=2.0 1=2.0 1.5=2.0 1.75=2.0 2=6.2 2.25=3.2 3=2.0 3.5=3.2',
    '0=6.0,3.0 .5=4.2 1=4.4 1.5=3.0 2=4.4 2.5=4.2 3=4.0 3.5=2.3 3.75=1.0',
    '0=5.3 .5=2.3 .75=1.0 1=1.0 1.25=1.0 1.75=2.3 2=4.0 2.5=3.2 3=2.3 3.5=2.3',
    '0=6.3,1.0 .5=2.0 1=3.2 1.5=2.0 2=4.0 2.5=3.2 3=4.0 3.5=3.2',
    '0=6.3 .5=2.0 .75=2.0 1=2.0 1.5=2.0 1.75=2.0 2=6.2 2.25=3.2 3=2.0 3.5=3.2 3.75=3.0',
    '0=6.0,3.2 .25=3.0 .5=3.0 1=4.2 1.25=4.4 1.5=3.0 2=4.4 2.25=4.2 2.5=3.0 3=2.0 3.5=3.0 3.75=3.0',
    '0=5.3,3.2 .25=3.0 1=4.2 1.5=3.0 2=4.0 2.5=3.0 2.75=3.0 3=3.2 3.5=4.2 3.75=3.0',
]
INTERLUDE = [
    '0=6.0 .5=4.2 1=3.0 1.5=2.0 2=6.0,5.2,4.2,3.0,2.0,1.0 2.5=3.2 2.75=3.4 3=2.5 3.25=2.3 3.5=2.5 3.75=2.3',
    '0=5.3,4.2 .5=5.3 1=4.2 1.5=3.0 1.75=3.2 2=3.2,4.0 3=2.0 3.5=2.3',
    '0=6.3,2.0 .333333=2.3 .666667=2.0 1=2.0 1.5=3.0 2=4.0 2.5=6.3 2.75=3.2 3=3.4 3.25=2.5 3.5=2.3 3.666667=2.5 3.833333=2.3',
    '0=5.3,4.2 .5=5.3 1=4.2 1.5=3.0 1.75=3.2 2=3.2,4.0 3=2.0 3.5=2.3',
    '0=6.3,2.0 .333333=2.3 .666667=2.0 1=2.0 1.5=3.0 2=4.0 2.5=6.3 3=4.0 3.5=1.7 3.75=1.5',
    '0=5.3,1.5 .5=1.3 1=2.0 1.5=3.0 2=4.0,1.5 2.75=1.5 3=1.7 3.5=1.10',
    '0=6.0,1.7 .125=1.10 .25=1.7 .375=1.10 .5=1.7 1=2.0 1.5=3.0 2=6.0 2.5=1.12 3=1.12 3.5=1.12 3.75=1.5',
    '0=5.3,1.5 .5=3.0 1=2.0 1.5=1.3 1.75=1.3 2=4.0,1.5 2.5=1.3 3=1.5 3.5=1.7',
    '0=6.0,1.7 .5=1.0 1=2.0 1.5=3.0 2=1.12,2.12,3.12 3.5=2.3 3.75=2.3',
]
ENDING = [
    '0=6.0 .5=4.2 1=3.0 1.5=2.0 2=6.0,5.2,4.2,3.0,2.0,1.0 2.5=4.2 3=3.0 3.5=2.3 3.75=2.3',
    '0=5.3,1.3 .5=4.2 1=3.0 1.5=1.3 1.75=1.3 2=5.5,1.5 2.25=1.0 2.5=1.0 3=3.0 3.5=1.0 3.75=1.0',
    '0=6.0,1.7 .5=1.2 1=1.2 1.5=1.0 1.75=1.0 2=4.0 2.25=2.3 2.5=1.0 3=3.2 3.5=1.0 3.75=2.3',
    '0=5.3,1.0 .5=2.3 1=1.0 1.5=2.3 2=3.2 2.5=1.3 3=1.3 3.5=1.5',
    '0=6.3 .5=2.3 .75=2.0 1=3.2 1.5=4.0 2=3.2 2.5=2.0 3=1.3 3.5=2.3 3.75=2.3',
    '0=5.3,1.3 .5=4.2 1=3.0 1.5=1.3 1.75=1.3 2=5.5,1.5 2.25=1.0 2.5=1.0 3=3.0 3.5=1.0 3.75=1.0',
    '0=6.0,1.7 .5=1.2 1=1.2 1.5=1.0 1.75=1.0 2=4.0 2.25=2.3 2.5=1.0 3=3.2 3.5=1.0 3.75=2.3',
    '0=5.3,1.0 .5=2.3 1=3.0 1.5=4.2 2=5.5 2.5=4.4 3=2.5 3.5=3.0',
    '0=6.0,3.0 .5=4.2 1=3.0 1.5=2.0 2=1.0',
    VERSE[0], VERSE[1], VERSE[2], VERSE[3], VERSE[4],
    '0=6.0,3.0 .5=4.2 1=4.4 1.5=3.0 2=4.4 2.5=4.2 3=4.0 3.5=3.2',
    '0=5.3,3.0 .5=4.2 1=3.0 1.5=2.3 2=5.3 2.25=5.5 2.5=4.4 3=2.5 3.5=3.0',
    '0=6.3,3.0 .5=4.0 1=3.2 1.5=2.0 2=1.3',
]
# Repeat starts at the chorus on page 1 and ends at the interlude on page 2.
# Its first ending is the bridge into the interlude; the second takes ENDING.
BARS = INTRO + VERSE + CHORUS + BRIDGE_TO_SOLO + INTERLUDE + CHORUS + ENDING
INTERLUDE_START = len(INTRO) + len(VERSE) + len(CHORUS) + len(BRIDGE_TO_SOLO)
INTERLUDE_VELOCITY_BOOST = 15


def guitar_notes():
    """Read the tab events as (time, string, pitch, velocity)."""
    for bar, measure in enumerate(BARS):
        for token in measure.split():
            beat_text, frets = token.split('=')
            beat = float(beat_text)
            if not 0 <= beat < 4:
                raise ValueError(f'Invalid beat in measure {bar + 1}: {beat}')
            for entry in frets.split(','):
                string, fret = map(int, entry.split('.'))
                if not 1 <= string <= 6 or not 0 <= fret <= 24:
                    raise ValueError(f'Invalid tab in measure {bar + 1}: {entry}')
                velocity = 82 if string >= 5 else 90
                if INTERLUDE_START <= bar < INTERLUDE_START + len(INTERLUDE):
                    velocity = min(127, velocity + INTERLUDE_VELOCITY_BOOST)
                yield bar * 4 + beat, string, OPEN_STRINGS[6 - string] + fret, velocity


class AnheBridge:
    def __init__(self):
        self.name = str(Path(__file__).resolve().parent / '安和桥.midi')

    def generator(self):
        midi = MIDIFile(1)
        midi.addTempo(0, 0, TEMPO)
        # GM steel-string guitar; separate channels let each string ring.
        for channel in range(6):
            midi.addProgramChange(0, channel, 0, 25)
        notes = sorted(guitar_notes())
        for index, (start, string, pitch, velocity) in enumerate(notes):
            next_start = next((n[0] for n in notes[index + 1:] if n[1] == string), None)
            duration = min(1.5, next_start - start) if next_start is not None else 1.5
            if duration <= 0:
                raise ValueError(f'Duplicate string {string} at beat {start}')
            midi.addNote(0, 6 - string, pitch, start, duration, velocity)
        with open(self.name, 'wb') as output:
            midi.writeFile(output)
        return self.name
