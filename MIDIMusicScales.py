# Author: Authey
# Date: 10/06/2020

# ------------------------------------------------------------------------------ #
#   #  ||  C  |  C# |  D  |  D# |  E  |  F  |  F# |  G  |  G# |  A  |  A# |  B   #
# ------------------------------------------------------------------------------ #
#   0  ||   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |  10 |  11  #
#   1  ||  12 |  13 |  14 |  15 |  16 |  17 |  18 |  19 |  20 |  21 |  22 |  23  #
#   2  ||  24 |  25 |  26 |  27 |  28 |  29 |  30 |  31 |  32 |  33 |  34 |  35  #
#   3  ||  36 |  37 |  38 |  39 |  40 |  41 |  42 |  43 |  44 |  45 |  46 |  47  #
#   4  ||  48 |  49 |  50 |  51 |  52 |  53 |  54 |  55 |  56 |  57 |  58 |  59  #
#   5  ||  60 |  61 |  62 |  63 |  64 |  65 |  66 |  67 |  68 |  69 |  70 |  71  #
#   6  ||  72 |  73 |  74 |  75 |  76 |  77 |  78 |  79 |  80 |  81 |  82 |  83  #
#   7  ||  84 |  85 |  86 |  87 |  88 |  89 |  90 |  91 |  92 |  93 |  94 |  95  #
#   8  ||  96 |  97 |  98 |  99 | 100 | 101 | 102 | 103 | 104 | 105 | 106 | 107  #
#   9  || 108 | 109 | 110 | 111 | 112 | 113 | 114 | 115 | 116 | 117 | 118 | 119  #
#   10 || 120 | 121 | 122 | 123 | 124 | 125 | 126 | 127 |                        #
# ------------------------------------------------------------------------------ #


from midiutil import MIDIFile


