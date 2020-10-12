from numpy import arange
from skfuzzy import control
import skfuzzy as fuzzy


COMMON_CONSEQUENT_NAME = 'diagnosis'
COMMON_RANGE = arange(0, 11, .1)
FIRST_INTERVAL = fuzzy.gbellmf(COMMON_RANGE, .9, 5, 1.25)
SECOND_INTERVAL = fuzzy.gbellmf(COMMON_RANGE, .9, 5, 3.75)
THIRD_INTERVAL = fuzzy.gbellmf(COMMON_RANGE, .9, 5, 6.25)
FOURTH_INTERVAL = fuzzy.gbellmf(COMMON_RANGE, .9, 5, 8.75)


def get_fever_consequent():
    fever = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    fever['unidentified'] = FIRST_INTERVAL
    fever['dengue'] = SECOND_INTERVAL
    fever['zika'] = THIRD_INTERVAL
    fever['chikungunya'] = FOURTH_INTERVAL

    return fever


def get_melasma_consequent():
    melasma = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    melasma['dengue'] = fuzzy.sigmf(melasma.universe, 5, .34)
    melasma['dengue'] = [
        v * melasma['dengue'].mf[i]
        for i, v in enumerate(SECOND_INTERVAL)
    ]  # approx. .3 to .5

    melasma['zika'] = fuzzy.sigmf(melasma.universe, -1.5, .34)
    melasma['zika'] = [
        v * melasma['zika'].mf[i]
        for i, v in enumerate(THIRD_INTERVAL)
    ]  # approx. .9 to .1

    melasma['chikungunya'] = fuzzy.sigmf(melasma.universe, 0, 0)
    melasma['chikungunya'] = [
        v * melasma['chikungunya'].mf[i]
        for i, v in enumerate(FOURTH_INTERVAL)
    ] # .5

    melasma['unidentified'] = list(map(lambda x: min(1, x), (
        FIRST_INTERVAL + SECOND_INTERVAL + THIRD_INTERVAL + FOURTH_INTERVAL
    )))
    melasma['unidentified'] = [
        max(0, v - melasma['dengue'].mf[i] - melasma['zika'].mf[i] - melasma['chikungunya'].mf[i])
        for i, v in enumerate(melasma['unidentified'].mf)
    ]

    return melasma


def get_muscle_pain_consequent():
    muscle_pain = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    muscle_pain['unidentified'] = FIRST_INTERVAL
    muscle_pain['dengue'] = SECOND_INTERVAL
    muscle_pain['zika'] = THIRD_INTERVAL
    muscle_pain['chikungunya'] = FOURTH_INTERVAL

    return muscle_pain


def get_joint_pain_consequent():
    joint_pain = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    joint_pain['unidentified'] = FIRST_INTERVAL
    joint_pain['dengue'] = SECOND_INTERVAL
    joint_pain['zika'] = THIRD_INTERVAL
    joint_pain['chikungunya'] = FOURTH_INTERVAL

    return joint_pain


def get_conjunctivitis_consequent():
    conjunctivitis = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    conjunctivitis['dengue'] = fuzzy.sigmf(conjunctivitis.universe, 15.65, .2)
    conjunctivitis['dengue'] = [
        v * conjunctivitis['dengue'].mf[i]
        for i, v in enumerate(SECOND_INTERVAL)
    ]  # rare
    conjunctivitis['zika'] = fuzzy.sigmf(conjunctivitis.universe, -1.5, .34)
    conjunctivitis['zika'] = [
        v * conjunctivitis['zika'].mf[i]
        for i, v in enumerate(THIRD_INTERVAL)
    ]  # approx. .5 to .9
    conjunctivitis['chikungunya'] = fuzzy.sigmf(conjunctivitis.universe, 0, 0)
    conjunctivitis['chikungunya'] = [
        v * conjunctivitis['chikungunya'].mf[i]
        for i, v in enumerate(FOURTH_INTERVAL)
    ] # .3

    conjunctivitis['unidentified'] = list(map(lambda x: min(1, x), (
        FIRST_INTERVAL + SECOND_INTERVAL + THIRD_INTERVAL + FOURTH_INTERVAL
    )))
    conjunctivitis['unidentified'] = [
        max(0, v - conjunctivitis['dengue'].mf[i] - conjunctivitis['zika'].mf[i] - conjunctivitis['chikungunya'].mf[i])
        for i, v in enumerate(conjunctivitis['unidentified'].mf)
    ]

    return conjunctivitis


def get_headache_consequent():
    headache = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    headache['unidentified'] = FIRST_INTERVAL
    headache['dengue'] = SECOND_INTERVAL
    headache['zika'] = THIRD_INTERVAL
    headache['chikungunya'] = FOURTH_INTERVAL

    return headache


def get_itch_consequent():
    itch = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    itch['unidentified'] = FIRST_INTERVAL
    itch['dengue'] = SECOND_INTERVAL
    itch['zika'] = THIRD_INTERVAL
    itch['chikungunya'] = FOURTH_INTERVAL

    return itch


def get_ganglionic_hypertrophy_consequent():
    ganglionic_hypertrophy = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    ganglionic_hypertrophy['unidentified'] = FIRST_INTERVAL
    ganglionic_hypertrophy['dengue'] = SECOND_INTERVAL
    ganglionic_hypertrophy['zika'] = THIRD_INTERVAL
    ganglionic_hypertrophy['chikungunya'] = FOURTH_INTERVAL

    return ganglionic_hypertrophy


def get_hemorrhagic_dyscrasia_consequent():
    hemorrhagic_dyscrasia = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    hemorrhagic_dyscrasia['unidentified'] = FIRST_INTERVAL
    hemorrhagic_dyscrasia['dengue'] = SECOND_INTERVAL
    hemorrhagic_dyscrasia['zika'] = THIRD_INTERVAL
    hemorrhagic_dyscrasia['chikungunya'] = FOURTH_INTERVAL

    return hemorrhagic_dyscrasia


def get_neurological_damage_consequent():
    neurological_damage = control.Consequent(COMMON_RANGE, COMMON_CONSEQUENT_NAME)

    neurological_damage['dengue'] = fuzzy.sigmf(neurological_damage.universe, 15.65, .2)
    neurological_damage['dengue'] = [
        v * neurological_damage['dengue'].mf[i]
        for i, v in enumerate(SECOND_INTERVAL)
    ]  # rare
    neurological_damage['zika'] = fuzzy.sigmf(neurological_damage.universe, 0, 0)
    neurological_damage['zika'] = [
        v * neurological_damage['zika'].mf[i]
        for i, v in enumerate(THIRD_INTERVAL)
    ]  # rare, but more often than in the others
    neurological_damage['chikungunya'] = fuzzy.sigmf(neurological_damage.universe, 15.65, .2)
    neurological_damage['chikungunya'] = [
        v * neurological_damage['chikungunya'].mf[i]
        for i, v in enumerate(FOURTH_INTERVAL)
    ] # rare, but often in newborn

    neurological_damage['unidentified'] = list(map(lambda x: min(1, x), (
        FIRST_INTERVAL + SECOND_INTERVAL + THIRD_INTERVAL + FOURTH_INTERVAL
    )))
    neurological_damage['unidentified'] = [
        max(0, v - neurological_damage['dengue'].mf[i] - neurological_damage['zika'].mf[i] - neurological_damage['chikungunya'].mf[i])
        for i, v in enumerate(neurological_damage['unidentified'].mf)
    ]

    return neurological_damage
