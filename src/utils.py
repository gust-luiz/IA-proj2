from collections import OrderedDict

from skfuzzy import interp_membership

from consequents import disease


def inform_diagnosis(result):
    diagnosis = order_diagnosis(result)

    print()
    print('Então, pelo o que me foi informado acredito que esteja com:', diagnosis[0][0])
    print()

    print('Diagnóstico completo:')
    for disease, percent in diagnosis:
        print(''.join([
            '\t', disease, ': ', str(percent), ' %'
        ]))

def order_diagnosis(result):
    diagnosis = {}

    for name in list(disease.terms.keys()):
        diagnosis[name.capitalize()] = round(interp_membership(disease.universe, disease[name].mf, result) * 100, 2)

    diagnosis = OrderedDict(sorted(diagnosis.items(), key=lambda d: d[1], reverse=True))

    return list(diagnosis.items())
