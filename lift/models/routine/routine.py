from datetime import date
from typing import Dict


class Workout:
    pass


class Routine:
    routine: Dict[date, Workout] = {}



    def add_workout(self, day, workout):
        self.routine[day] = workout

