from skfuzzy import control


def get_fiver_rules():
    from consequents import disease
    from antecedents import get_fiver_antecedents

    temperature, duration = get_fiver_antecedents()

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
    from consequents import disease
    from antecedents import get_melasma_antecedents

    when_happened, occurence = get_melasma_antecedents()

    return [
        control.Rule(
            when_happened['middle'] & occurence['uncommom'],
            disease['dengue']
        ),
        control.Rule(
            when_happened['beginning'] & occurence['for_sure'],
            disease['zika']
        ),
        control.Rule(
            when_happened['all'] & occurence['middle'],
            disease['chikungunya']
        )
    ]


all_rules = []
all_rules.extend(get_fiver_rules())
all_rules.extend(get_melasma_rules())
