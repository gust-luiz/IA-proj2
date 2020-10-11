from numpy import arange
from skfuzzy import control
import skfuzzy as fuzzy

disease = control.Consequent(arange(0, 11, .1), 'diagnosis')

disease.automf(names=['unidentified', 'dengue', 'zika', 'chikungunya'])


def get_melasma_consequent():
    melasma = control.Consequent(arange(0, 11, .1), 'diagnosis')

    second_portion = fuzzy.gbellmf(melasma.universe, 1.2, 5, 3.75)
    third_portion = fuzzy.gbellmf(melasma.universe, 1.2, 5, 6.25)
    fourth_portion = fuzzy.gbellmf(melasma.universe, 1.2, 5, 8.75)

    melasma['unidentified'] = fuzzy.gbellmf(melasma.universe, 1.2, 5, 1.25)# .1
    melasma['dengue'] = fuzzy.sigmf(melasma.universe, 5, .34)
    melasma['dengue'] = [
        v * melasma['dengue'].mf[i]
        for i, v in enumerate(second_portion)
    ]  # approx. .3 to .5
    melasma['zika'] = fuzzy.sigmf(melasma.universe, -1.5, .34)
    melasma['zika'] = [
        v * melasma['zika'].mf[i]
        for i, v in enumerate(third_portion)
    ]  # approx. .9 to .1
    melasma['chikungunya'] = fuzzy.sigmf(melasma.universe, 0, 0)
    melasma['chikungunya'] = [
        v * melasma['chikungunya'].mf[i]
        for i, v in enumerate(fourth_portion)
    ] # .5

    melasma['unidentified'] = list(map(lambda x: min(1, x), (
        fuzzy.gbellmf(melasma.universe, 1.2, 5, 1.25)
        + second_portion
        + third_portion
        + fourth_portion
    )))
    melasma['unidentified'] = [
        max(0, v - melasma['dengue'].mf[i] - melasma['zika'].mf[i] - melasma['chikungunya'].mf[i])
        for i, v in enumerate(melasma['unidentified'].mf)
    ]

    return melasma


def get_muscle_pain_consequent():
    muscle_pain = control.Consequent(arange(0, 11, .1), 'diagnosis')

    muscle_pain['dengue'] = fuzzy.gaussmf(muscle_pain.universe, 10, 1.5)
    muscle_pain['zika'] = fuzzy.gaussmf(muscle_pain.universe, 5, 1.5)
    muscle_pain['chikungunya'] = fuzzy.gaussmf(muscle_pain.universe, 0, 1.5)

    return muscle_pain


def get_joint_pain_consequent():
    joint_pain = control.Consequent(arange(0, 11, .1), 'diagnosis')

    joint_pain['unidentified'] = (
        fuzzy.gaussmf(joint_pain.universe, 2.5, .75) +
        fuzzy.gaussmf(joint_pain.universe, 7.5, .75)
    )
    joint_pain['dengue'] = fuzzy.gaussmf(joint_pain.universe, 0, .75)
    joint_pain['zika'] = fuzzy.gaussmf(joint_pain.universe, 5, .75)
    joint_pain['chikungunya'] = fuzzy.gaussmf(joint_pain.universe, 10, .75)

    return joint_pain


def get_conjunctivitis_consequent():
    conjunctivitis = control.Consequent(arange(0, 11, .1), 'diagnosis')

    second_portion = fuzzy.gbellmf(conjunctivitis.universe, 1.2, 5, 3.75)
    third_portion = fuzzy.gbellmf(conjunctivitis.universe, 1.2, 5, 6.25)
    fourth_portion = fuzzy.gbellmf(conjunctivitis.universe, 1.2, 5, 8.75)

    conjunctivitis['dengue'] = fuzzy.sigmf(conjunctivitis.universe, 15.65, .2)
    conjunctivitis['dengue'] = [
        v * conjunctivitis['dengue'].mf[i]
        for i, v in enumerate(second_portion)
    ]  # rare
    conjunctivitis['zika'] = fuzzy.sigmf(conjunctivitis.universe, -1.5, .34)
    conjunctivitis['zika'] = [
        v * conjunctivitis['zika'].mf[i]
        for i, v in enumerate(third_portion)
    ]  # approx. .5 to .9
    conjunctivitis['chikungunya'] = fuzzy.sigmf(conjunctivitis.universe, 0, 0)
    conjunctivitis['chikungunya'] = [
        v * conjunctivitis['chikungunya'].mf[i]
        for i, v in enumerate(fourth_portion)
    ] # .3

    conjunctivitis['unidentified'] = list(map(lambda x: min(1, x), (
        fuzzy.gbellmf(conjunctivitis.universe, 1.2, 5, 1.25)
        + second_portion
        + third_portion
        + fourth_portion
    )))
    conjunctivitis['unidentified'] = [
        max(0, v - conjunctivitis['dengue'].mf[i] - conjunctivitis['zika'].mf[i] - conjunctivitis['chikungunya'].mf[i])
        for i, v in enumerate(conjunctivitis['unidentified'].mf)
    ]

    return conjunctivitis


