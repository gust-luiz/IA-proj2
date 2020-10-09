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
