import skfuzzy as fuzzy
from numpy import arange
from skfuzzy import control


def get_fiver_antecedents():
    fever_temperature = control.Antecedent(arange(30, 41, .1), 'temperatura')
    fever_duration = control.Antecedent(arange(0, 7, 1), 'duração da febre')

    fever_temperature['normal'] = fuzzy.gaussmf(fever_temperature.universe, 30, 4)
    fever_temperature['feverish'] = fuzzy.gaussmf(fever_temperature.universe, 40, 3)

    fever_duration['short'] = fuzzy.trapmf(fever_duration.universe, [0, 0, 2, 3])
    fever_duration['medium'] = fuzzy.trapmf(fever_duration.universe, [1, 2, 3, 4])
    fever_duration['long'] = fuzzy.trapmf(fever_duration.universe, [3, 4, 7, 7])

    return fever_temperature, fever_duration


def get_melasma_antecedents():
    melasma_when = control.Antecedent(arange(0, 7, 1), 'melasma')
    melasma_occurence = control.Antecedent(arange(0, 10, 1), 'melasma_occurence')

    melasma_when['beginning'] = fuzzy.trapmf(melasma_when.universe, [0, 1, 2, 3])
    melasma_when['middle'] = fuzzy.trimf(melasma_when.universe, [3, 4, 5])
    melasma_when['all'] = fuzzy.trapmf(melasma_when.universe, [1, 2, 5, 7])

    melasma_occurence['uncommom'] = fuzzy.trapmf(melasma_occurence.universe, [2, 3, 5, 6])
    melasma_occurence['for_sure'] = fuzzy.trapmf(melasma_occurence.universe, [8, 9, 10, 10])
    melasma_occurence['middle'] = fuzzy.trimf(melasma_occurence.universe, [4, 5, 6])

    return melasma_when, melasma_occurence
