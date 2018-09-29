from abc import ABC

from typing import Dict, List
from datetime import date


class Set(ABC):
    pass


class PercentSet(Set):
    reps: int
    multiplier: float


class ExerciseTemplate:
    name: str
    id: int

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'[{self.id} | {self.name}]'


class Exercise:
    exercise_template: ExerciseTemplate
    sets: List[Set]

    def __init__(self, exercise_template=None, sets=None):
        self.exercise_template = exercise_template
        self.sets = sets

    def __str__(self):
        return f'{self.exercise_template} | {str(self.sets)}'


class Workout:
    exercises: List[Exercise]

    def add_exercise(self, exercise):
        self.exercises.append(exercise)


class Routine:
    maxes: Dict[int, float]
    workouts: Dict[date, Workout]

    def add_workout(self, date, workout):
        self.workouts[date] = workout
