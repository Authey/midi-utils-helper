# Author: Authey
# Date: 11/06/2020


from Scales import Scales


class sakura_tears:

    def __init__(self):
        self.name = 'SakuraTears'
        self.sakura_tears = Scales(220)

    def generator(self):
        # ------------------------ start ------------------------ #
        # ---------------- first bar ---------------- #
        self.sakura_tears.modify_time(4)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------------------- repeat part -------------------- #
        for i in range(0, 2):
            # ---------------- second bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.a5(2)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(2)
            self.sakura_tears.g5(1)
            self.sakura_tears.d5(1)
            self.sakura_tears.e5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.f3(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.f4(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.e3(1)
            self.sakura_tears.d4(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.d4(1)
            # ---------------- third bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.modify_time(3)
            self.sakura_tears.e5(1)
            self.sakura_tears.c6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.c4(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            # ---------------- fourth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.a5(2)
            self.sakura_tears.a5(1)
            self.sakura_tears.e6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.c6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.b5(2)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(9, 1)
            # -------- minor -------- #
            self.sakura_tears.f3(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.f4(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.e3(1)
            self.sakura_tears.d4(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.d4(1)
            # ---------------- fifth bar ---------------- #
            # -------- modify time -------- #
            self.sakura_tears.modify_time(1)
            # -------- major -------- #
            self.sakura_tears.c6(2)
            self.sakura_tears.c6(0.5)
            self.sakura_tears.c6(0.5)
            self.sakura_tears.c6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.a3(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.c5(2)
            # ----------------sixth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.a5(2)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(2)
            self.sakura_tears.g5(1)
            self.sakura_tears.d5(1)
            self.sakura_tears.e5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.f3(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.f4(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.e3(1)
            self.sakura_tears.d4(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.d4(1)
            # ---------------- seventh bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.modify_time(3)
            self.sakura_tears.e5(1)
            self.sakura_tears.c6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.c4(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            # ---- differential ---- #
            if i == 0:
                # ---------------- eighth bar ---------------- #
                # -------- major -------- #
                self.sakura_tears.a5(2)
                self.sakura_tears.a5(1)
                self.sakura_tears.e6(1)
                self.sakura_tears.b5(1)
                self.sakura_tears.c6(1)
                self.sakura_tears.b5(1)
                self.sakura_tears.b5(2)
                # -------- modify time -------- #
                self.sakura_tears.modify_time(9, 1)
                # -------- minor -------- #
                self.sakura_tears.f3(1)
                self.sakura_tears.c4(1)
                self.sakura_tears.f4(1)
                self.sakura_tears.c4(1)
                self.sakura_tears.e3(1)
                self.sakura_tears.d4(1)
                self.sakura_tears.e4(1)
                self.sakura_tears.d4(1)
                # ---------------- ninth bar ---------------- #
                # -------- modify time -------- #
                self.sakura_tears.modify_time(1)
                # -------- major -------- #
                self.sakura_tears.c6(3)
                self.sakura_tears.c6(1)
                self.sakura_tears.b5(1)
                self.sakura_tears.a5(1)
                self.sakura_tears.g5(1)
                # -------- modify time -------- #
                self.sakura_tears.modify_time(8, 1)
                # -------- minor -------- #
                self.sakura_tears.a3(1)
                self.sakura_tears.e4(1)
                self.sakura_tears.c5(2)
                self.sakura_tears.modify_time(4)
            # ---- differential ---- #
            else:
                # ---------------- tenth bar ---------------- #
                # -------- major -------- #
                self.sakura_tears.a5(2)
                self.sakura_tears.a5(1)
                self.sakura_tears.e6(1)
                self.sakura_tears.b5(1)
                self.sakura_tears.c6(1)
                self.sakura_tears.b5(1)
                self.sakura_tears.b5(2)
                # -------- modify time -------- #
                self.sakura_tears.modify_time(9, 1)
                # -------- minor -------- #
                self.sakura_tears.f3(1)
                self.sakura_tears.c4(1)
                self.sakura_tears.f4(1)
                self.sakura_tears.c4(1)
                self.sakura_tears.e3(1)
                self.sakura_tears.d4(1)
                self.sakura_tears.e4(1)
                self.sakura_tears.d4(1)
        # ---------------- eleventh bar ---------------- #
        # -------- modify time -------- #
        self.sakura_tears.modify_time(1)
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c7(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        self.sakura_tears.modify_time(3)
        self.sakura_tears.g3(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(4, 1)
        # -------- other -------- #
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # -------------------- repeat part -------------------- #
        for i in range(0, 2):
            # ---------------- twelfth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.a5(2)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(2)
            self.sakura_tears.g5(1)
            self.sakura_tears.d5(1)
            self.sakura_tears.e5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.f3(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.f4(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.e3(1)
            self.sakura_tears.d4(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.d4(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- other -------- #
            self.sakura_tears.a6(2)
            self.sakura_tears.a6(1)
            self.sakura_tears.g6(2)
            self.sakura_tears.g6(1)
            self.sakura_tears.d6(1)
            self.sakura_tears.e6(1)
            # ---------------- thirteenth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.modify_time(3)
            self.sakura_tears.e5(1)
            self.sakura_tears.c6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.c4(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(5, 1)
            # -------- other -------- #
            self.sakura_tears.e6(1)
            self.sakura_tears.c7(1)
            self.sakura_tears.b6(1)
            self.sakura_tears.a6(1)
            self.sakura_tears.g6(1)
            # ---------------- fourteenth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.a5(2)
            self.sakura_tears.a5(1)
            self.sakura_tears.e6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.c6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.b5(2)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(9, 1)
            # -------- minor -------- #
            self.sakura_tears.f3(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.f4(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.e3(1)
            self.sakura_tears.d4(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.d4(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- other -------- #
            self.sakura_tears.a6(2)
            self.sakura_tears.a6(1)
            self.sakura_tears.e7(1)
            self.sakura_tears.b6(1)
            self.sakura_tears.c7(1)
            self.sakura_tears.b6(1)
            self.sakura_tears.b6(2)
            # ---------------- fifteenth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.c6(2)
            self.sakura_tears.c6(0.5)
            self.sakura_tears.c6(0.5)
            self.sakura_tears.c6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.a3(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.c5(2)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(7, 1)
            # -------- other -------- #
            self.sakura_tears.c7(2)
            self.sakura_tears.c7(0.5)
            self.sakura_tears.c7(0.5)
            self.sakura_tears.c7(1)
            self.sakura_tears.b6(1)
            self.sakura_tears.a6(1)
            self.sakura_tears.g6(1)
            # ---------------- sixteenth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.a5(2)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(2)
            self.sakura_tears.g5(1)
            self.sakura_tears.d5(1)
            self.sakura_tears.e5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.f3(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.f4(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.e3(1)
            self.sakura_tears.d4(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.d4(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- other -------- #
            self.sakura_tears.a6(2)
            self.sakura_tears.a6(1)
            self.sakura_tears.g6(2)
            self.sakura_tears.g6(1)
            self.sakura_tears.d6(1)
            self.sakura_tears.e6(1)
            # ---------------- seventeenth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.modify_time(3)
            self.sakura_tears.e5(1)
            self.sakura_tears.c6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.c4(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            self.sakura_tears.c5(1)
            self.sakura_tears.g4(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(5, 1)
            # -------- other -------- #
            self.sakura_tears.e6(1)
            self.sakura_tears.c7(1)
            self.sakura_tears.b6(1)
            self.sakura_tears.a6(1)
            self.sakura_tears.g6(1)
            # ---------------- eighteenth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.a5(2)
            self.sakura_tears.a5(1)
            self.sakura_tears.e6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.d6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.b5(2)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(9, 1)
            # -------- minor -------- #
            self.sakura_tears.f3(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.f4(1)
            self.sakura_tears.c4(1)
            self.sakura_tears.e3(1)
            self.sakura_tears.d4(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.d4(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- other -------- #
            self.sakura_tears.a6(2)
            self.sakura_tears.a6(1)
            self.sakura_tears.e7(1)
            self.sakura_tears.b6(1)
            self.sakura_tears.d7(1)
            self.sakura_tears.b6(1)
            self.sakura_tears.b6(2)
            # ---------------- nineteenth bar ---------------- #
            # -------- major -------- #
            self.sakura_tears.c6(2)
            self.sakura_tears.c7(1)
            self.sakura_tears.c6(1)
            self.sakura_tears.b5(1)
            self.sakura_tears.a5(1)
            self.sakura_tears.g5(1)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(8, 1)
            # -------- minor -------- #
            self.sakura_tears.a3(1)
            self.sakura_tears.e4(1)
            self.sakura_tears.c5(2)
            self.sakura_tears.modify_time(4)
            # -------- modify time -------- #
            self.sakura_tears.modify_time(7, 1)
            # -------- other -------- #
            self.sakura_tears.c7(2)
            self.sakura_tears.c7(1)
            self.sakura_tears.c7(1)
            self.sakura_tears.b6(1)
            self.sakura_tears.a6(1)
            self.sakura_tears.g6(1)
        # ---------------- twentieth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- twenty-first bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- twenty-second bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- twenty-third bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.c7(2)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- twenty-fourth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- twenty-fifth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- twenty-sixth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.d7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- twenty-seventh bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c7(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        self.sakura_tears.modify_time(4)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.c7(2)
        self.sakura_tears.c7(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- twenty-eighth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- twenty-ninth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- thirtieth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- thirty-first bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.c7(2)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- thirty-second bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- thirty-third bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- thirty-fourth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.d7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- thirty-fifth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(1)
        self.sakura_tears.c6(2)
        self.sakura_tears.modify_time(2)
        self.sakura_tears.c6(1)
        self.sakura_tears.d6(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        self.sakura_tears.modify_time(4)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(1, 1)
        # -------- other -------- #
        self.sakura_tears.a6(1)
        self.sakura_tears.modify_time(6)
        # ---------------- thirty-sixth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.e6(2)
        self.sakura_tears.e6(2)
        self.sakura_tears.d6(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # ---------------- thirty-seventh bar ---------------- #
        # -------- modify time -------- #
        self.sakura_tears.modify_time(1)
        # --------major -------- #
        self.sakura_tears.c6(3)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # ---------------- thirty-eighth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.d6(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # ---------------- thirty-ninth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(3)
        self.sakura_tears.f6(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.c6(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # ---------------- forty bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(2)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # ---------------- forty-first bar ---------------- #
        # -------- modify time -------- #
        self.sakura_tears.modify_time(1)
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # ---------------- forty-second bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.f5(4)
        self.sakura_tears.d5(3)
        self.sakura_tears.e5(4)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(11, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(4)
        self.sakura_tears.g3(3)
        self.sakura_tears.c4(5)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(12, 1)
        # -------- other -------- #
        self.sakura_tears.a5(4)
        self.sakura_tears.g5(3)
        self.sakura_tears.g5(4)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(11, 1)
        # -------- other -------- #
        self.sakura_tears.c6(4)
        self.sakura_tears.b5(3)
        self.sakura_tears.c6(4)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(11, 1)
        # -------- minor -------- #
        self.sakura_tears.f4(4)
        self.sakura_tears.g4(3)
        self.sakura_tears.c5(5)
        # ---------------- forty-third bar ---------------- #
        # -------- modify time -------- #
        self.sakura_tears.modify_time(1, 1)
        # -------- major -------- #
        self.sakura_tears.c7(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(4, 1)
        # -------- minor -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.g3(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(4, 1)
        # -------- other -------- #
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- forty-fourth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- forty-fifth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- forty-sixth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- forty-seventh bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.c7(2)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- forty-eighth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- forty-ninth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- fiftieth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.d7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- fifty-first bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c7(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        self.sakura_tears.modify_time(4)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.c7(2)
        self.sakura_tears.c7(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- fifty-second bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- fifty-third bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- fifty-fourth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- fifty-fifth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.c7(2)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- fifty-sixth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- fifty-seventh bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- fifty-eighth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.d7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- fifty-ninth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(1)
        self.sakura_tears.c6(2)
        self.sakura_tears.e5(2)
        self.sakura_tears.e5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        self.sakura_tears.modify_time(4)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.modify_time(2)
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.a6(1)
        self.sakura_tears.modify_time(2)
        self.sakura_tears.c6(2)
        self.sakura_tears.c6(2)
        # ---------------- sixtieth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.d6(1)
        self.sakura_tears.d6s(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(2, 1)
        # -------- minor -------- #
        self.sakura_tears.modify_time(1)
        self.sakura_tears.a3(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.d7(1)
        self.sakura_tears.d7s(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        # ---------------- sixty-first bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- sixty-second bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- sixty-third bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- sixty-fourth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.c7(2)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- sixty-fifth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- sixty-sixth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- sixty-seventh bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.d7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- sixty-eighth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c7(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(3, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.modify_time(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- sixty-ninth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- seventy bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- seventy-first bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- seventy-second bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(2)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(0.5)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.c7(2)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(0.5)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- seventy-third bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(2)
        self.sakura_tears.g5(1)
        self.sakura_tears.d5(1)
        self.sakura_tears.e5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(2)
        self.sakura_tears.g6(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.e6(1)
        # ---------------- seventy-fourth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.modify_time(3)
        self.sakura_tears.e5(1)
        self.sakura_tears.c6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.a5(1)
        self.sakura_tears.g5(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.c4(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        self.sakura_tears.c5(1)
        self.sakura_tears.g4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(5, 1)
        # -------- other -------- #
        self.sakura_tears.e6(1)
        self.sakura_tears.c7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.a6(1)
        self.sakura_tears.g6(1)
        # ---------------- seventy-fifth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.a5(2)
        self.sakura_tears.a5(1)
        self.sakura_tears.e6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.d6(1)
        self.sakura_tears.b5(1)
        self.sakura_tears.b5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(9, 1)
        # -------- minor -------- #
        self.sakura_tears.f3(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.f4(1)
        self.sakura_tears.c4(1)
        self.sakura_tears.e3(1)
        self.sakura_tears.d4(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.d4(1)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- other -------- #
        self.sakura_tears.a6(2)
        self.sakura_tears.a6(1)
        self.sakura_tears.e7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.d7(1)
        self.sakura_tears.b6(1)
        self.sakura_tears.b6(2)
        # ---------------- seventy-sixth bar ---------------- #
        # -------- major -------- #
        self.sakura_tears.c6(3)
        self.sakura_tears.a5(2)
        self.sakura_tears.c5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(8, 1)
        # -------- minor -------- #
        self.sakura_tears.a3(1)
        self.sakura_tears.e4(1)
        self.sakura_tears.c5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(3, 1)
        # -------- other -------- #
        self.sakura_tears.e6(3)
        self.sakura_tears.c6(2)
        self.sakura_tears.a5(2)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(7, 1)
        # -------- other -------- #
        self.sakura_tears.a6(3)
        self.sakura_tears.modify_time(4)
        # ---------------- seventy-seventh bar ---------------- #
        # -------- minor -------- #
        self.sakura_tears.a3(4)
        # -------- modify time -------- #
        self.sakura_tears.modify_time(4, 1)
        # -------- other -------- #
        self.sakura_tears.a2(4)
        # ------------------------ end ------------------------ #
        with open(self.name, "wb") as output_file:
            self.sakura_tears.get_midi().writeFile(output_file)
        return self.name
