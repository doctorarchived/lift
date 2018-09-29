from abc import ABC, abstractmethod
from datetime import date, datetime
from typing import Dict, List


class MaxContext(ABC):

    @abstractmethod
    def get_maxes(self):
        pass


class ExerciseTemplate:
    name: str
    id: int

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'[{self.id} | {self.name}]'


class Set:
    percent: float
    weight: float
    reps: int

    def __init__(self, percent, reps):
        self.percent = percent
        self.reps = reps

    def __repr__(self):
        return f'{self.weight} x {self.reps}'


class PercentBasedSet:
    percent: float
    reps: int

    context: MaxContext

    def __init__(self, context, percent, reps):
        self.context = context
        self.percent, self.reps = percent, reps

    def get_weight(self):
        pass


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

    def __init__(self, exercises):
        self.exercises = exercises

    def show_me(self):
        for exercise in self.exercises:
            print(exercise)


class Routine(MaxContext):
    routine: Dict[date, Workout] = {}
    exercise_bases: Dict[int, float] = {}

    def add_workout(self, day, workout):
        for exercise in workout.exercises:
            id = exercise.exercise_template.id
            base = self.exercise_bases[id]
            for s in exercise.sets:
                s.weight = base * s.percent

        self.routine[day] = workout
        workout.show_me()

    def get_maxes(self):
        return self.exercise_bases


if __name__ == '__main__':
    template = ExerciseTemplate(1, 'Squat')

    squat = Exercise(template, [Set(0.5, 10), Set(0.6, 8), Set(0.7, 6)])

    workout = Workout([squat, ])

    routine = Routine()
    routine.exercise_bases = {1: 315}
    routine.add_workout(datetime.today(), workout)
