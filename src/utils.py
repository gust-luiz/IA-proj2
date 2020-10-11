from collections import OrderedDict

from skfuzzy import interp_membership

from consequents import disease


class Patient:
    name = ''
    name2 = ''
    age = 0


def inform_diagnosis(result):
    diagnosis = order_diagnosis(disease, result)

    print()
    print('Então, pelo o que me foi informado acredito que esteja com:', diagnosis[0][0])
    print()

    print('Diagnóstico completo:')
    for disease_name, percent in diagnosis:
        print(''.join([
            '\t', disease_name, ': ', str(percent), ' %'
        ]))


def order_diagnosis(disease, result):
    diagnosis = {}

    for name in list(disease.terms.keys()):
        diagnosis[name.capitalize()] = round(interp_membership(disease.universe, disease[name].mf, result) * 100, 2)

    diagnosis = OrderedDict(sorted(diagnosis.items(), key=lambda d: d[1], reverse=True))

    return list(diagnosis.items())


def wait_valid_answer(question, valid_answers=None, min_value=None, cast_to=None):
    options = '/'.join(valid_answers) if valid_answers else ''

    while True:
        print(question, options)
        resp = input()

        if cast_to:
            resp = cast_to(resp)

        if ((valid_answers and resp not in valid_answers) or
                (min_value and resp <= min_value)):
            print('Infelizmente nesta resposta não entendi o que escreveu...')
            continue

        return resp

def wait_any_key_press(msg=''):
    input(msg or 'Aperte ENTER para prosseguirmos...')
