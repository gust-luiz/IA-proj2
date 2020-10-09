from skfuzzy import interp_membership

from consequents import disease


def inform_diagnosis(result):
    disease_names = list(disease.terms.keys())

    print()
    print('Então, pelo o que me foi informado acredito que esteja com:', disease_names[0].capitalize())
    print()

    print('Diagnóstico completo:')
    for name in disease_names:
        print(''.join([
            '\t', name, ': ',
            str(round(interp_membership(disease.universe, disease[name].mf, result) * 100, 2)),
            ' %'
        ]))
