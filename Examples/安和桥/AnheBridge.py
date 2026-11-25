"""《安和桥》吉他弹唱谱：Notes/note-1.png 至 note-4.png。

六线谱叉号按和弦指型拨弦；简谱旋律用长笛演奏。
滑音用连续音符近似，MIDI 吉他音色无法完整重现真实演奏。
"""
from pathlib import Path

from midiutil import MIDIFile

TEMPO = 63
INTRO_SILENCE_SECONDS = 0.5
INTERLUDE_PREVIEW_SILENCE_SECONDS = 0.3
INTERLUDE_GAP_SECONDS = 0.3  # 完整曲目中，前段结束到间奏开始的静音
FLUTE_OCTAVE_SHIFT = -12
INTERLUDE_TRANSPOSE = 2  # 比先前指弹版高两个半音
INTERLUDE_VELOCITY_BOOST = 30  # 间奏力度：数值越大越响；MIDI 最大为 127
PLAY_FROM_INTERLUDE = False  # 试听间奏；设为 False 恢复从头播放
OPEN_STRINGS = (40, 45, 50, 55, 59, 64)  # 六弦至一弦，标准调弦
CHORDS = {
    'G': (3, None, 0, 0, 0, None),
    'D6add9': (2, 0, 0, 2, 0, 0),
    'Em': (0, 2, 2, 0, 0, 0),
    'Cadd9': (None, 3, 2, 0, 3, 3),
    'D11': (None, 5, 4, 0, 5, None),
    'Gadd9': (3, None, 0, 2, 0, 3),
    'Cmaj7': (None, 3, 2, 0, 0, 3),
    'Dadd9': (None, 5, 4, 0, 5, 5),
}

# 小节内事件 (拍数, 和弦索引, 琴弦, 可选的明确品位)。
# 如六线谱中同一时间有两个叉号，则两根弦一起拨响。
PATTERNS = {
    'gd': [(0,0,(6,)),(.5,0,(4,)),(1,0,(2,)),(1.5,0,(4,)),
           (2,1,(6,3)),(2.5,1,(4,)),(3,1,(2,)),(3.5,1,(4,))],
    'em_riff': [(0,0,(6,3)),(.5,0,(4,)),(1,0,(4,),4),
                (1.5,0,(3,)),(2,0,(4,),4),(2.5,0,(4,)),(3,0,(4,),0)],
    'cd': [(0,0,(5,2)),(.5,0,(4,)),(1,0,(3,)),(1.5,0,(2,)),
           (2,1,(5,2)),(2.5,1,(4,)),(3,1,(3,)),(3.5,1,(2,),0)],
    'gadd': [(0,0,(6,2)),(.5,0,(4,)),(1,0,(3,)),(1.5,0,(4,)),
             (2,0,(2,)),(2.5,0,(4,)),(3,0,(3,)),(3.5,0,(4,))],
    'em_end': [(0,0,(6,1)),(.5,0,(3,)),(1,0,(2,)),(1.5,0,(3,)),(2,0,(6,))],
    'cm_d': [(0,0,(5,2)),(.5,0,(4,)),(1,0,(1,)),(1.5,0,(4,)),
             (2,1,(5,1)),(2.5,1,(4,)),(3,1,(2,)),(3.5,1,(4,))],
    'em_d': [(0,0,(6,1)),(.5,0,(4,)),(1,0,(1,)),(1.5,0,(4,)),
             (2,1,(5,2)),(2.5,1,(4,)),(3,1,(3,)),(3.5,1,(2,))],
    'ca_d': [(0,0,(5,1)),(.5,0,(4,)),(1,0,(1,)),(1.5,0,(4,)),
             (2,1,(5,1)),(2.5,1,(4,)),(3,1,(2,)),(3.5,1,(4,))],
}
GD = ('gd', 'G', 'D6add9')
ER = ('em_riff', 'Em', 'Em')
CD = ('cd', 'Cadd9', 'D11')
GA = ('gadd', 'Gadd9', 'Gadd9')
EE = ('em_end', 'Em', 'Em')
CM = ('cm_d', 'Cmaj7', 'Dadd9')
ED = ('em_d', 'Em', 'D11')
CA = ('ca_d', 'Cadd9', 'Dadd9')
GUITAR_BARS = [
    None, GD, ER, CD, GA, GD, ER, CD, EE,       # 1–9 前奏
    GD, ER, CD, GA, GD, ER, CD, EE,             # 10–17
    CM, ED, CD, GA, CA, ED, CD, EE,             # 18–25
    GD, ER, CD, GA, GD, ER, CD, EE,             # 26–33
    CM, ED, CD, GA, CA, ED, CD, EE,             # 34–41 间奏
    CM, ED, CD, GA, CA, ED, CD, EE,             # 42–49
    CM, ED, CD, GA, CA, ED, CD, EE,             # 50–57
]

