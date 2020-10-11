from os import system

from utils import Patient, wait_valid_answer, wait_any_key_press


def initial_questionary(medical_record):
    system('clear')
    patient = Patient()

    print('Olá, seja bem-vindo(a) à consulta com o Dr. Lewis Zimmerman!')
    print('''\nTentarei lhe ajudar a diagnosticar, identificar, se possui ou não
    alguma das doenças transmitidas pelo mosquito aedes aegypti, o mosquito da dengue.''')

    print('\nDesculpe pela minha grosseria, nem perguntei o seu nome.')
    print('Como você se chama?')
    patient.name = input()

    print('\nÉ um prazer lhe atender,', patient.name)

    if wait_valid_answer('Ou está acompanhando alguém?', ['sim', 'não']) == 'sim':
        print('Entendo, então como ele se chama?')
        patient.name2 = patient.name
        patient.name = input()

        patient.age = wait_valid_answer(
            f'Então {patient.name2}, quantos anos inteiros {patient.name} tem?',
            min_value=0,
            cast_to=int
        )
    else:
        patient.age = wait_valid_answer(
            f'Então {patient.name}, quantos anos inteiros você tem?',
            min_value=0,
            cast_to=int
        )

    medical_record.input['neurological_damage_newborn'] = int(not patient.age)

    print('Obrigado, podemos começar a consulta!')
    wait_any_key_press()

    return patient, medical_record


def ask_about_fever(medical_record):

    print('Poderia nos informar a sua temperatura?')
    resp = float(input().replace(',', '.'))
    medical_record.input['body_temperature'] = resp

    print('E por quantos dias?')
    resp = int(input())
    medical_record.input['fever_duration'] = resp

    return medical_record


def ask_about_melasma(medical_record):
    while True:
        print('Apareceram algumas manchas na sua pele na última semana? (sim/não)')
        resp = input()

        if resp == 'não':
            medical_record.input['melasma'] = 0
            return medical_record

        if resp == 'sim':
            break

    print('Saberia dizer há quantos dias elas apareceram?')
    resp = 7 - int(input())

    medical_record.input['melasma'] = resp

    return medical_record


def ask_about_muscle_pain(medical_record):
    while True:
        print('Sentiu dor muscular durante a última semana? (sim/não)')
        resp = input()

        if resp == 'não':
            medical_record.input['muscle_pain_frequency'] = 0
            return medical_record

        if resp == 'sim':
            break

    print('Já que teve dores musculares, infelizmente, poderia dizer se doia com frequência?')

    while True:
        print('Numa escala de 1 (pouco frequente) a 10 (muito frequente), por favor')
        resp = int(input())

        if resp >= 1 and resp <= 10:
            medical_record.input['muscle_pain_frequency'] = resp
            break
        else:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')

    return medical_record


def ask_about_joint_pain(medical_record):
    while True:
        print('Sentiu dor nas articulações durante a última semana? (sim/não)')
        resp = input()

        if resp == 'não':
            medical_record.input['joint_pain_freq'] = 0
            medical_record.input['joint_pain_intensity'] = 0
            medical_record.input['joint_edema'] = 0
            medical_record.input['joint_edema_intensity'] = 0

            return medical_record

        if resp == 'sim':
            break

    print('Já que teve dores, infelizmente, poderia dizer se doia com frequência?')

    while True:
        print('Numa escala de 1 (pouco frequente) a 10 (muito frequente), por favor')
        resp = int(input())

        if resp >= 1 and resp <= 10:
            medical_record.input['joint_pain_freq'] = resp
            break
        else:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')

    print('Obrigado! Prosseguindo, então')
    print('E quanto à intensidade, doia muito?')

    while True:
        print('Numa escala de 1 (bastante fraca) a 10 (muito forte), por favor')
        resp = int(input())

        if resp >= 1 and resp <= 10:
            medical_record.input['joint_pain_intensity'] = resp
            break
        else:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')

    print('Obrigado! Prosseguindo, então...')
    print('Além das dores, percebeu algum inchaço nas articulações?')

    while True:
        print('Numa escala de 0 (não apareceu) a 10 (tinha por todo o corpo), por favor')
        resp = int(input())

        if resp >= 0 and resp <= 10:
            medical_record.input['joint_edema'] = resp
            break
        else:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')

    if resp == 0:
        medical_record.input['joint_edema_intensity'] = 0
        return medical_record

    print('Obrigado! Prosseguindo, então...')
    print('Já que ficaram inchadas, saberia dizer o quão inchada elas ficaram, no geral?')

    while True:
        print('Numa escala de 1 (pouco inchadas) a 10 (bastante inchadas), por favor')
        resp = int(input())

        if resp >= 1 and resp <= 10:
            medical_record.input['joint_edema_intensity'] = resp
            break
        else:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')

    return medical_record


