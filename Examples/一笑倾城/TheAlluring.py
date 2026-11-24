"""《一笑倾城》：根据 Notes 记录和弦、扫弦节奏及简谱。

原谱没有标注速度；TEMPO 是可自行调整的演奏速度。简谱旋律与
吉他伴奏分别记录，连音跨小节时保持为同一个音符。
"""
from pathlib import Path

from midiutil import MIDIFile

TEMPO = 90
OPEN_STRINGS = (40, 45, 50, 55, 59, 64)  # 6 弦到 1 弦，标准调弦
CHORDS = {
    'C': (None, 3, 2, 0, 1, 0),
    'G': (3, 2, 0, 0, 0, 3),
    'Em': (0, 2, 2, 0, 0, 0),
    'Am': (None, 0, 2, 2, 1, 0),
    'Fmaj7': (0, 0, 3, 2, 1, 0),
}

# 每小节八个八分音符位置；1-7 为中央 C 起的简谱，+ 为高八度，
# # 为升半音，0 为休止，- 延长上一个音（包括跨小节连音）。
# 每行对应谱面的一小节，伴奏和旋律同时开始。
SCORE = [
    ('C', '0 0 0 0 0 0 0 0'), ('G', '0 0 0 0 0 0 0 0'),
    ('Em', '0 0 0 0 0 0 0 0'), ('Am', '0 0 0 0 0 0 0 0'),
    ('Fmaj7', '0 0 0 0 0 0 0 0'), ('G', '0 0 0 0 0 0 0 0'),
    ('C', '0 0 0 0 0 0 0 0'), ('C', '0 0 0 0 0 0 0 0'),
    ('C', '0 1+ 1+ 1+ 1+ 6 6 1+'),
    ('G', '7 7 7 1+ 7 5 5 -'),
    ('Em', '0 7 7 7 7 5 5 7'),
    ('Am', '7 5 5 7 7 1+ 1+ -'),
    ('Fmaj7', '0 1+ 1+ 1+ 1+ 6 6 1+'),
    ('G', '7 7 7 1+ 7 5 5 -'),
    ('C', '0 1+ 1+ 1+ 1+ 2+ 3+ 1+'),
    ('C', '0 1+ 1+ 1+ 1+ 2+ 3+ 1+'),
    ('C', '1+ - 3+ 1+ - 3+ 1+ 2+'),
    ('G', '- - - - - - - -'),
    ('Em', '7 - 2+ 7 - 2+ 7 1+'),
    ('Am', '- - - - - - - -'),
    ('Fmaj7', '1+ - 3+ 1+ - 3+ 1+ 2+'),
    ('G', '- - 5 5 1+ 2+ 3+ 3+'),
    ('C', '- - - - - - - -'),
    ('C', '0 0 0 0 0 0 0 0'),
    ('C', '1+ - 3+ 1+ - 3+ 1+ 2+'),
    ('G', '- - - - - - - -'),
    ('Em', '7 - 2+ 7 - 2+ 7 1+'),
    ('Am', '- - - - - - - -'),
    ('Fmaj7', '1+ - 3+ 1+ - 3+ 1+ 2+'),
    ('G', '- - - - 2+ 1+ 7 1+'),
    ('C', '- - - - - - - -'),
    ('C', '0 0 0 0 3+ 4+ 3+ 5+'),
    ('C', '- 1+ 1+ 1+ 1+ 6 1+ 3+'),
    ('G', '- 2+ - - 3+ 4+ 3+ 5+'),
    ('Em', '- 7 7 7 7 5 7 2+'),
    ('Am', '- #1+ - - 2+ 3+ 2+ 4+'),
    ('Fmaj7', '- 3+ 4+ 3+ 4+ 3+ 6 1+'),
    ('G', '- 7 - 7 7 1+ 6 5+'),
    ('C', '- - - - - - - -'),
    ('C', '0 0 0 0 3+ 4+ 3+ 5+'),
    ('C', '- 1+ 1+ 1+ 1+ 6 1+ 3+'),
    ('G', '- 2+ - - 3+ 4+ 3+ 5+'),
    ('Em', '- 7 7 7 7 5 7 2+'),
    ('Am', '- #1+ - - 2+ 3+ 2+ 4+'),
    ('Fmaj7', '- 3+ 4+ 3+ 4+ 3+ 6 1+'),
    ('G', '- 7 - 7 5 7 2+ -'),
    ('C', '- 1+ - - - - - -'),
    ('C', '0 0 0 0 0 0 0 0'),
]

