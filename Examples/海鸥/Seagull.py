"""《海鸥》吉他伴奏和主唱旋律，按 Notes 中的六线谱和简谱录入。

六线谱中的叉号按相应和弦的指型发音；数字是相对于变调夹的品位。
MIDI 无法完全表现扫弦、连音和吉他的自然衰减，这里用同时拨弦近似。
"""
from pathlib import Path

from midiutil import MIDIFile

TEMPO = 93  # 谱面标注的四分音符速度
CAPO = 2
BEATS_PER_BAR = 3  # 6/8：一个小节为三个四分音符
OPEN_STRINGS = (40, 45, 50, 55, 59, 64)  # 从六弦到一弦

# 从六弦到一弦；None 表示该弦不在和弦指型中。
CHORDS = {
    'G': (3, 2, 0, 0, 0, 3),
    'G5': (3, 2, 0, 0, 3, None),
    'Em7': (0, 2, 2, 0, 3, 0),
    'D/F#': (2, None, 0, 2, 3, 2),
    'C': (None, 3, 2, 0, 1, 0),
    'C/E': (0, 3, 2, 0, 1, 0),
    'Dadd11': (None, 5, 4, 0, 3, 0),
    'G/B': (None, 2, 0, 0, 0, 3),
    'Am': (None, 0, 2, 2, 1, 0),
    'Am7': (None, 0, 2, 0, 1, 0),
    'Dsus4': (None, None, 0, 2, 3, 3),
    'Dsus2': (None, None, 0, 2, 3, 0),
    'D': (None, None, 0, 2, 3, 2),
    'D7': (None, None, 0, 2, 1, 2),
    'Em/D': (None, None, 0, 0, 0, 0),
    'Em': (0, 2, 2, 0, 0, 0),
    'Gsus4': (3, 3, 0, 0, 1, 3),
    'Gadd9': (3, 2, 0, 2, 0, 3),
    'Cmaj7': (None, 3, 2, 0, 0, 0),
    'Em(3)': (None, None, 5, 4, 5, 3),
}

# Each item is (beat, string(s)); the chord supplies the fret for an X.
# A digit after a dot overrides the chord fingering for a numbered tab note.
PATTERNS = {
    'intro': '0:642 1.5:2.1,3 2.5:3',
    'held': '0:642 1.5:642',
    'verse': '0:642 1.5:642 2.5:3',
    'walk': '0:6 0.5:4 1:3 1.5:2 2:3 2.5:4',
    'arp': '0:5 0.5:4 1:3 1.5:2 2:3 2.5:4',
    'turn': '0:642 1.5:4 2:3 2.5:2',
    'chord': '0:642 1.5:642',
}


def bar(chord, pattern='arp', *, bass=None, notes=''):
    """Return a measure of (beat, string, fret) events.

    Muted strings are skipped. The optional bass adapts a shared picking
    pattern to a chord whose lowest played string differs from the pattern.
    """
    shape = CHORDS[chord]
    events = []
    for token in (PATTERNS[pattern] + ' ' + notes).split():
        beat_text, strings = token.split(':')
        beat = float(beat_text)
        for item in strings.split(','):
            if '.' in item:
                string, fret = map(int, item.split('.'))
                entries = [(string, fret)]
            else:
                entries = []
                for digit in item:
                    string = int(digit)
                    if bass is not None and string in (5, 6):
                        string = bass
                    entries.append((string, shape[6 - string]))
            for string, fret in entries:
                if fret is not None:
                    events.append((beat, string, fret))
    return events


def picked(chord, *, bass=5, notes=''):
    return bar(chord, 'arp' if bass == 5 else 'walk', bass=bass, notes=notes)


