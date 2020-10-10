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


def get_muscle_pain_antecedents():
    muscle_pain_frequency = control.Antecedent(arange(0, 10, .1), 'muscle_pain_frequency')

    muscle_pain_frequency['low'] = fuzzy.gaussmf(muscle_pain_frequency.universe, 0, 1.5)
    muscle_pain_frequency['medium'] = fuzzy.gaussmf(muscle_pain_frequency.universe, 5, .75)
    muscle_pain_frequency['high'] = fuzzy.gaussmf(muscle_pain_frequency.universe, 10, 1.5)

    return muscle_pain_frequency


def get_joint_pain_antecedents():
    frequency = control.Antecedent(arange(0, 10, .1), 'joint_pain_freq')
    intensity = control.Antecedent(arange(0, 10, .1), 'joint_pain_intensity')
    edema = control.Antecedent(arange(0, 10, .1), 'joint_edema')
    edema_intensity = control.Antecedent(arange(0, 10, .1), 'joint_edema_intensity')

    frequency['rare'] = fuzzy.gaussmf(frequency.universe, 0, 1.5)
    frequency['common'] = fuzzy.gaussmf(frequency.universe, 5, .75)
    frequency['frequent'] = fuzzy.gaussmf(frequency.universe, 10, 1.5)

    intensity['mild'] = fuzzy.gaussmf(intensity.universe, 0, 1.5)
    intensity['moderate'] = fuzzy.gaussmf(intensity.universe, 5, .75)
    intensity['intense'] = fuzzy.gaussmf(intensity.universe, 10, 1.5)

    edema['rare'] = fuzzy.gaussmf(edema.universe, 0, 1.5)
    edema['common'] = fuzzy.gaussmf(edema.universe, 5, .75)
    edema['frequent'] = fuzzy.gaussmf(edema.universe, 10, 1.5)

    edema_intensity['mild'] = fuzzy.gaussmf(edema_intensity.universe, 0, 1.5)
    edema_intensity['moderate'] = fuzzy.gaussmf(edema_intensity.universe, 5, .75)
    edema_intensity['intense'] = fuzzy.gaussmf(edema_intensity.universe, 10, 1.5)

    return [frequency, intensity, edema, edema_intensity]


def get_headache_antecedents():
    headache_frequency = control.Antecedent(arange(0, 10, .1), 'headache_frequency')
    headache_intensity = control.Antecedent(arange(0, 10, .1), 'headache_intensity')

    headache_frequency['low'] = fuzzy.gaussmf(headache_frequency.universe, 0, 1.5)
    headache_frequency['medium'] = fuzzy.gaussmf(headache_frequency.universe, 5, .75)
    headache_frequency['high'] = fuzzy.gaussmf(headache_frequency.universe, 10, 1.5)

    headache_intensity['low'] = fuzzy.gaussmf(headache_intensity.universe, 0, 1.5)
    headache_intensity['medium'] = fuzzy.gaussmf(headache_intensity.universe, 5, .75)
    headache_intensity['high'] = fuzzy.gaussmf(headache_intensity.universe, 10, 1.5)

    return headache_frequency, headache_intensity