# 箭头覆盖低音弦或高音弦；向上/向下分别按低到高/高到低扫弦。
# 四个十六分音符和最后一组八分、十六分音符按原谱排列。
STRUMS = (
    (0, 'bass', 'down'), (.5, 'bass', 'down'),
    (1, 'treble', 'down'), (1.5, 'treble', 'down'),
    (2, 'bass', 'down'), (2.25, 'treble', 'down'),
    (2.5, 'treble', 'up'), (2.75, 'bass', 'down'),
    (3, 'treble', 'down'), (3.5, 'treble', 'down'),
    (3.75, 'treble', 'up'),
)
SCALE = (0, 2, 4, 5, 7, 9, 11)


def melody_notes(score):
    """将简谱展开为 (起始拍, 音高, 时值)，保留跨小节连音。"""
    current = None
    for bar, (_, melody) in enumerate(score):
        slots = melody.split()
        if len(slots) != 8:
            raise ValueError(f'第 {bar + 1} 小节应有八个八分音符位置')
        for slot, symbol in enumerate(slots):
            time = bar * 4 + slot * .5
            if symbol == '-':
                if current is None:
                    raise ValueError(f'第 {bar + 1} 小节的连音没有前置音符')
                current[2] += .5
                continue
            if current is not None:
                yield tuple(current)
                current = None
            if symbol != '0':
                degree = symbol.replace('#', '').replace('+', '')
                if degree not in '1234567' or len(degree) != 1:
                    raise ValueError(f'无效简谱音符: {symbol}')
                pitch = 60 + SCALE[int(degree) - 1] + 12 * symbol.count('+') + symbol.count('#')
                current = [time, pitch, .5]
    if current is not None:
        yield tuple(current)


def guitar_notes(score):
    """展开扫弦，弦音持续到下一次拨动或换和弦为止。"""
    events = []
    for bar, (chord, _) in enumerate(score):
        frets = CHORDS[chord]
        for stroke, (beat, group, direction) in enumerate(STRUMS):
            indices = range(0, 3) if group == 'bass' else range(3, 6)
            indices = [i for i in indices if frets[i] is not None]
            if direction == 'up':
                indices.reverse()
            # 重拍更有力，回扫较轻；逐弦略微减弱，避免机械式齐奏。
            accent = (9, 1, 5, 0, 6, 1, -4, 0, 5, 0, -4)[stroke]
            for offset, i in enumerate(indices):
                start = bar * 4 + beat + offset * .022
                velocity = (72 if group == 'bass' else 69) + accent - offset * 2
                # 相邻小节和弦相同时可以继续共鸣；换和弦时止音。
                chord_end = (bar + 1) * 4
                while chord_end < len(score) * 4 and score[int(chord_end / 4)][0] == chord:
                    chord_end += 4
                events.append((start, i, OPEN_STRINGS[i] + frets[i], velocity, chord_end))
    next_on_string = {}
    result = []
    for start, string, pitch, velocity, chord_end in reversed(events):
        end = min(start + 1.25, chord_end, next_on_string.get(string, float('inf')))
        if end > start:
            result.append((start, string, pitch, end - start, velocity))
        next_on_string[string] = start
    yield from reversed(result)



class TheAlluring:
    def __init__(self):
        self.name = str(Path(__file__).resolve().parent / '一笑倾城.midi')

    def generator(self):
        name = Path(self.name)
        midi = MIDIFile(2)
        midi.addTempo(0, 0, TEMPO)
        midi.addTrackName(0, 0, 'Guitar')
        midi.addTrackName(1, 0, 'Melody')
        # GM 钢弦吉他及长笛；每根吉他弦独立通道，避免同音互相截断。
        for channel in range(6):
            midi.addProgramChange(0, channel, 0, 25)
        midi.addProgramChange(1, 6, 0, 73)
        # 末尾反复记号没有指定起点，按惯例从头反复一次。
        score = SCORE * 2
        for start, string, pitch, duration, velocity in guitar_notes(score):
            midi.addNote(0, string, pitch, start, duration, velocity)
        for start, pitch, duration in melody_notes(score):
            midi.addNote(1, 6, pitch, start, duration * .95, 88)
        with name.open('wb') as output:
            midi.writeFile(output)
        return str(name)
