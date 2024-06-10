# Enum for scheduling switch
from enum import Enum


class Switch(Enum):
    PREEMPTIVE = "preemptive_scheduling"
    NON_PREEMPTIVE = "non_preemptive_scheduling"