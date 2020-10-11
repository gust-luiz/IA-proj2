from collections import OrderedDict
from os import system

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


def wait_valid_answer(question, valid_answers=None, min_value=None, max_value=None, cast_to=None):
    if valid_answers:
        options = '/'.join(valid_answers)
    elif min_value:
        options = ' - '.join([str(min_value), str(max_value) or 'inf'])
    else:
        options = ''

    if options:
        options = f'({options})'

    while True:
        print(question, options)
        resp = input()

        try:
            if cast_to:
                resp = cast_to(resp.replace(',', '.'))
        except:
            print('Infelizmente nesta resposta não entendi o que escreveu...')
            continue

        if ((valid_answers and resp not in valid_answers) or
                (min_value and resp <= min_value)):
            print('Infelizmente nesta resposta não entendi o que escreveu...')
            print('Lembre-se que as respostas válidas são', options)
            print()
            continue

        print()
        return resp


def wait_any_key_press(msg=''):
    input(msg or 'Aperte ENTER para prosseguirmos...')


def get_consultation_section_title(patient, section):
    line_sz = 50

    system('clear')

    print('*' * line_sz)
    print('* Doutor: Lewis Zimmerman'.ljust(line_sz - 2), '*')
    print(f'* Paciente: {patient.name}'.ljust(line_sz - 2), '*')
    print(f'* Idade: {patient.age}'.ljust(line_sz - 2), '*')

    if patient.name2:
        print(f'* Acompanhante: {patient.name2}'.ljust(line_sz - 2), '*')

    print(f'* Perguntas sobre: {section}'.ljust(line_sz - 2), '*')
    print('*' * line_sz)
