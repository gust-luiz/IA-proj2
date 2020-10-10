from numpy import arange
from skfuzzy import control
import skfuzzy as fuzzy

disease = control.Consequent(arange(0, 10, 1), 'doenças')

disease.automf(names=['dengue', 'zika', 'chikungunya'])


def get_melasma_consequent():
    disease = control.Consequent(arange(0, 10, .1), 'from melasma')

    disease['dengue'] = fuzzy.trapmf(disease.universe, [2, 3, 5, 6])
    disease['zika'] = fuzzy.trapmf(disease.universe, [8, 9, 10, 10])
    disease['chikungunya'] = fuzzy.trimf(disease.universe, [4, 5, 6])

    return disease
