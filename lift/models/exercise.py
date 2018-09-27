from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date
from typing import List, Dict


class Scheme(ABC):

    @abstractmethod
    def get_id(self):
        pass


@dataclass
class WeightReps(Scheme):
    weight: float
    reps: int

    def get_id(self):
        return "weight_reps"


class WeightRepsStrategy(Scheme):


class Programmable(ABC):
    pass


@dataclass
class Exercise(Programmable):
    name: str
    scheme: Scheme


@dataclass
class ExerciseGroup(Programmable):
    name: str
    exercises: List[Exercise]


@dataclass
class Workout:
    programming: List[Programmable]


@dataclass
class Routine:
    routine: Dict[date, Workout]