class Scales:

    def __init__(self, tempo=120):
        self.tempo = tempo  # In BPM
        self.track = 0
        self.time = 0
        self.channel = 0
        self.MyMIDI = MIDIFile(1)  # One track, defaults to format 1
        self.MyMIDI.addTempo(self.track, self.time, self.tempo)

    # ------------------------------------------ C ------------------------------------------- #

    # ------------------------------- C0 ------------------------------- #
    def c0(self, duration=1, volume=100):
        pitch = 0
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C1 ------------------------------- #
    def c1(self, duration=1, volume=100):
        pitch = 12
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C2 ------------------------------- #
    def c2(self, duration=1, volume=100):
        pitch = 24
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C3 ------------------------------- #
    def c3(self, duration=1, volume=100):
        pitch = 36
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C4 ------------------------------- #
    def c4(self, duration=1, volume=100):
        pitch = 48
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C5 ------------------------------- #
    def c5(self, duration=1, volume=100):
        pitch = 60
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C6 ------------------------------- #
    def c6(self, duration=1, volume=100):
        pitch = 72
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C7 ------------------------------- #
    def c7(self, duration=1, volume=100):
        pitch = 84
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C8 ------------------------------- #
    def c8(self, duration=1, volume=100):
        pitch = 96
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C9 ------------------------------- #
    def c9(self, duration=1, volume=100):
        pitch = 108
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C10 ------------------------------- #
    def c10(self, duration=1, volume=100):
        pitch = 120
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ----------------------------------------- C# ------------------------------------------- #

    # ------------------------------- C#0 ------------------------------- #
    def c0s(self, duration=1, volume=100):
        pitch = 1
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#1 ------------------------------- #
    def c1s(self, duration=1, volume=100):
        pitch = 13
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#2 ------------------------------- #
    def c2s(self, duration=1, volume=100):
        pitch = 25
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#3 ------------------------------- #
    def c3s(self, duration=1, volume=100):
        pitch = 37
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#4 ------------------------------- #
    def c4s(self, duration=1, volume=100):
        pitch = 49
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#5 ------------------------------- #
    def c5s(self, duration=1, volume=100):
        pitch = 61
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#6 ------------------------------- #
    def c6s(self, duration=1, volume=100):
        pitch = 73
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#7 ------------------------------- #
    def c7s(self, duration=1, volume=100):
        pitch = 85
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#8 ------------------------------- #
    def c8s(self, duration=1, volume=100):
        pitch = 97
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#9 ------------------------------- #
    def c9s(self, duration=1, volume=100):
        pitch = 109
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- C#10 ------------------------------- #
    def c10s(self, duration=1, volume=100):
        pitch = 121
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ D ------------------------------------------- #

    # ------------------------------- D0 ------------------------------- #
    def d0(self, duration=1, volume=100):
        pitch = 2
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D1 ------------------------------- #
    def d1(self, duration=1, volume=100):
        pitch = 14
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D2 ------------------------------- #
    def d2(self, duration=1, volume=100):
        pitch = 26
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D3 ------------------------------- #
    def d3(self, duration=1, volume=100):
        pitch = 38
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D4 ------------------------------- #
    def d4(self, duration=1, volume=100):
        pitch = 50
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D5 ------------------------------- #
    def d5(self, duration=1, volume=100):
        pitch = 62
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D6 ------------------------------- #
    def d6(self, duration=1, volume=100):
        pitch = 74
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D7 ------------------------------- #
    def d7(self, duration=1, volume=100):
        pitch = 86
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D8 ------------------------------- #
    def d8(self, duration=1, volume=100):
        pitch = 98
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D9 ------------------------------- #
    def d9(self, duration=1, volume=100):
        pitch = 110
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D10 ------------------------------- #
    def d10(self, duration=1, volume=100):
        pitch = 122
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ D# ------------------------------------------- #

    # ------------------------------- D#0 ------------------------------- #
    def d0s(self, duration=1, volume=100):
        pitch = 3
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#1 ------------------------------- #
    def d1s(self, duration=1, volume=100):
        pitch = 15
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#2 ------------------------------- #
    def d2s(self, duration=1, volume=100):
        pitch = 27
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#3 ------------------------------- #
    def d3s(self, duration=1, volume=100):
        pitch = 39
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#4 ------------------------------- #
    def d4s(self, duration=1, volume=100):
        pitch = 51
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#5 ------------------------------- #
    def d5s(self, duration=1, volume=100):
        pitch = 63
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#6 ------------------------------- #
    def d6s(self, duration=1, volume=100):
        pitch = 75
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#7 ------------------------------- #
    def d7s(self, duration=1, volume=100):
        pitch = 87
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#8 ------------------------------- #
    def d8s(self, duration=1, volume=100):
        pitch = 99
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#9 ------------------------------- #
    def d9s(self, duration=1, volume=100):
        pitch = 111
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- D#10 ------------------------------- #
    def d10s(self, duration=1, volume=100):
        pitch = 123
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ E ------------------------------------------- #

    # ------------------------------- E0 ------------------------------- #
    def e0(self, duration=1, volume=100):
        pitch = 4
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E1 ------------------------------- #
    def e1(self, duration=1, volume=100):
        pitch = 16
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E2 ------------------------------- #
    def e2(self, duration=1, volume=100):
        pitch = 28
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E3 ------------------------------- #
    def e3(self, duration=1, volume=100):
        pitch = 40
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E4 ------------------------------- #
    def e4(self, duration=1, volume=100):
        pitch = 52
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E5 ------------------------------- #
    def e5(self, duration=1, volume=100):
        pitch = 64
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E6 ------------------------------- #
    def e6(self, duration=1, volume=100):
        pitch = 76
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E7 ------------------------------- #
    def e7(self, duration=1, volume=100):
        pitch = 88
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E8 ------------------------------- #
    def e8(self, duration=1, volume=100):
        pitch = 100
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E9 ------------------------------- #
    def e9(self, duration=1, volume=100):
        pitch = 112
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- E10 ------------------------------- #
    def e10(self, duration=1, volume=100):
        pitch = 124
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ F ------------------------------------------- #

    # ------------------------------- F0 ------------------------------- #
    def f0(self, duration=1, volume=100):
        pitch = 5
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F1 ------------------------------- #
    def f1(self, duration=1, volume=100):
        pitch = 17
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F2 ------------------------------- #
    def f2(self, duration=1, volume=100):
        pitch = 29
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F3 ------------------------------- #
    def f3(self, duration=1, volume=100):
        pitch = 41
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F4 ------------------------------- #
    def f4(self, duration=1, volume=100):
        pitch = 53
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F5 ------------------------------- #
    def f5(self, duration=1, volume=100):
        pitch = 65
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F6 ------------------------------- #
    def f6(self, duration=1, volume=100):
        pitch = 77
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F7 ------------------------------- #
    def f7(self, duration=1, volume=100):
        pitch = 89
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F8 ------------------------------- #
    def f8(self, duration=1, volume=100):
        pitch = 101
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F9 ------------------------------- #
    def f9(self, duration=1, volume=100):
        pitch = 113
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F10 ------------------------------- #
    def f10(self, duration=1, volume=100):
        pitch = 125
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ F# ------------------------------------------- #

    # ------------------------------- F#0 ------------------------------- #
    def f0s(self, duration=1, volume=100):
        pitch = 6
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#1 ------------------------------- #
    def f1s(self, duration=1, volume=100):
        pitch = 18
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#2 ------------------------------- #
    def f2s(self, duration=1, volume=100):
        pitch = 30
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#3 ------------------------------- #
    def f3s(self, duration=1, volume=100):
        pitch = 42
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#4 ------------------------------- #
    def f4s(self, duration=1, volume=100):
        pitch = 54
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#5 ------------------------------- #
    def f5s(self, duration=1, volume=100):
        pitch = 66
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#6 ------------------------------- #
    def f6s(self, duration=1, volume=100):
        pitch = 78
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#7 ------------------------------- #
    def f7s(self, duration=1, volume=100):
        pitch = 90
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#8 ------------------------------- #
    def f8s(self, duration=1, volume=100):
        pitch = 102
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#9 ------------------------------- #
    def f9s(self, duration=1, volume=100):
        pitch = 114
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- F#10 ------------------------------- #
    def f10s(self, duration=1, volume=100):
        pitch = 126
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ G ------------------------------------------- #

    # ------------------------------- G0 ------------------------------- #
    def g0(self, duration=1, volume=100):
        pitch = 7
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G1 ------------------------------- #
    def g1(self, duration=1, volume=100):
        pitch = 19
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G2 ------------------------------- #
    def g2(self, duration=1, volume=100):
        pitch = 31
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G3 ------------------------------- #
    def g3(self, duration=1, volume=100):
        pitch = 43
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G4 ------------------------------- #
    def g4(self, duration=1, volume=100):
        pitch = 55
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G5 ------------------------------- #
    def g5(self, duration=1, volume=100):
        pitch = 67
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G6 ------------------------------- #
    def g6(self, duration=1, volume=100):
        pitch = 79
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G7 ------------------------------- #
    def g7(self, duration=1, volume=100):
        pitch = 91
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G8 ------------------------------- #
    def g8(self, duration=1, volume=100):
        pitch = 103
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G9 ------------------------------- #
    def g9(self, duration=1, volume=100):
        pitch = 115
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G10 ------------------------------- #
    def g10(self, duration=1, volume=100):
        pitch = 127
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ G# ------------------------------------------- #

    # ------------------------------- G#0 ------------------------------- #
    def g0s(self, duration=1, volume=100):
        pitch = 8
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G#1 ------------------------------- #
    def g1s(self, duration=1, volume=100):
        pitch = 20
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G#2 ------------------------------- #
    def g2s(self, duration=1, volume=100):
        pitch = 32
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G#3 ------------------------------- #
    def g3s(self, duration=1, volume=100):
        pitch = 44
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G#4 ------------------------------- #
    def g4s(self, duration=1, volume=100):
        pitch = 56
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G#5 ------------------------------- #
    def g5s(self, duration=1, volume=100):
        pitch = 68
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G#6 ------------------------------- #
    def g6s(self, duration=1, volume=100):
        pitch = 80
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G#7 ------------------------------- #
    def g7s(self, duration=1, volume=100):
        pitch = 92
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G#8 ------------------------------- #
    def g8s(self, duration=1, volume=100):
        pitch = 104
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- G#9 ------------------------------- #
    def g9s(self, duration=1, volume=100):
        pitch = 116
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ A ------------------------------------------- #

    # ------------------------------- A0 ------------------------------- #
    def a0(self, duration=1, volume=100):
        pitch = 9
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A1 ------------------------------- #
    def a1(self, duration=1, volume=100):
        pitch = 21
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A2 ------------------------------- #
    def a2(self, duration=1, volume=100):
        pitch = 33
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A3 ------------------------------- #
    def a3(self, duration=1, volume=100):
        pitch = 45
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A4 ------------------------------- #
    def a4(self, duration=1, volume=100):
        pitch = 57
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A5 ------------------------------- #
    def a5(self, duration=1, volume=100):
        pitch = 69
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A6 ------------------------------- #
    def a6(self, duration=1, volume=100):
        pitch = 81
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A7 ------------------------------- #
    def a7(self, duration=1, volume=100):
        pitch = 93
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A8 ------------------------------- #
    def a8(self, duration=1, volume=100):
        pitch = 105
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A9 ------------------------------- #
    def a9(self, duration=1, volume=100):
        pitch = 117
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ A# ------------------------------------------- #

    # ------------------------------- A#0 ------------------------------- #
    def a0s(self, duration=1, volume=100):
        pitch = 10
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A#1 ------------------------------- #
    def a1s(self, duration=1, volume=100):
        pitch = 22
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A#2 ------------------------------- #
    def a2s(self, duration=1, volume=100):
        pitch = 34
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A#3 ------------------------------- #
    def a3s(self, duration=1, volume=100):
        pitch = 46
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A#4 ------------------------------- #
    def a4s(self, duration=1, volume=100):
        pitch = 58
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A#5 ------------------------------- #
    def a5s(self, duration=1, volume=100):
        pitch = 70
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A#6 ------------------------------- #
    def a6s(self, duration=1, volume=100):
        pitch = 82
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A#7 ------------------------------- #
    def a7s(self, duration=1, volume=100):
        pitch = 94
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A#8 ------------------------------- #
    def a8s(self, duration=1, volume=100):
        pitch = 106
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- A#9 ------------------------------- #
    def a9s(self, duration=1, volume=100):
        pitch = 118
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------------------ B ------------------------------------------- #

    # ------------------------------- B0 ------------------------------- #
    def b0(self, duration=1, volume=100):
        pitch = 11
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- B1 ------------------------------- #
    def b1(self, duration=1, volume=100):
        pitch = 23
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- B2 ------------------------------- #
    def b2(self, duration=1, volume=100):
        pitch = 35
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- B3 ------------------------------- #
    def b3(self, duration=1, volume=100):
        pitch = 47
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- B4 ------------------------------- #
    def b4(self, duration=1, volume=100):
        pitch = 59
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- B5 ------------------------------- #
    def b5(self, duration=1, volume=100):
        pitch = 71
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- B6 ------------------------------- #
    def b6(self, duration=1, volume=100):
        pitch = 83
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- B7 ------------------------------- #
    def b7(self, duration=1, volume=100):
        pitch = 95
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- B8 ------------------------------- #
    def b8(self, duration=1, volume=100):
        pitch = 107
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    # ------------------------------- B9 ------------------------------- #
    def b9(self, duration=1, volume=100):
        pitch = 119
        self.MyMIDI.addNote(self.track, self.channel, pitch, self.time, duration, volume)
        self.time += duration

    def modify_time(self, duration=1, direction=0):
        if direction == 0:
            self.time += duration
        elif direction == 1:
            self.time -= duration
        else:
            print('Unknown Direction')

    def get_midi(self):
        return self.MyMIDI