# 第 1 页：前奏、两段主歌及过门。每个列表项是一小节。
INTRO = [
    bar('G', 'intro'), bar('G5', 'held'),
    bar('Em7', 'walk', notes='1.5:6.2'), bar('G', 'held'),
    bar('G', 'intro', notes='1:3'), bar('G5', 'held'),
    bar('C', 'verse', bass=5, notes='2.5:3.0'), bar('G', 'held'),
]
VERSE_1 = [
    bar('G', 'held'), bar('D/F#', 'held'), bar('C/E', 'held'),
    bar('G', 'verse', notes='2.5:1.3'),
    bar('C', 'verse', bass=5, notes='2.5:1.2'),
    bar('G/B', 'verse', bass=5), bar('Am', 'verse', bass=5),
    bar('Dsus4', 'turn', bass=4),
    bar('G', 'turn', notes='2.5:2.1'),
    bar('D/F#', 'turn', notes='2.5:2.0'),
    bar('C/E', 'turn', notes='2.5:3.2'),
    bar('G', 'turn', notes='2.5:1.2'),
    bar('C', 'turn', bass=5, notes='2.5:2.0'),
    bar('D', 'chord', bass=4, notes='1.5:4.4'),
    bar('G', 'turn', notes='2.5:2.1'),
    bar('G', 'turn', notes='2.5:2.2'),
]
INTERLUDE_1 = [
    bar('G', 'turn', notes='1:2.3 2.5:1.2'),
    bar('C', 'turn', bass=5, notes='2:2.3 2.5:2.1'),
    bar('Em/D', 'chord', bass=4), bar('G', 'turn'),
    picked('Em7', bass=6, notes='2:1.3 2.5:1.2'),
    bar('C', 'turn', bass=5, notes='2.5:2.0'),
    bar('D', 'turn', bass=4, notes='2.5:2.0'),
    bar('Dadd11', 'chord', bass=5, notes='2.5:3.0'),
]
VERSE_2 = [
    picked('G', bass=6), picked('D/F#', bass=6), picked('C/E', bass=6),
    picked('G', bass=6, notes='2.5:2.3'),
    picked('C', notes='2:1.3 2.5:1.2'), picked('G/B'),
    picked('Am', notes='2:2.0 2.5:3.0'),
    bar('Em/D', 'chord', bass=4),
    picked('G', bass=6), picked('D/F#', bass=6, notes='2:1.0 2.5:1.2'),
    picked('C/E', bass=6, notes='0:1.3'),
    picked('G', bass=6, notes='2.5:1.2'),
    picked('C', notes='2.5:2.0'), bar('D', 'chord', bass=4, notes='1.5:4.4'),
    picked('Gsus4', bass=6, notes='2.5:3.2'),
    bar('G', 'turn', notes='2:3.2 2.5:2.3'),
]

# 第 2 页的反复从副歌开头到第一结尾；第二遍转入第二结尾。
CHORUS = [
    picked('C'), picked('C'), picked('G/B'), picked('G/B'),
    picked('Am'), picked('D', bass=4), picked('G', bass=6), picked('G', bass=6),
    picked('Em', bass=6), picked('Em', bass=6), picked('Am'), picked('Am'),
    picked('D7', bass=4), picked('D7', bass=4),
]
FIRST_ENDING = [
    picked('Gadd9', bass=6, notes='2:2.3 2.5:2.0'),
    picked('G', bass=6, notes='1:2.3 1.5:2.0 2:2.3 2.5:2.3'),
    picked('Cmaj7'), picked('Cmaj7'), picked('G/B'), picked('G/B'),
    picked('Am7'), picked('D7', bass=4),
    picked('Gadd9', bass=6, notes='0:2.3 1.5:2.3'),
    picked('Gadd9', bass=6, notes='0:2.3 2:1.0 2.5:1.2'),
    picked('Em(3)', bass=4), picked('Em(3)', bass=4),
    picked('Am'), picked('Am'),
    bar('Dsus2', 'turn', bass=4, notes='2.5:2.0'),
    bar('D7', 'turn', bass=4, notes='2.5:2.0'),
    picked('G5', bass=6, notes='1.5:3.2'),
    picked('G', bass=6, notes='2:2.3 2.5:2.0'),
]
SECOND_ENDING = [
    picked('Gsus4', bass=6, notes='2.5:3.2'),
    picked('G', bass=6, notes='2:2.3'),
    picked('Em', bass=6), picked('Em', bass=6), picked('Am'), picked('Am'),
    picked('D7', bass=4), bar('D7', 'chord', bass=4),
]
OUTRO = [
    bar('G', 'intro'), bar('G5', 'held'),
    bar('Em7', 'walk', notes='1.5:6.2'), bar('G', 'held'),
    bar('G', 'intro', notes='1:3'), bar('G5', 'held'),
    bar('C', 'verse', bass=5, notes='2.5:3.0'), bar('G', 'held'),
]
BARS = (INTRO + VERSE_1 + INTERLUDE_1 + VERSE_2 + CHORUS + FIRST_ENDING
        + CHORUS + SECOND_ENDING + OUTRO)


