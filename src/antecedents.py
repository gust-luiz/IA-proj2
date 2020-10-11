import skfuzzy as fuzzy
from numpy import arange
from skfuzzy import control


def get_fever_antecedents():
    temperature = control.Antecedent(arange(30, 41, .1), 'body_temperature')
    duration = control.Antecedent(arange(0, 7, 1), 'fever_duration')

    temperature['normal'] = fuzzy.gaussmf(temperature.universe, 30, 4)
    temperature['feverish'] = fuzzy.gaussmf(temperature.universe, 40, 3)

    duration['short'] = fuzzy.trapmf(duration.universe, [0, 0, 2, 3])
    duration['medium'] = fuzzy.trapmf(duration.universe, [1, 2, 3, 4])
    duration['long'] = fuzzy.trapmf(duration.universe, [3, 4, 7, 7])

    return temperature, duration


def get_melasma_antecedents():
    when = control.Antecedent(arange(0, 7, .1), 'melasma')

    when['beginning'] = fuzzy.gbellmf(when.universe, 2, 5, 0)
    when['middle'] = fuzzy.gbellmf(when.universe, 1.2, 5, 3.5)
    when['ending'] = fuzzy.gbellmf(when.universe, 2, 5, 7)

    return when


def get_muscle_pain_antecedents():
    frequency = control.Antecedent(arange(0, 10, .1), 'muscle_pain_frequency')

    frequency['low'] = fuzzy.gaussmf(frequency.universe, 0, 1.5)
    frequency['medium'] = fuzzy.gaussmf(frequency.universe, 5, .75)
    frequency['high'] = fuzzy.gaussmf(frequency.universe, 10, 1.5)

    return frequency


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


def get_conjunctivitis_antecedents():
    occurence = control.Antecedent(arange(0, 1, 1), 'conjunctivitis')

    occurence['no'] = fuzzy.gaussmf(occurence.universe, 0, .25)
    occurence['yes'] = fuzzy.gaussmf(occurence.universe, 1, .25)

    return occurence


def get_headache_antecedents():
    frequency = control.Antecedent(arange(0, 10, .1), 'headache_frequency')
    intensity = control.Antecedent(arange(0, 10, .1), 'headache_intensity')

    frequency['low'] = fuzzy.gaussmf(frequency.universe, 0, 1.5)
    frequency['medium'] = fuzzy.gaussmf(frequency.universe, 5, .75)
    frequency['high'] = fuzzy.gaussmf(frequency.universe, 10, 1.5)

    intensity['low'] = fuzzy.gaussmf(intensity.universe, 0, 1.5)
    intensity['medium'] = fuzzy.gaussmf(intensity.universe, 5, .75)
    intensity['high'] = fuzzy.gaussmf(intensity.universe, 10, 1.5)

    return frequency, intensity


def get_itch_antecedents():
    intensity = control.Antecedent(arange(0, 10, .1), 'itch_intensity')

    intensity['mild'] = fuzzy.gaussmf(intensity.universe, 0, 1.5)
    intensity['moderate'] = fuzzy.gaussmf(intensity.universe, 5, .75)
    intensity['intense'] = fuzzy.gaussmf(intensity.universe, 10, 1.5)

    return intensity


def get_ganglionic_hypertrophy_antecedents():
    frequency = control.Antecedent(arange(0, 10, .1), 'ganglionic_hypertrophy_frequency')

    frequency['mild'] = fuzzy.gaussmf(frequency.universe, 0, 1.5)
    frequency['moderate'] = fuzzy.gaussmf(frequency.universe, 5, .75)
    frequency['intense'] = fuzzy.gaussmf(frequency.universe, 10, 1.5)

    return frequency


def get_hemorrhagic_dyscrasia():
    frequency = control.Antecedent(arange(0, 10, .1), 'hemorrhagic_dyscrasia_frequency')

    frequency['none'] = fuzzy.trimf(frequency.universe, [0, 0, 1])
    frequency['mild'] = fuzzy.gaussmf(frequency.universe, 2.5, 1.5)
    frequency['moderate'] = fuzzy.sigmf(frequency.universe, 3.5, .5)

    return frequency

    
def get_neurological_damage_antecedents():
    occurence = control.Antecedent(arange(0, 1, 1), 'neurological_damage')
    newborn = control.Antecedent(arange(0, 1, .1), 'neurological_damage_newborn')

    occurence['no'] = fuzzy.gaussmf(occurence.universe, 0, .25)
    occurence['yes'] = fuzzy.gaussmf(occurence.universe, 1, .25)

    newborn['no'] = fuzzy.gaussmf(newborn.universe, 0, .25)
    newborn['yes'] = fuzzy.gaussmf(newborn.universe, 1, .25)

    return occurence, newborn