# 每项为一小节。格式“音级:时值”，四分音符一拍；0 表示休止，
# 后缀 , 为低八度，^ 为高八度；~ 把前一音延长（包括跨小节连音）。
REST = '0:4'
MELODY_10_17 = [
    '0:.5 5,:.25 5,:.25 3:.25 3:.25 2:.25 3:.25 2:1 3:.5 2:.5',
    '1:.25 6,:.75 ~:1 0:1.5 5,:.25 5,:.25',
    '6:.5 5:.25 6:.25 ~:.25 5:.75 ~:.5 2:.5 2:.5 5:.5',
    '0:.5 5:.25 3:.25 ~:1 0:1 0:1',
    '0:.5 3:.25 3:.25 3:.5 6,:.25 3:.25 ~:.25 2:.75 3:.5 2:.25 1:.25',
    '~:.25 6,:.75 0:1 0:1.5 5,:.25 5,:.25',
    '2:.5 2:.25 1:.25 2:.25 1:.75 0:.75 5,:.25 2:.5 1:.25 1:.25',
    '~:.25 1:.25 6,:.5 ~:1 0:1.5 5:.25 5:.25',
]
MELODY_18_25 = [
    '1^:1 0:.5 1^:.25 1^:.25 2^:.5 6:.5 0:.5 6:.25 6:.25',
    '3^:.5 1^:.5 7:.5 6:.5 6:.25 5:.25 6:.5 0:.5 6:.25 5:.25',
    '6:.5 5:.25 1^:.25 ~:.75 1^:.25 1^:.25 2^:.5 2^:.25 2^:.5 3^:.5',
    '0:.5 5:.25 3:.25 ~:1 0:1.5 5:.25 5:.25',
    '1^:1 1^:.25 6:.75 6:.25 2^:.25 2^:.5 6:.25 6:.25 6:.5',
    '3^:.5 1^:.5 7:.5 6:.25 5:.25 6:.25 6:.75 ~:.5 6:.25 5:.25',
    '6:.5 5:.25 1^:.25 ~:.25 6:.75 6:.25 ~:.75 2:.5 2:.25 1:.25',
    '~:2 0:1 0:1',
]
MELODY_26_33 = [
    '0:.5 3:.25 3:.25 3:.5 3:.25 ~:.25 3:.25 2:.75 3:.5 2:.5',
    '1:.25 6,:.75 ~:1 0:1.5 5:.25 6:.25',
    '~:.5 5:.25 6:.25 ~:.25 6:.75 5:.25 ~:.75 5:.5 5:.5',
    '6:.5 3:.5 ~:1 0:1 0:1',
    '0:.5 3:.25 3:.25 3:.5 3:.25 ~:.25 3:.25 2:.75 3:.5 2:.25 1:.25',
    '1:.5 1:.25 6,:.25 ~:1 0:1 0:.5 5,:.25 2:.25',
    '2:.25 1:.75 0:1 0:.5 5,:.25 5,:.25 2:.5 6,:.25 1:.25',
    '~:.5 1:.5 0:1 0:1 0:1',
]
MELODY_34_41 = [REST] * 7 + ['0:.25 0:.75 0:1 0:1.5 5:.25 5:.25']
MELODY_42_49 = MELODY_18_25[:7] + ['~:2 0:1.5 5:.25 5:.25']
MELODY_50_57 = [
    MELODY_18_25[0], MELODY_18_25[1],
    '6:.5 5:.25 1^:.25 ~:.75 1^:.25 1^:.25 2^:.5 ~:.25 2^:.5 3^:.5',
    '0:.5 5:.25 3:.25 ~:1 ~:1.5 5:.25 5:.25',
    '1^:1 1^:.25 6:.75 2^:.5 2^:.5 6:.5 6:.5',
    MELODY_18_25[5],
    '1^:.25 6:.75 ~:1 0:1 0:.5 2:.5',
    '6,:1 ~:1 0:1 0:1',
]
MELODY_BARS = ([REST] * 9 + MELODY_10_17 + MELODY_18_25 + MELODY_26_33
               + MELODY_34_41 + MELODY_42_49 + MELODY_50_57)