# 简谱按每小节六个八分音符位置录入：0 是休止，- 延长前一音，
# 数字为 A 大调音级，后缀 , 表示低八度。旋律用长笛模拟，不含歌词。
REST = '0 0 0 0 0 0'
MELODY_INTRO = [REST] * 8
MELODY_VERSE_1 = [
    '0 0 0 3 4 5', '5 - 2 - - -', '0 0 0 1 2 3', '2 - 1 - - 5,',
    '6, - 1 1 - 1', '2 - 1 1 - -', '2 - 2 2 1 6,', '3 2 2 - - -',
    '3 3 3 3 4 5', '5 - 2 - - -', '1 1 1 1 2 3', '3 - - - 0 5,',
    '6, - 1 1 - 1', '2 - - - 0 3', '1 - - - - -', REST,
]
MELODY_INTERLUDE_1 = [REST] * 8
MELODY_VERSE_2 = [
    '0 0 0 3 4 5', '5 - 2 - - 5,', '1 1 1 1 2 3', '3 - - - 0 1',
    '6, - 5, 6, - 5,', '5, 4, 4, 3, - 1', '6, - 1 1 - 2', '2 - - - - -',
    '0 0 0 3 4 5', '5 - 2 - - 5,', '1 - 1 1 - 2', '3 - - - - -',
    '4 4 3 4 - 3', '6, 5, 5, 5, 7, 2', '2 1 1 1 - -', '0 0 0 3 - 2',
]
MELODY_CHORUS = [
    '1 1 1 1 1 1', '1 - 6, 1 - 6,', '5, - 3 - - -', '0 0 0 1 2 3',
    '4 4 3 4 3 3', '3 2 2 2 - 1', '2 - 3 - - -', '0 0 0 5, - 3',
    '6, 6, 6, 6, 7, 6,', '3 - - - - -', '4 4 4 4 5 4', '2 - - 2 2 1',
    '2 2 2 2 2 3', '4 - 3 2 - 3',
]
MELODY_FIRST_ENDING = ['2 - 1 - - -', REST] + [REST] * 15 + ['0 0 0 3 - 2']
MELODY_SECOND_ENDING = [
    '2 - 1 - - -', '0 0 0 5, - 3', '6, 6, 6, 6, 7, 6,',
    '3 - - - - -', '4 4 4 4 5 4', '2 - - 2 2 1',
    '2 2 2 2 2 3', '4 - 3 2 3 2',
]
MELODY_OUTRO = ['1 - - - - -'] + [REST] * 7
MELODY = (MELODY_INTRO + MELODY_VERSE_1 + MELODY_INTERLUDE_1 + MELODY_VERSE_2
          + MELODY_CHORUS + MELODY_FIRST_ENDING + MELODY_CHORUS
          + MELODY_SECOND_ENDING + MELODY_OUTRO)
SCALE = (0, 2, 4, 5, 7, 9, 11)


def melody_notes():
    """将六八拍简谱展开为 (起始拍, MIDI 音高, 时值)。"""
    if len(MELODY) != len(BARS):
        raise ValueError('旋律和伴奏小节数不一致')
    current = None
    for bar_number, measure in enumerate(MELODY):
        slots = measure.split()
        if len(slots) != 6:
            raise ValueError(f'第 {bar_number + 1} 小节应有六个八分音符位置')
        for index, symbol in enumerate(slots):
            start = bar_number * BEATS_PER_BAR + index * .5
            if symbol == '-':
                if current is None:
                    raise ValueError(f'第 {bar_number + 1} 小节的延音没有前置音符')
                current[2] += .5
                continue
            if current is not None:
                yield tuple(current)
                current = None
            if symbol != '0':
                degree = symbol.rstrip(',')
                if len(degree) != 1 or degree not in '1234567' or symbol.count(',') > 1:
                    raise ValueError(f'无效简谱音符: {symbol}')
                pitch = 69 + SCALE[int(degree) - 1] - 12 * symbol.count(',')
                current = [start, pitch, .5]
    if current is not None:
        yield tuple(current)


def guitar_notes():
    """Yield (quarter-note beat, string, MIDI pitch, velocity)."""
    for number, measure in enumerate(BARS):
        # Explicit ornaments can replace an X on the same string and beat.
        unique = {(beat, string): fret for beat, string, fret in measure}
        for (beat, string), fret in unique.items():
            if not 0 <= beat < BEATS_PER_BAR or not 1 <= string <= 6 or not 0 <= fret <= 24:
                raise ValueError(f'Invalid tab in measure {number + 1}')
            yield (number * BEATS_PER_BAR + beat, string,
                   OPEN_STRINGS[6 - string] + CAPO + fret,
                   82 if string >= 5 else 90)


class Seagull:
    def __init__(self):
        self.name = str(Path(__file__).resolve().parent / '海鸥.midi')

    def generator(self):
        midi = MIDIFile(2)
        midi.addTempo(0, 0, TEMPO)
        midi.addTimeSignature(0, 0, 6, 3, 36)
        midi.addTrackName(0, 0, 'Guitar')
        midi.addTrackName(1, 0, 'Melody')
        midi.addProgramChange(1, 6, 0, 73)  # GM flute, as in 一笑倾城
        for channel in range(6):
            midi.addProgramChange(0, channel, 0, 25)  # GM steel-string guitar
        notes = sorted(guitar_notes())
        for index, (start, string, pitch, velocity) in enumerate(notes):
            next_start = next((n[0] for n in notes[index + 1:] if n[1] == string), None)
            duration = min(1.5, next_start - start) if next_start is not None else 1.5
            if duration <= 0:
                raise ValueError(f'Duplicate string {string} at beat {start}')
            midi.addNote(0, 6 - string, pitch, start, duration, velocity)
        for start, pitch, duration in melody_notes():
            midi.addNote(1, 6, pitch, start, duration * .95, 88)
        with open(self.name, 'wb') as output:
            midi.writeFile(output)
        return self.name
