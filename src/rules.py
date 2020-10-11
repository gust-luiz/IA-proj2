from skfuzzy import control


def get_fever_rules():
    from consequents import disease
    from antecedents import get_fever_antecedents

    temperature, duration = get_fever_antecedents()

    return [
        control.Rule(
            temperature['feverish'] & duration['long'],
            disease['dengue']
        ),
        control.Rule(
            temperature['normal'] & duration['short'],
            disease['zika']
        ),
        control.Rule(
            temperature['feverish'] & duration['medium'],
            disease['chikungunya']
        )
    ]


def get_melasma_rules():
    from consequents import get_melasma_consequent
    from antecedents import get_melasma_antecedents

    from_melasma = get_melasma_consequent()
    when_happened = get_melasma_antecedents()

    return [
        control.Rule(
            when_happened['middle'],
            from_melasma['dengue']
        ),
        control.Rule(
            when_happened['beginning'],
            from_melasma['zika']
        ),
        control.Rule(
            (when_happened['beginning'] &
            when_happened['middle']) |
            when_happened['ending'],
            from_melasma['chikungunya']
        ),
    ]


def get_muscle_pain_rules():
    from consequents import disease
    from antecedents import get_muscle_pain_antecedents

    frequency = get_muscle_pain_antecedents()

    return [
        control.Rule(
            frequency['high'],
            disease['dengue']
        ),
        control.Rule(
            frequency['medium'],
            disease['zika']
        ),
        control.Rule(
            frequency['low'],
            disease['chikungunya']
        )
    ]


def get_joint_pain_rules():
    from antecedents import get_joint_pain_antecedents
    from consequents import get_joint_pain_consequent

    joint_pain = get_joint_pain_consequent()
    frequency, intensity, edema, edema_intensity = get_joint_pain_antecedents()

    return [
        control.Rule(
            frequency['rare'] &
            intensity['mild'] &
            edema['rare'] &
            edema_intensity['mild'],
            joint_pain['dengue']
        ),
        control.Rule(
            frequency['common'] &
            (intensity['mild'] | intensity['moderate']) &
            edema['frequent'] &
            edema_intensity['mild'],
            joint_pain['zika']
        ),
        control.Rule(
            frequency['frequent'] &
            (intensity['moderate'] | intensity['intense']) &
            edema['frequent'] &
            (edema_intensity['moderate'] | intensity['intense']),
            joint_pain['chikungunya']
        )
    ]


def get_conjunctivitis_rules():
    from consequents import get_conjunctivitis_consequent
    from antecedents import get_conjunctivitis_antecedents

    from_conjunctivitis = get_conjunctivitis_consequent()
    occurence = get_conjunctivitis_antecedents()

    return [
        control.Rule(
            occurence['no'],
            from_conjunctivitis['dengue']
        ),
        control.Rule(
            occurence['yes'],
            from_conjunctivitis['zika']
        ),
        control.Rule(
            occurence['yes'],
            from_conjunctivitis['chikungunya']
        ),
    ]


def get_headache_rules():
    from consequents import disease
    from antecedents import get_headache_antecedents

    frequency, intensity = get_headache_antecedents()

    return [
        control.Rule(
            frequency['high'] &
            intensity['high'],
            disease['dengue']
        ),
        control.Rule(
            frequency['medium'] &
            intensity['medium'],
            disease['zika']
        ),
        control.Rule(
            frequency['medium'] &
            intensity['medium'],
            disease['chikungunya']
        )
    ]


def get_itch_rules():
    from consequents import disease
    from antecedents import get_itch_antecedents

    intensity = get_itch_antecedents()

    return [
        control.Rule(
            intensity['mild'],
            disease['dengue']
        ),
        control.Rule(
            (intensity['moderate'] | intensity['intense']),
            disease['zika']
        ),
        control.Rule(
            intensity['mild'],
            disease['chikungunya']
        )
    ]


def get_ganglionic_hypertrophy_rules():
    from consequents import disease
    from antecedents import get_ganglionic_hypertrophy_antecedents

    frequency = get_ganglionic_hypertrophy_antecedents()

    return [
        control.Rule(
            frequency['mild'],
            disease['dengue']
        ),
        control.Rule(
            frequency['intense'],
            disease['zika']
        ),
        control.Rule(
            frequency['moderate'],
            disease['chikungunya']
        )
    ]


def get_hemorrhagic_dyscrasia_rules():
    from consequents import disease
    from antecedents import get_hemorrhagic_dyscrasia_antecedents

    frequency = get_hemorrhagic_dyscrasia_antecedents()

    return [
        control.Rule(
            frequency['moderate'],
            disease['dengue']
        ),
        control.Rule(
            frequency['none'],
            disease['zika']
        ),
        control.Rule(
            frequency['mild'],
            disease['chikungunya']
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