SCALE = (0, 2, 4, 5, 7, 9, 11)

# 恢复上一版点点糖指弹谱中的九小节间奏。格式为拍=弦.品，
# 同时拨响的多根弦用逗号分隔；滑音、击弦和勾弦仍为近似。
INTERLUDE = [
    '3=2.5 3.25=2.3 3.5=2.5 3.75=2.3',
    '0=5.3,4.2 .5=5.3 1=4.2 1.5=3.0 1.75=3.2 2=3.2,4.0 3=2.0 3.5=2.3',
    '0=6.3,2.0 .333333=2.3 .666667=2.0 1=2.0 1.5=3.0 2=4.0 2.5=6.3 2.75=3.2 3=3.4 3.25=2.5 3.5=2.3 3.666667=2.5 3.833333=2.3',
    '0=5.3,4.2 .5=5.3 1=4.2 1.5=3.0 1.75=3.2 2=3.2,4.0 3=2.0 3.5=2.3',
    '0=6.3,2.0 .333333=2.3 .666667=2.0 1=2.0 1.5=3.0 2=4.0 2.5=6.3 3=4.0 3.5=1.7 3.75=1.5',
    '0=5.3,1.5 .5=1.3 1=2.0 1.5=3.0 2=4.0,1.5 2.75=1.5 3=1.7 3.5=1.10',
    '0=6.0,1.7 .125=1.10 .25=1.7 .375=1.10 .5=1.7 1=2.0 1.5=3.0 2=6.0 2.5=1.12 3=1.12 3.5=1.12 3.75=1.5',
    '0=5.3,1.5 .5=3.0 1=2.0 1.5=1.3 1.75=1.3 2=4.0,1.5 2.5=1.3 3=1.5 3.5=1.7',
    '0=6.0,1.7 .5=1.0 1=2.0 1.5=3.0 2=1.12,2.12,3.12 3.5=2.3 3.75=2.3',
]
INTERLUDE_FIRST_BAR = 33  # 当前谱的第 34 小节，索引从零开始
REPLACED_BARS = 8
INTERLUDE_EXTRA_BEATS = (len(INTERLUDE) - REPLACED_BARS) * 4


def melody_notes():
    if len(MELODY_BARS) != len(GUITAR_BARS):
        raise ValueError('旋律和吉他伴奏的小节数不一致')
    current = None
    for bar, measure in enumerate(MELODY_BARS):
        beat = 0.0
        for token in measure.split():
            name, value = token.split(':')
            duration = float(value)
            start = bar * 4 + beat
            if name == '~':
                if current is None or current[0] + current[2] != start:
                    raise ValueError(f'第 {bar + 1} 小节的连音没有前置音符')
                current[2] += duration
            else:
                if current is not None:
                    yield tuple(current)
                    current = None
                if name != '0':
                    degree = name[0]
                    if degree not in '1234567' or name[1:] not in ('', ',', '^'):
                        raise ValueError(f'无效音级: {name}')
                    octave = -12 if name.endswith(',') else 12 if name.endswith('^') else 0
                    current = [start, 67 + SCALE[int(degree) - 1] + octave, duration]
            beat += duration
        if beat != 4:
            raise ValueError(f'第 {bar + 1} 小节旋律共 {beat} 拍，预期 4 拍')
    if current is not None:
        yield tuple(current)


