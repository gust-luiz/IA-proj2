from skfuzzy import control

from consequents import disease


def get_fiver_rules():
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

all_rules = []
all_rules.extend(
    get_fiver_rules()
)
