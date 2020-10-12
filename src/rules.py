from skfuzzy import control


def get_fever_rules():
    from consequents import get_fever_consequent
    from antecedents import get_fever_antecedents

    aedes_aegypti_disease = get_fever_consequent()
    temperature, duration = get_fever_antecedents()

    return [
        control.Rule(
            temperature['feverish'] & duration['long'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            temperature['normal'] & duration['short'],
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            temperature['feverish'] & duration['medium'],
            aedes_aegypti_disease['chikungunya']
        )
    ]


def get_melasma_rules():
    from consequents import get_melasma_consequent
    from antecedents import get_melasma_antecedents

    aedes_aegypti_disease = get_melasma_consequent()
    when_happened = get_melasma_antecedents()

    return [
        control.Rule(
            when_happened['middle'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            when_happened['beginning'],
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            when_happened['beginning'] |
            when_happened['middle'] |
            when_happened['ending'],
            aedes_aegypti_disease['chikungunya']
        ),
    ]


def get_muscle_pain_rules():
    from consequents import get_muscle_pain_consequent
    from antecedents import get_muscle_pain_antecedents

    aedes_aegypti_disease = get_muscle_pain_consequent()
    frequency = get_muscle_pain_antecedents()

    return [
        control.Rule(
            frequency['high'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            frequency['medium'],
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            frequency['low'],
            aedes_aegypti_disease['chikungunya']
        )
    ]


def get_joint_pain_rules():
    from antecedents import get_joint_pain_antecedents
    from consequents import get_joint_pain_consequent

    aedes_aegypti_disease = get_joint_pain_consequent()
    frequency, intensity, edema, edema_intensity = get_joint_pain_antecedents()

    return [
        control.Rule(
            frequency['rare'] &
            intensity['mild'] &
            edema['rare'] &
            edema_intensity['mild'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            frequency['common'] &
            (intensity['mild'] | intensity['moderate']) &
            edema['frequent'] &
            edema_intensity['mild'],
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            frequency['frequent'] &
            (intensity['moderate'] | intensity['intense']) &
            edema['frequent'] &
            (edema_intensity['moderate'] | intensity['intense']),
            aedes_aegypti_disease['chikungunya']
        )
    ]


def get_conjunctivitis_rules():
    from consequents import get_conjunctivitis_consequent
    from antecedents import get_conjunctivitis_antecedents

    aedes_aegypti_disease = get_conjunctivitis_consequent()
    occurence = get_conjunctivitis_antecedents()

    return [
        control.Rule(
            occurence['no'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            occurence['yes'],
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            occurence['yes'],
            aedes_aegypti_disease['chikungunya']
        ),
    ]


def get_headache_rules():
    from consequents import get_headache_consequent
    from antecedents import get_headache_antecedents

    aedes_aegypti_disease = get_headache_consequent()
    frequency, intensity = get_headache_antecedents()

    return [
        control.Rule(
            frequency['high'] &
            intensity['high'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            frequency['medium'] &
            intensity['medium'],
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            frequency['medium'] &
            intensity['medium'],
            aedes_aegypti_disease['chikungunya']
        )
    ]


def get_itch_rules():
    from consequents import get_itch_consequent
    from antecedents import get_itch_antecedents

    aedes_aegypti_disease = get_itch_consequent()
    intensity = get_itch_antecedents()

    return [
        control.Rule(
            intensity['mild'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            (intensity['moderate'] | intensity['intense']),
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            intensity['mild'],
            aedes_aegypti_disease['chikungunya']
        )
    ]


def get_ganglionic_hypertrophy_rules():
    from consequents import get_ganglionic_hypertrophy_consequent
    from antecedents import get_ganglionic_hypertrophy_antecedents

    aedes_aegypti_disease = get_ganglionic_hypertrophy_consequent()
    frequency = get_ganglionic_hypertrophy_antecedents()

    return [
        control.Rule(
            frequency['mild'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            frequency['intense'],
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            frequency['moderate'],
            aedes_aegypti_disease['chikungunya']
        )
    ]


def get_hemorrhagic_dyscrasia_rules():
    from consequents import get_hemorrhagic_dyscrasia_consequent
    from antecedents import get_hemorrhagic_dyscrasia_antecedents

    aedes_aegypti_disease = get_hemorrhagic_dyscrasia_consequent()
    frequency = get_hemorrhagic_dyscrasia_antecedents()

    return [
        control.Rule(
            frequency['moderate'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            frequency['none'],
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            frequency['mild'],
            aedes_aegypti_disease['chikungunya']
        )
    ]


def get_neurological_damage_rules():
    from consequents import get_neurological_damage_consequent
    from antecedents import get_neurological_damage_antecedents

    aedes_aegypti_disease = get_neurological_damage_consequent()
    occurence, newborn = get_neurological_damage_antecedents()

    return [
        control.Rule(
            occurence['yes'],
            aedes_aegypti_disease['dengue']
        ),
        control.Rule(
            occurence['yes'],
            aedes_aegypti_disease['zika']
        ),
        control.Rule(
            occurence['yes'] & newborn['yes'],
            aedes_aegypti_disease['chikungunya']
        )
    ]


all_rules = []
all_rules.extend(get_fever_rules())
all_rules.extend(get_melasma_rules())
all_rules.extend(get_muscle_pain_rules())
all_rules.extend(get_joint_pain_rules())
all_rules.extend(get_conjunctivitis_rules())
all_rules.extend(get_headache_rules())
all_rules.extend(get_itch_rules())
all_rules.extend(get_ganglionic_hypertrophy_rules())
all_rules.extend(get_hemorrhagic_dyscrasia_rules())
all_rules.extend(get_neurological_damage_rules())