def guitar_notes():
    for number, spec in enumerate(GUITAR_BARS):
        if INTERLUDE_FIRST_BAR <= number < INTERLUDE_FIRST_BAR + REPLACED_BARS:
            continue
        if spec is None:
            continue
        pattern, first, second = spec
        chords = (CHORDS[first], CHORDS[second])
        for event in PATTERNS[pattern]:
            beat, half, strings = event[:3]
            for string in strings:
                fret = event[3] if len(event) == 4 else chords[half][6 - string]
                if fret is None:
                    raise ValueError(f'第 {number + 1} 小节使用了不发声的 {string} 弦')
                shift = INTERLUDE_EXTRA_BEATS if number >= INTERLUDE_FIRST_BAR + REPLACED_BARS else 0
                yield number * 4 + beat + shift, string, OPEN_STRINGS[6 - string] + fret, 82 if string >= 5 else 76
    for bar, measure in enumerate(INTERLUDE):
        for token in measure.split():
            beat_text, entries = token.split('=')
            beat = float(beat_text)
            for entry in entries.split(','):
                string, fret = map(int, entry.split('.'))
                yield ((INTERLUDE_FIRST_BAR + bar) * 4 + beat, string,
                       OPEN_STRINGS[6 - string] + fret + INTERLUDE_TRANSPOSE,
                       min(127, (82 if string >= 5 else 90) + INTERLUDE_VELOCITY_BOOST))


class AnheBridge:
    def __init__(self):
        self.name = str(Path(__file__).resolve().parent / '安和桥.midi')

    def generator(self):
        midi = MIDIFile(2)
        midi.addTempo(0, 0, TEMPO)
        midi.addTimeSignature(0, 0, 4, 2, 24)
        midi.addTrackName(0, 0, 'Guitar')
        midi.addTrackName(1, 0, 'Flute melody')
        for channel in range(6):
            midi.addProgramChange(0, channel, 0, 25)  # 钢弦吉他
        midi.addProgramChange(1, 6, 0, 73)  # 长笛
        notes = sorted(guitar_notes())
        vocals = list(melody_notes())
        # 试听时保留指定的间奏前静音；完整播放仍保留开头半秒缓冲。
        interlude_start = INTERLUDE_FIRST_BAR * 4
        # 间奏首个事件可能在小节中途，按实际音符起点裁掉前面的空拍。
        first_interlude_note = next(n[0] for n in notes if n[0] >= interlude_start)
        start_beat = (first_interlude_note
                      if PLAY_FROM_INTERLUDE else notes[0][0])
        silence_seconds = INTERLUDE_PREVIEW_SILENCE_SECONDS if PLAY_FROM_INTERLUDE else INTRO_SILENCE_SECONDS
        silence = silence_seconds * TEMPO / 60
        lead_trim = max(0, start_beat - silence)
        # 完整播放时，把间奏及后续声部一起前移，使前段音符结束后
        # 保留指定静音；不改变间奏和后续段落之间的相对时间。
        previous_ends = []
        for index, (start, string, pitch, velocity) in enumerate(notes):
            if start >= interlude_start:
                break
            following = next((n[0] for n in notes[index + 1:] if n[1] == string), None)
            duration = min(1.0, following - start) if following is not None else 1.0
            previous_ends.append(start + duration)
        previous_ends.extend(start + duration * .95 for start, pitch, duration in vocals
                             if start < interlude_start)
        gap_trim = max(0, first_interlude_note - max(previous_ends)
                       - INTERLUDE_GAP_SECONDS * TEMPO / 60)
        for index, (start, string, pitch, velocity) in enumerate(notes):
            if start < start_beat:
                continue
            following = next((n[0] for n in notes[index + 1:] if n[1] == string), None)
            duration = min(1.0, following - start) if following is not None else 1.0
            if duration <= 0:
                raise ValueError(f'第 {start / 4 + 1:g} 小节同一弦重复拨弦')
            interlude_shift = gap_trim if not PLAY_FROM_INTERLUDE and start >= first_interlude_note else 0
            midi.addNote(0, 6 - string, pitch, start - lead_trim - interlude_shift, duration, velocity)
        for start, pitch, duration in vocals:
            # 第 41 小节末尾的引唱随恢复的间奏一起顺延一小节。
            shift = INTERLUDE_EXTRA_BEATS if start >= (INTERLUDE_FIRST_BAR + REPLACED_BARS - 1) * 4 else 0
            if start + shift < start_beat:
                continue
            interlude_shift = gap_trim if not PLAY_FROM_INTERLUDE and start + shift >= first_interlude_note else 0
            midi.addNote(1, 6, pitch + FLUTE_OCTAVE_SHIFT,
                         start + shift - lead_trim - interlude_shift, duration * .95, 85)
        with open(self.name, 'wb') as output:
            midi.writeFile(output)
        return self.name