def get_headache_consequent():
    headache = control.Consequent(arange(0, 11, .1), 'diagnosis')

    headache['dengue'] = fuzzy.gaussmf(headache.universe, 10, 1.5)
    headache['zika'] = fuzzy.gaussmf(headache.universe, 5, 1.5)
    headache['chikungunya'] = fuzzy.gaussmf(headache.universe, 5, 1.5)

    return headache


def get_itch_consequent():
    itch = control.Consequent(arange(0, 11, .1), 'diagnosis')

    itch['dengue'] = fuzzy.gaussmf(itch.universe, 0, 1.5)
    itch['zika'] = fuzzy.gaussmf(itch.universe, 10, 2.5)
    itch['chikungunya'] = fuzzy.gaussmf(itch.universe, 0, 1.5)

    return itch


def get_ganglionic_hypertrophy_consequent():
    ganglionic_hypertrophy = control.Consequent(arange(0, 11, .1), 'diagnosis')

    ganglionic_hypertrophy['dengue'] = fuzzy.gaussmf(ganglionic_hypertrophy.universe, 0, 1.5)
    ganglionic_hypertrophy['zika'] = fuzzy.gaussmf(ganglionic_hypertrophy.universe, 10, 1.5)
    ganglionic_hypertrophy['chikungunya'] = fuzzy.gaussmf(ganglionic_hypertrophy.universe, 5, 1.5)

    return ganglionic_hypertrophy


def get_hemorrhagic_dyscrasia_consequent():
    hemorrhagic_dyscrasia = control.Consequent(arange(0, 11, .1), 'diagnosis')

    hemorrhagic_dyscrasia['dengue'] = fuzzy.sigmf(hemorrhagic_dyscrasia.universe, 3.5, .5)
    hemorrhagic_dyscrasia['zika'] = fuzzy.gaussmf(hemorrhagic_dyscrasia.universe, 0, .5)
    hemorrhagic_dyscrasia['chikungunya'] = fuzzy.gaussmf(hemorrhagic_dyscrasia.universe, 2, 1.5)

    return hemorrhagic_dyscrasia

    
def get_neurological_damage_consequent():
    neurological_damage = control.Consequent(arange(0, 11, .1), 'diagnosis')

    second_portion = fuzzy.gbellmf(neurological_damage.universe, 1.2, 5, 3.75)
    third_portion = fuzzy.gbellmf(neurological_damage.universe, 1.2, 5, 6.25)
    fourth_portion = fuzzy.gbellmf(neurological_damage.universe, 1.2, 5, 8.75)

    neurological_damage['dengue'] = fuzzy.sigmf(neurological_damage.universe, 15.65, .2)
    neurological_damage['dengue'] = [
        v * neurological_damage['dengue'].mf[i]
        for i, v in enumerate(second_portion)
    ]  # rare
    neurological_damage['zika'] = fuzzy.sigmf(neurological_damage.universe, 0, 0)
    neurological_damage['zika'] = [
        v * neurological_damage['zika'].mf[i]
        for i, v in enumerate(third_portion)
    ]  # rare, but more often than in the others
    neurological_damage['chikungunya'] = fuzzy.sigmf(neurological_damage.universe, 15.65, .2)
    neurological_damage['chikungunya'] = [
        v * neurological_damage['chikungunya'].mf[i]
        for i, v in enumerate(fourth_portion)
    ] # rare, but often in newborn

    neurological_damage['unidentified'] = list(map(lambda x: min(1, x), (
        fuzzy.gbellmf(neurological_damage.universe, 1.2, 5, 1.25)
        + second_portion
        + third_portion
        + fourth_portion
    )))
    neurological_damage['unidentified'] = [
        max(0, v - neurological_damage['dengue'].mf[i] - neurological_damage['zika'].mf[i] - neurological_damage['chikungunya'].mf[i])
        for i, v in enumerate(neurological_damage['unidentified'].mf)
    ]

    return neurological_damage
