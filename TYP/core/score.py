from datetime import datetime
from datetime import timedelta
from math import floor

class Score:
    def __init__(self):
        self.hour = timedelta(hours=1)
        self.half = timedelta(minutes=30)

        self.PRECISE_BONUS      =  2
        self.ALMOST_BONUS       =  1
        self.SLIGHT_PENALTY     = -2
        self.HEAVY_PENALTY      = -3
        self.RECURRING_PENALTY  = -1

        self.START  =  5
        self.MIN    =  0
        self.MAX    = 10

    def translate(self, treatment, taken):
        ntaken = []
        ntaken.append(treatment.created_at)
        ntaken = ntaken + [ t.taken_at for t in taken ]
        return self.derive_score(treatment.time_interval, ntaken)

    def derive_score(self, time_interval, taken):
        score = self.START

        # calculate the first entry and the difference between
        last = taken[0]
        taken.pop(0)
        diff = timedelta(hours = time_interval)
        
        # goes through all taken intervals recalculating score
        for t in taken:
            target = last + timedelta(hours=time_interval)
            score = score + self.interval_score(target, t)
            last = target
            
            # never let user go too far below minimum
            if (score < self.MIN):
                score = self.MIN
            if (score > self.MAX):
                score = self.MAX

        return score

    def interval_score(self, target, taken):
        diff = abs(target - taken)

        if (diff <= self.half):
            return self.PRECISE_BONUS
        elif (diff <= self.hour):
            return self.ALMOST_BONUS
        elif (diff <= 2 * self.hour):
            return self.SLIGHT_PENALTY
        else:
            return self.HEAVY_PENALTY + floor((diff - 2 * self.hour).total_seconds() / self.hour.total_seconds()) * self.RECURRING_PENALTY

