from numpy import arange
from skfuzzy import control
import skfuzzy as fuzzy

disease = control.Consequent(arange(0, 11, .1), 'doenças')

disease.automf(names=['dengue', 'zika', 'chikungunya'])


def get_melasma_consequent():
    melasma = control.Consequent(arange(0, 11, .1), 'from melasma')

    melasma['dengue'] = fuzzy.trapmf(melasma.universe, [2, 3, 5, 6])
    melasma['zika'] = fuzzy.trapmf(melasma.universe, [8, 9, 10, 10])
    melasma['chikungunya'] = fuzzy.trimf(melasma.universe, [4, 5, 6])

    return melasma


def get_muscle_pain_consequent():
    muscle_pain = control.Consequent(arange(0, 11, .1), 'from muscle_pain')

    muscle_pain['dengue'] = fuzzy.gaussmf(muscle_pain.universe, 0, 1.5)
    muscle_pain['zika'] = fuzzy.gaussmf(muscle_pain.universe, 5, 1.5)
    muscle_pain['chikungunya'] = fuzzy.gaussmf(muscle_pain.universe, 10, 1.5)

    return muscle_pain


def get_joint_pain_consequent():
    joint_pain = control.Consequent(arange(0, 11, .1), 'joint_pain')

    joint_pain['dengue'] = fuzzy.gaussmf(joint_pain.universe, 0, 2.5)
    joint_pain['zika'] = fuzzy.gaussmf(joint_pain.universe, 5, 1.5)
    joint_pain['chikungunya'] = fuzzy.gaussmf(joint_pain.universe, 10, 2.5)

    return joint_pain


def get_headache_consequent():
    headache = control.Consequent(arange(0, 11, .1), 'from headache')

    headache['dengue'] = fuzzy.gaussmf(headache.universe, 0, 1.5)
    headache['zika'] = fuzzy.gaussmf(headache.universe, 5, 1.5)
    headache['chikungunya'] = fuzzy.gaussmf(headache.universe, 10, 1.5)

    return headache