def ask_about_conjuctivitis(medical_record):
    print('Sabe informar se estava com conjuntivite? (sim/não)')
    resp = input()

    medical_record.input['conjunctivitis'] = 0 if resp == 'não' else 1

    return medical_record


def ask_about_headache(medical_record):
    while True:
        print('Sentiu dor de cabeça durante a última semana? (sim/não)')
        resp = input()

        if resp == 'não':
            medical_record.input['headache_frequency'] = 0
            medical_record.input['headache_intensity'] = 0
            return medical_record

        if resp == 'sim':
            break

    print('Já que teve dores de cabeça, infelizmente, poderia dizer se doia com frequência?')

    while True:
        print('Numa escala de 1 (pouco frequente) a 10 (muito frequente), por favor')
        resp = int(input())

        if resp >= 1 and resp <= 10:
            medical_record.input['headache_frequency'] = resp
            break
        else:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')

    print('Obrigado! Prosseguindo, então')
    print('E quanto à intensidade da dor de cabeça, doia muito?')

    while True:
        print('Numa escala de 1 (bastante fraca) a 10 (muito forte), por favor')
        resp = int(input())

        if resp >= 1 and resp <= 10:
            medical_record.input['headache_intensity'] = resp
            break
        else:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')

    return medical_record


def ask_about_itch(medical_record):
    while True:
        print('Sentiu coceira na pele durante a última semana? (sim/não)')
        resp = input()

        if resp == 'não':
            medical_record.input['itch_intensity'] = 0
            return medical_record

        if resp == 'sim':
            break

    print('Já que teve coceira, poderia dizer qual era a intensidade?')

    while True:
        print('Numa escala de 1 (bastante fraca) a 10 (muito forte), por favor')
        resp = int(input())

        if resp >= 1 and resp <= 10:
            medical_record.input['itch_intensity'] = resp
            break
        else:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')

    return medical_record


def ask_about_ganglionic_hypertrophy(medical_record):
    while True:
        print('Observou o aparecimento de caroços (ínguas), principalmente na região do pescoço, durante a última semana? (sim/não)')
        resp = input()

        if resp == 'não':
            medical_record.input['ganglionic_hypertrophy_frequency'] = 0
            return medical_record

        if resp == 'sim':
            break

    print('Já que notou o aparecimento de caroços (ínguas), poderia dizer com que frequência apareciam?')

    while True:
        print('Numa escala de 1 (poucas vezes) a 10 (constantemente), por favor')
        resp = int(input())

        if resp >= 1 and resp <= 10:
            medical_record.input['ganglionic_hypertrophy_frequency'] = resp
            break
        else:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')

    return medical_record


def ask_about_neurological_damage(medical_record):
    print('''Saberia informar se o paciente possui alguma
    sequela neurológica ou se já tem o resultado de algum exame? (sim/não)''')

    if input() == 'não':
        medical_record.input['neurological_damage'] = 0
        return medical_record

    while True:
        print('Já que pode nos informar, o paciente tem ou não tem alguma sequela neurológica? (tem/não)')
        resp = input()

        if resp not in ['tem', 'não']:
            print('Infelizmente, esta resposta não pode ser utilizada pela gente...')
            continue

        medical_record.input['neurological_damage'] = 1 if resp == 'tem' else 0
        return medical_record
