# Author: Authey
# Date: 20/07/2021

from MIDIMusicScales import Scales


class night_when_fireworks_flash:

    def __init__(self):
        self.name = 'A Night When Fireworks Flash.midi'
        self.sc = Scales(150)

    def generator(self):

        # ---- first bar ---- #
        self.sc.modify_time(4)
        self.sc.g5(4)

        # ---- second bar ---- #
        self.sc.a5(1)
        self.sc.e6(1)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(1)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(1)

        self.sc.modify_time(8, 1)

        self.sc.f3(1, 70)
        self.sc.c4(1, 70)
        self.sc.f4(1, 70)
        self.sc.g4(1, 70)
        self.sc.g3(1, 70)

        self.sc.modify_time(1, 1)

        self.sc.a4(1, 70)
        self.sc.d4(1, 70)
        self.sc.g4(2, 70)

        # ---- third bar ---- #
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(2)
        self.sc.a5(1)
        self.sc.g5(1)
        self.sc.e5(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.e3(1, 70)
        self.sc.b3(1, 70)
        self.sc.e4(2, 70)

        self.sc.modify_time(2, 1)

        self.sc.b4(2, 70)
        self.sc.a3(1, 70)
        self.sc.e4(1, 70)
        self.sc.a4(2, 70)

        # ---- forth bar ---- #
        self.sc.a5(1)
        self.sc.e6(2)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.g5(2)
        self.sc.f5(1)

        self.sc.modify_time(8, 1)

        self.sc.f3(1, 70)
        self.sc.c4(1, 70)
        self.sc.f4(1, 70)
        self.sc.g4(1, 70)
        self.sc.g3(1, 70)

        self.sc.modify_time(1, 1)

        self.sc.a4(1, 70)
        self.sc.d4(1, 70)
        self.sc.g4(1, 70)
        self.sc.f4(1, 70)

        # ---- fifth bar ---- #
        self.sc.e5(4)
        self.sc.e4(2)
        self.sc.e5(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.c3(1, 90)
        self.sc.g3(1, 90)
        self.sc.c4(1, 90)
        self.sc.d4(1, 90)
        self.sc.c3(1, 90)
        self.sc.c4(1, 90)
        self.sc.c4(2, 70)

        self.sc.modify_time(2, 1)

        self.sc.g4(2, 70)

        # ---- sixth bar ---- #
        self.sc.a5(1)
        self.sc.e6(1)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(1)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(1)

        self.sc.modify_time(8, 1)

        self.sc.f3(1, 70)
        self.sc.c4(1, 70)
        self.sc.f4(2, 70)
        self.sc.g3(1, 70)

        self.sc.modify_time(1, 1)

        self.sc.a4(1, 70)
        self.sc.d4(1, 70)
        self.sc.g4(2, 70)

        # ---- seventh bar ---- $
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.g6(2)

        self.sc.modify_time(1)

        self.sc.g5(1)
        self.sc.e5(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.e3(1, 70)
        self.sc.b3(1, 70)
        self.sc.e4(2, 70)

        self.sc.modify_time(2, 1)

        self.sc.b4(2, 70)
        self.sc.a3(1, 70)
        self.sc.e4(1, 70)
        self.sc.a4(1, 70)
        self.sc.b4(1, 70)

        # ---- eighth bar ---- #
        self.sc.a5(1)
        self.sc.e6(2)
        self.sc.g5(1)
        self.sc.a5(2)
        self.sc.e6(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.f3(1, 70)
        self.sc.c4(1, 70)
        self.sc.f4(1, 70)
        self.sc.g4(1, 70)
        self.sc.g3(1, 70)

        self.sc.modify_time(1, 1)

        self.sc.a4(1, 70)
        self.sc.d4(1, 70)
        self.sc.g4(2, 70)

        # ---- ninth bar ---- #
        self.sc.a5(4)

        self.sc.modify_time(2)

        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 90)
        self.sc.b3(1, 90)
        self.sc.c4(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(2, 70)

        # ---- tenth bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.d5(1)
        self.sc.c5(1)
        self.sc.b4(1)
        self.sc.b4(0.5)
        self.sc.c5(0.5)
        self.sc.b4(0.5)
        self.sc.g4(0.5)
        self.sc.e4(0.5)
        self.sc.g4(0.5)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- eleventh bar ---- #
        self.sc.d4(0.5)
        self.sc.g3(0.5)
        self.sc.e4(0.5)
        self.sc.g4(0.5)
        self.sc.d4(0.5)
        self.sc.g3(0.5)
        self.sc.b3(0.5)
        self.sc.c4(2.5)
        self.sc.a3(1)
        self.sc.c4(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 70)
        self.sc.b2(1, 70)
        self.sc.e3(2, 70)
        self.sc.a2(1, 70)
        self.sc.e3(1.5, 70)
        self.sc.e3(1.5, 70)

        # ---- twelfth bar ---- #
        self.sc.d4(1)
        self.sc.d4(0.5)
        self.sc.c4(0.5)
        self.sc.d4(1)
        self.sc.c4(0.5)

        self.sc.modify_time(0.5, 1)

        self.sc.e4(0.5)
        self.sc.a3(0.5)
        self.sc.g4(0.5)
        self.sc.d4(0.5)
        self.sc.g4(0.5)
        self.sc.a4(0.5)
        self.sc.b4(0.5)
        self.sc.d4(0.5)
        self.sc.a4(0.5)
        self.sc.g4(0.5)

        self.sc.modify_time(1, 1)

        self.sc.c5(0.5)
        self.sc.b4(0.5)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(0.5, 70)
        self.sc.f3(1.5, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- thirteenth bar ---- #
        self.sc.c4(2)

        self.sc.modify_time(2, 1)

        self.sc.e4(2)
        self.sc.e4(1)
        self.sc.e5(1)
        self.sc.d5(0.5)
        self.sc.e5(0.5)
        self.sc.c5(0.5)
        self.sc.d5(0.5)
        self.sc.b4(0.5)
        self.sc.c5(0.5)
        self.sc.g4(0.5)
        self.sc.e4(0.5)

        self.sc.modify_time(8, 1)

        self.sc.c3(1, 90)
        self.sc.g3(1, 90)
        self.sc.c4(1, 70)
        self.sc.e4(2, 70)
        self.sc.d4(1, 70)
        self.sc.c4(1, 70)
        self.sc.b3(1, 70)

        # ---- fourteenth bar ---- #
        self.sc.d4(0.5)
        self.sc.a3(0.5)
        self.sc.e4(1)
        self.sc.g4(1)
        self.sc.e4(0.5)
        self.sc.d4(1)
        self.sc.e4(0.5)
        self.sc.d4(1)
        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(0.5, 70)
        self.sc.g3(1, 70)
        self.sc.b3(0.5, 70)
        self.sc.c4(1, 70)

        # ---- fifteenth bar ---- #
        self.sc.d4(0.5)
        self.sc.g3(0.5)
        self.sc.e4(0.5)
        self.sc.g4(0.5)
        self.sc.d4(0.5)
        self.sc.g3(0.5)
        self.sc.b3(0.5)
        self.sc.c4(1)
        self.sc.g3(0.5)
        self.sc.a3(0.5)
        self.sc.g3(0.5)
        self.sc.a3(0.5)
        self.sc.c4(0.5)
        self.sc.d4(0.5)
        self.sc.e4(0.5)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 70)
        self.sc.b2(1, 70)
        self.sc.e3(1, 70)
        self.sc.e3(0.5, 70)
        self.sc.g3(0.5, 70)
        self.sc.a2(1, 70)
        self.sc.e3(1.5, 70)
        self.sc.a3(0.5, 70)
        self.sc.b3(0.5, 70)
        self.sc.c4(0.5, 70)

        # ---- sixteenth bar ---- #
        self.sc.a3(0.5)
        self.sc.g3(0.5)
        self.sc.a3(1)
        self.sc.g3(1)
        self.sc.a3(0.5)
        self.sc.d4(1)
        self.sc.c4(0.5)
        self.sc.d4(0.5)
        self.sc.c4(0.5)
        self.sc.a3(1)
        self.sc.g3(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1.5, 70)
        self.sc.d3(1.5, 70)

        # ---- seventeenth bar ---- #
        self.sc.a3(2)

        self.sc.modify_time(4)

        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 90)
        self.sc.b3(1, 90)
        self.sc.c4(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(2, 70)

        # ---- eighteenth bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.d5(1)
        self.sc.c5(1)
        self.sc.b4(1)
        self.sc.b4(0.5)
        self.sc.c5(0.5)
        self.sc.b4(0.5)
        self.sc.g4(0.5)
        self.sc.e4(0.5)
        self.sc.g4(0.5)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- nineteenth bar ---- #
        self.sc.d4(0.5)
        self.sc.g3(0.5)
        self.sc.e4(0.5)
        self.sc.g4(0.5)
        self.sc.d4(0.5)
        self.sc.g3(0.5)
        self.sc.b3(0.5)
        self.sc.c4(2.5)
        self.sc.a3(1)
        self.sc.c4(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 70)
        self.sc.b2(1, 70)
        self.sc.e3(2, 70)
        self.sc.a2(1, 70)
        self.sc.e3(1.5, 70)
        self.sc.e3(1.5, 70)

        # ---- twentieth bar ---- #
        self.sc.d4(1)
        self.sc.d4(0.5)
        self.sc.c4(0.5)
        self.sc.d4(1)
        self.sc.c4(0.5)

        self.sc.modify_time(0.5, 1)

        self.sc.e4(0.5)
        self.sc.a3(0.5)
        self.sc.g4(0.5)
        self.sc.d4(0.5)
        self.sc.g4(0.5)
        self.sc.a4(0.5)
        self.sc.b4(0.5)
        self.sc.d4(0.5)
        self.sc.a4(0.5)
        self.sc.g4(0.5)

        self.sc.modify_time(1, 1)

        self.sc.c5(0.5)
        self.sc.b4(0.5)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(0.5, 70)
        self.sc.f3(1.5, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- twenty-first bar ---- #
        self.sc.c4(2)

        self.sc.modify_time(2, 1)

        self.sc.e4(2)

        self.sc.modify_time(4)

        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.c3(1, 90)
        self.sc.g3(1, 90)
        self.sc.c4(1, 90)
        self.sc.e4(2, 90)
        self.sc.d4(1, 90)
        self.sc.c4(1, 70)
        self.sc.b3(1, 70)

        # ---- twenty-second bar ---- #
        self.sc.d4(1)
        self.sc.e4(1)
        self.sc.g4(1)
        self.sc.e4(0.5)
        self.sc.d4(1)
        self.sc.e4(0.5)
        self.sc.d4(3)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(0.5, 70)
        self.sc.g3(0.5, 70)
        self.sc.e3(1, 70)
        self.sc.g3(1, 70)

        # ---- twenty-third bar ---- #
        self.sc.d4(0.5)
        self.sc.g3(0.5)
        self.sc.e4(0.5)
        self.sc.g4(0.5)
        self.sc.d4(0.5)
        self.sc.g3(0.5)
        self.sc.b3(0.5)
        self.sc.c4(1)
        self.sc.g3(0.5)
        self.sc.a3(0.5)
        self.sc.g3(0.5)
        self.sc.a3(0.5)
        self.sc.c4(0.5)
        self.sc.d4(0.5)
        self.sc.e4(0.5)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 70)
        self.sc.b2(1, 70)
        self.sc.e3(1, 70)
        self.sc.e3(0.5, 70)
        self.sc.g3(0.5, 70)
        self.sc.a2(1, 70)
        self.sc.e3(1.5, 70)
        self.sc.a3(0.5, 70)
        self.sc.b3(0.5, 70)
        self.sc.c4(0.5, 70)

        # ---- twenty-fourth bar ---- #
        self.sc.a3(0.5)
        self.sc.g3(0.5)
        self.sc.a3(1)
        self.sc.g3(1)
        self.sc.a3(0.5)
        self.sc.d4(1)
        self.sc.c4(0.5)
        self.sc.d4(0.5)
        self.sc.c4(0.5)
        self.sc.a3(1)
        self.sc.g3(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1.5, 70)
        self.sc.d3(1.5, 70)

        # ---- twenty-fifth bar ---- #
        self.sc.a3(2)

        self.sc.modify_time(4)

        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.a2(1, 70)
        self.sc.e3(1, 70)
        self.sc.a3(1, 70)
        self.sc.b3(1, 70)
        self.sc.c4(4, 70)

        # ---- twenty-sixth bar ---- #
        self.sc.a4(2)
        self.sc.e5(2)
        self.sc.g4(2)
        self.sc.a4(2)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 90)
        self.sc.c3(1, 90)
        self.sc.f3(2, 90)
        self.sc.g2(1, 90)
        self.sc.d3(1, 90)
        self.sc.g3(2, 90)

        # ---- twenty-seventh bar ---- #
        self.sc.e5(2)
        self.sc.g4(2)
        self.sc.a4(2)
        self.sc.e5(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 90)
        self.sc.b2(1, 90)
        self.sc.g3(2, 90)
        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 70)
        self.sc.b3(1, 70)

        # ---- twenty-eighth bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.d5(1)
        self.sc.c5(1)
        self.sc.d5(1)
        self.sc.g4(1)
        self.sc.c5(1)
        self.sc.d5(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)

        self.sc.modify_time(2, 1)

        self.sc.a3(2, 70)
        self.sc.g2(2, 70)
        self.sc.d3(1, 70)
        self.sc.g3(1, 70)

        # ---- twenty-ninth bar ---- #
        self.sc.e5(4)

        self.sc.modify_time(2)

        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.c3(1, 90)
        self.sc.g3(1, 90)
        self.sc.c4(1, 90)
        self.sc.d4(1, 90)
        self.sc.e4(2, 70)

        self.sc.modify_time(2)

        # ---- thirtieth bar ---- #
        self.sc.a4(4)
        self.sc.g4(4)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 90)
        self.sc.c3(1, 90)
        self.sc.f3(2, 90)
        self.sc.g2(1, 90)
        self.sc.d3(1, 90)
        self.sc.g3(2, 90)

        # ---- thirty-first bar ---- #
        self.sc.a4(3)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.g4(1)
        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 70)
        self.sc.b2(1, 70)
        self.sc.e3(1, 70)
        self.sc.g3(1, 70)
        self.sc.a2(1, 70)
        self.sc.e3(1, 70)
        self.sc.a3(1, 70)
        self.sc.b3(1, 70)

        # ---- thirty-second bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.a4(1)
        self.sc.g4(1)
        self.sc.a4(3)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- thirty-third bar ---- #
        self.sc.a3(4)

        self.sc.modify_time(2)

        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 90)
        self.sc.b3(1, 90)
        self.sc.c4(4, 90)

        # ---- thirty-fourth bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.e5(2)
        self.sc.g4(2)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 90)
        self.sc.d3(1, 90)
        self.sc.g3(2, 90)

        # ---- thirty-fifth bar ---- #
        self.sc.e5(2)
        self.sc.g4(2)
        self.sc.a4(2)
        self.sc.e5(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 90)
        self.sc.b2(1, 90)
        self.sc.g3(2, 90)
        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 70)
        self.sc.b3(1, 70)

        # ---- thirty-sixth bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.d5(1)
        self.sc.c5(1)
        self.sc.d5(1)
        self.sc.g4(1)
        self.sc.c5(1)
        self.sc.d5(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)

        self.sc.modify_time(2, 1)

        self.sc.a3(2, 70)
        self.sc.g2(2, 70)
        self.sc.d3(1, 70)
        self.sc.g3(1, 70)

        # ---- thirty-seventh bar ---- #
        self.sc.e5(4)

        self.sc.modify_time(2)

        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.c3(1, 90)
        self.sc.g3(1, 90)
        self.sc.c4(1, 90)
        self.sc.d4(1, 90)
        self.sc.e4(2, 70)

        self.sc.modify_time(2)

        # ---- thirty-eighth bar ---- #
        self.sc.a4(2)
        self.sc.e5(2)
        self.sc.b4(2)
        self.sc.c5(1)
        self.sc.d5(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 90)
        self.sc.c3(1, 90)
        self.sc.f3(2, 90)
        self.sc.g2(1, 90)
        self.sc.d3(1, 90)
        self.sc.g3(2, 70)

        # ---- thirty-ninth bar ---- #
        self.sc.e5(2)
        self.sc.b4(2)
        self.sc.e4(1)

        self.sc.modify_time(1, 1)

        self.sc.g4(1)

        self.sc.modify_time(1, 1)

        self.sc.d5(1)
        self.sc.c5(1)
        self.sc.b4(1)
        self.sc.c5(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 90)
        self.sc.b2(1, 90)
        self.sc.e3(1, 90)
        self.sc.g3(1, 90)
        self.sc.a2(1, 70)
        self.sc.e3(1, 70)
        self.sc.a3(1, 70)
        self.sc.b3(1, 70)

        # ---- fortieth bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.a4(1)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.a4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- forty-first bar ---- #
        self.sc.a3(4)

        self.sc.modify_time(2)

        self.sc.e5(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 90)
        self.sc.b3(1, 90)
        self.sc.c4(4, 90)

        # ---- forty-second bar ---- #
        self.sc.a5(1)
        self.sc.e6(1)
        self.sc.d6(1)
        self.sc.c6(1)
        self.sc.d5(2)

        self.sc.modify_time(2, 1)

        self.sc.g5(2)

        self.sc.modify_time(2, 1)

        self.sc.b5(2)
        self.sc.a5(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 90)
        self.sc.d3(1, 90)
        self.sc.g3(2, 70)

        # ---- forty-third bar ---- #
        self.sc.c5(2)

        self.sc.modify_time(2, 1)

        self.sc.e5(2)
        self.sc.e5(1.5)

        self.sc.modify_time(1.5, 1)

        self.sc.g5(1.5)
        self.sc.e4(2.5)

        self.sc.modify_time(2.5, 1)

        self.sc.c5(2.5)
        self.sc.a4(1)
        self.sc.c5(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 90)
        self.sc.b2(1, 90)
        self.sc.e3(2, 70)
        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(2, 70)

        # ---- forty-fourth bar ---- #
        self.sc.f4(2)

        self.sc.modify_time(2, 1)

        self.sc.d5(2)
        self.sc.d5(1)
        self.sc.c5(1)

        self.sc.modify_time(1, 1)

        self.sc.e5(1)
        self.sc.b4(1)

        self.sc.modify_time(1, 1)

        self.sc.g5(1)
        self.sc.g5(0.5)
        self.sc.a5(0.5)

        self.sc.b5(1)
        self.sc.a5(0.5)
        self.sc.g5(0.5)

        self.sc.modify_time(1, 1)

        self.sc.c6(0.5)
        self.sc.b5(0.5)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 90)
        self.sc.c3(1, 90)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- forty-fifth bar ---- #
        self.sc.c5(1)

        self.sc.modify_time(1, 1)

        self.sc.e5(1)
        self.sc.g4(1)
        self.sc.e5(1)
        self.sc.e6(1)
        self.sc.d6(0.5)
        self.sc.e6(0.5)
        self.sc.c6(0.5)
        self.sc.d6(0.5)
        self.sc.b5(0.5)
        self.sc.c6(0.5)
        self.sc.g5(0.5)
        self.sc.e5(0.5)

        self.sc.modify_time(8, 1)

        self.sc.c3(1, 70)
        self.sc.g3(1, 70)
        self.sc.c4(1, 70)
        self.sc.e4(2, 70)
        self.sc.d4(1, 70)
        self.sc.c3(1, 70)
        self.sc.b2(1, 70)

        self.sc.modify_time(2, 1)

        self.sc.c4(1, 70)
        self.sc.b3(1, 70)

        # ---- forty-sixth bar ---- #
        self.sc.d5(0.5)
        self.sc.a4(0.5)
        self.sc.e5(1)
        self.sc.c5(1)

        self.sc.modify_time(1, 1)

        self.sc.g5(1)
        self.sc.e5(0.5)
        self.sc.d5(1)

        self.sc.modify_time(0.5, 1)

        self.sc.g4(0.5)
        self.sc.e5(0.5)
        self.sc.d5(0.5)
        self.sc.g4(0.5)
        self.sc.e5(0.5)
        self.sc.b4(0.5)
        self.sc.c5(1)

        self.sc.modify_time(1, 1)

        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- forty-seventh bar ---- #
        self.sc.d5(0.5)
        self.sc.g4(0.5)
        self.sc.e5(0.5)
        self.sc.g5(0.5)
        self.sc.d5(0.5)
        self.sc.g4(0.5)
        self.sc.e4(0.5)
        self.sc.g4(1)

        self.sc.modify_time(1.5, 1)

        self.sc.b4(0.5)
        self.sc.c5(1)
        self.sc.g4(0.5)
        self.sc.a4(0.5)
        self.sc.g4(0.5)
        self.sc.a4(0.5)
        self.sc.a4(0.5)
        self.sc.b4(0.5)
        self.sc.c5(0.5)

        self.sc.modify_time(1.5, 1)

        self.sc.c5(0.5)
        self.sc.d5(0.5)
        self.sc.e5(0.5)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 70)
        self.sc.b2(1, 70)
        self.sc.e3(2, 70)
        self.sc.a2(1, 70)
        self.sc.e3(1, 70)
        self.sc.a3(2, 70)

        # ---- forty-eighth bar ---- #
        self.sc.a4(0.5)
        self.sc.g4(0.5)
        self.sc.a4(1)
        self.sc.g4(1)
        self.sc.a4(0.5)
        self.sc.d5(1)
        self.sc.c5(0.5)
        self.sc.d5(0.5)
        self.sc.c5(0.5)
        self.sc.a4(0.5)
        self.sc.d4(0.5)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- forty-ninth bar ---- #
        self.sc.a3(4)

        self.sc.modify_time(2)

        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 90)
        self.sc.b3(1, 90)
        self.sc.c4(4, 90)

        # ---- fiftieth bar ---- #
        self.sc.a4(2)
        self.sc.e5(2)
        self.sc.g4(2)
        self.sc.a4(2)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 90)
        self.sc.c3(1, 90)
        self.sc.f3(2, 90)
        self.sc.g2(1, 90)
        self.sc.d3(1, 90)
        self.sc.g3(2, 90)

        # ---- fifty-first bar ---- #
        self.sc.e5(2)
        self.sc.g4(2)
        self.sc.a4(2)
        self.sc.e5(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 90)
        self.sc.b2(1, 90)
        self.sc.g3(2, 90)
        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 70)
        self.sc.b3(1, 70)

        # ---- fifty-third bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.d5(1)
        self.sc.c5(1)
        self.sc.d5(1)
        self.sc.g4(1)
        self.sc.c5(1)
        self.sc.d5(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)

        self.sc.modify_time(2, 1)

        self.sc.a3(2, 70)
        self.sc.g2(2, 70)
        self.sc.d3(1, 70)
        self.sc.g3(1, 70)

        # ---- fifty-third bar ---- #
        self.sc.e5(4)

        self.sc.modify_time(2)

        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.c3(1, 90)
        self.sc.g3(1, 90)
        self.sc.c4(1, 90)
        self.sc.d4(1, 90)
        self.sc.e4(2, 70)

        self.sc.modify_time(2)

        # ---- fifty-fourth bar ---- #
        self.sc.a4(2)
        self.sc.e5(2)
        self.sc.b4(2)
        self.sc.c5(1)
        self.sc.d5(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 90)
        self.sc.c3(1, 90)
        self.sc.f3(2, 90)
        self.sc.g2(1, 90)
        self.sc.d3(1, 90)
        self.sc.g3(2, 70)

        # ---- fifty-fifth bar ---- #
        self.sc.e5(2)
        self.sc.b4(2)
        self.sc.e4(1)

        self.sc.modify_time(1, 1)

        self.sc.g4(1)

        self.sc.modify_time(1, 1)

        self.sc.d5(1)
        self.sc.c5(1)
        self.sc.b4(1)
        self.sc.c5(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 90)
        self.sc.b2(1, 90)
        self.sc.e3(1, 90)
        self.sc.g3(1, 90)
        self.sc.a2(1, 70)
        self.sc.e3(1, 70)
        self.sc.a3(1, 70)
        self.sc.b3(1, 70)

        # ---- fifty-sixth bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.a4(1)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.a4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- fifty-seventh bar ---- #
        self.sc.a3(4)

        self.sc.modify_time(2)

        self.sc.e5(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 90)
        self.sc.b3(1, 90)
        self.sc.c4(4, 90)

        # ---- fifty-eighth bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.e5(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- fifty-ninth bar ---- #
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.e5(2)
        self.sc.a4(1)
        self.sc.g4(1)
        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 70)
        self.sc.b2(1, 70)
        self.sc.e3(2, 70)
        self.sc.a2(1, 70)
        self.sc.e3(1, 70)
        self.sc.a3(2, 70)

        # ---- sixtieth bar ---- #
        self.sc.a4(1)
        self.sc.e5(2)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.g4(2)
        self.sc.f4(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- sixty-first bar ---- #
        self.sc.e4(3)
        self.sc.d4(1)
        self.sc.e4(1)
        self.sc.d4(1)
        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.c3(1, 70)
        self.sc.g3(1, 70)
        self.sc.c4(6, 70)

        # ---- sixty-second bar ---- #
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.e5(1)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.e5(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(2, 70)

        # ---- sixty-third bar ---- #
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.g5(2)
        self.sc.a4(1)
        self.sc.g4(1)
        self.sc.e4(1)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.e2(1, 70)
        self.sc.b2(1, 70)
        self.sc.e3(2, 70)
        self.sc.a2(1, 70)
        self.sc.e3(1, 70)
        self.sc.a3(2, 70)

        # ---- sixty-fourth bar ---- #
        self.sc.a4(1)
        self.sc.e5(2)
        self.sc.g4(1)
        self.sc.a4(1)
        self.sc.e5(2)
        self.sc.g4(1)

        self.sc.modify_time(8, 1)

        self.sc.f2(1, 70)
        self.sc.c3(1, 70)
        self.sc.f3(2, 70)
        self.sc.g2(1, 70)
        self.sc.d3(1, 70)
        self.sc.g3(1, 70)
        self.sc.b3(1, 70)

        # ---- sixty-fifth bar ---- #
        self.sc.a3(4)

        self.sc.modify_time(2)

        self.sc.g5(2)

        self.sc.modify_time(8, 1)

        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 90)
        self.sc.b3(1, 90)
        self.sc.c4(4, 90)

        # ---- sixty-sixth bar ---- #
        self.sc.a5(1)
        self.sc.e6(1)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(1)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(1)

        self.sc.modify_time(8, 1)

        self.sc.f3(1, 70)
        self.sc.c4(1, 70)
        self.sc.f4(1, 70)
        self.sc.g4(1, 70)
        self.sc.g3(1, 70)

        self.sc.modify_time(1, 1)

        self.sc.a4(1, 70)
        self.sc.d4(1, 70)
        self.sc.g4(2, 70)

        # ---- sixty-seventh bar ---- #
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(2)
        self.sc.a5(1)
        self.sc.g5(1)
        self.sc.e5(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.e3(1, 70)
        self.sc.b3(1, 70)
        self.sc.e4(2, 70)

        self.sc.modify_time(2, 1)

        self.sc.b4(2, 70)
        self.sc.a3(1, 70)
        self.sc.e4(1, 70)
        self.sc.a4(2, 70)

        # ---- sixty-eighth bar ---- #
        self.sc.a5(1)
        self.sc.e6(2)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.g5(2)
        self.sc.f5(1)

        self.sc.modify_time(8, 1)

        self.sc.f3(1, 70)
        self.sc.c4(1, 70)
        self.sc.f4(1, 70)
        self.sc.g4(1, 70)
        self.sc.g3(1, 70)

        self.sc.modify_time(1, 1)

        self.sc.a4(1, 70)
        self.sc.d4(1, 70)
        self.sc.g4(1, 70)
        self.sc.f4(1, 70)

        # ---- sixty-ninth bar ---- #
        self.sc.e5(4)
        self.sc.e4(2)
        self.sc.e5(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.c3(1, 90)
        self.sc.g3(1, 90)
        self.sc.c4(1, 90)
        self.sc.d4(1, 90)
        self.sc.c3(1, 90)
        self.sc.c4(1, 90)
        self.sc.c4(2, 70)

        self.sc.modify_time(2, 1)

        self.sc.g4(2, 70)

        # ---- seventieth bar ---- #
        self.sc.a5(1)
        self.sc.e6(1)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(1)
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.e6(1)

        self.sc.modify_time(8, 1)

        self.sc.f3(1, 70)
        self.sc.c4(1, 70)
        self.sc.f4(2, 70)
        self.sc.g3(1, 70)

        self.sc.modify_time(1, 1)

        self.sc.a4(1, 70)
        self.sc.d4(1, 70)
        self.sc.g4(2, 70)

        # ---- seventy-first bar ---- #
        self.sc.g5(1)
        self.sc.a5(1)
        self.sc.g6(2)

        self.sc.modify_time(1)

        self.sc.g5(1)
        self.sc.e5(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.e3(1, 70)
        self.sc.b3(1, 70)
        self.sc.e4(2, 70)

        self.sc.modify_time(2, 1)

        self.sc.b4(2, 70)
        self.sc.a3(1, 70)
        self.sc.e4(1, 70)
        self.sc.a4(1, 70)
        self.sc.b4(1, 70)

        # ---- seventy-second bar ---- #
        self.sc.a5(1)
        self.sc.e6(2)
        self.sc.g5(1)
        self.sc.a5(2)
        self.sc.e6(1)
        self.sc.g5(1)

        self.sc.modify_time(8, 1)

        self.sc.f3(1, 70)
        self.sc.c4(1, 70)
        self.sc.f4(1, 90)
        self.sc.g4(1, 70)
        self.sc.g3(1, 70)

        self.sc.modify_time(1, 1)

        self.sc.a4(1, 70)
        self.sc.d4(1, 90)
        self.sc.g4(2, 70)

        # ---- seventy-third bar ---- #
        self.sc.a5(8)

        self.sc.modify_time(8, 1)

        self.sc.a2(1, 90)
        self.sc.e3(1, 90)
        self.sc.a3(1, 80)
        self.sc.b3(1, 80)
        self.sc.c4(4, 70)

        with open(self.name, 'wb') as f:
            self.sc.get_midi().writeFile(f)
        return self.name
