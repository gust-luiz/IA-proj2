from os import system

from utils import Patient, wait_any_key_press, wait_valid_answer

NO_SYMPTOMS_MSG = 'Ainda bem que não teve {}! Menos um sinal de problemas, não é mesmo?'


def initial_questionary(medical_record):
    system('clear')
    patient = Patient()

    print('Olá, seja bem-vindo(a) à consulta com o Dr. Lewis Zimmerman!')
    print('''\nTentarei lhe ajudar a diagnosticar, identificar, se possui ou não
    alguma das doenças transmitidas pelo mosquito aedes aegypti, o mosquito da dengue.''')

    print('\nDesculpe pela minha grosseria, nem perguntei o seu nome.')
    print('Como você se chama?')
    patient.name = input().capitalize()

    print('\nÉ um prazer lhe atender,', patient.name, '!')
    print()

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

    wait_any_key_press('\nObrigado, podemos começar a consulta!')

    return patient, medical_record


def ask_about_fever(medical_record, section):
    if wait_valid_answer('Em algum momento nesta última semana, sentiu febre?', ['sim', 'não']) == 'não':
        medical_record.input['body_temperature'] = 36.5
        medical_record.input['fever_duration'] = 0

        print(NO_SYMPTOMS_MSG.format(section))

        return medical_record

    print('Já que teve febre nesta última semana,')
    medical_record.input['body_temperature'] = wait_valid_answer(
        'Poderia nos informar quanto estava sua temperatura quando foi aferida, medida, no termômetro?',
        min_value=36.5,
        max_value=40.9,
        cast_to=float
    )

    print('Entendi...')
    medical_record.input['fever_duration'] = wait_valid_answer(
        'E poderia nos informar por quantos dias seguidos esteve com febre?',
        min_value=0,
        max_value=7,
        cast_to=int
    )

    return medical_record


def ask_about_melasma(medical_record, section):
    if wait_valid_answer('Em algum momento nesta última semana, apareceram manchas na pele?', ['sim', 'não']) == 'não':
        medical_record.input['melasma'] = 0

        print(NO_SYMPTOMS_MSG.format(section))

        return medical_record

    print('Então, já que elas apareceram,')
    medical_record.input['melasma'] = 7 - wait_valid_answer(
        'Poderia nos informar há quantos dias elas apareceram?',
        min_value=0,
        max_value=7,
        cast_to=int
    )

    return medical_record


def ask_about_muscle_pain(medical_record, section):
    if wait_valid_answer('Em algum momento nesta última semana, sentiu alguma dor muscular?', ['sim', 'não']) == 'não':
        medical_record.input['muscle_pain_frequency'] = 0

        print(NO_SYMPTOMS_MSG.format(section))

        return medical_record

    print('E já que teve dores musculares,')
    medical_record.input['muscle_pain_frequency'] = wait_valid_answer(
        'Poderia dizer se doia com frequência, numa escala de "pouco frequente" a "muito frequente"?',
        min_value=1,
        max_value=10,
        cast_to=int
    )

    return medical_record


def ask_about_joint_pain(medical_record, section):
    if wait_valid_answer(
        'Em algum momento nesta última semana, sentiu alguma dor nas articulações, juntas?',
        ['sim', 'não']
    ) == 'não':
        medical_record.input['joint_pain_freq'] = 0
        medical_record.input['joint_pain_intensity'] = 0
        medical_record.input['joint_edema'] = 0
        medical_record.input['joint_edema_intensity'] = 0

        print(NO_SYMPTOMS_MSG.format(section))

        return medical_record

    print('E, já que teve dores nas juntas,')
    medical_record.input['joint_pain_freq'] = wait_valid_answer(
        'Poderia informar se doia com frequência, numa escala de "pouco frequente" a "muito frequente"?',
        min_value=1,
        max_value=10,
        cast_to=int
    )

    print('Obrigado! E quanto à intensidade...')
    medical_record.input['joint_pain_intensity'] = wait_valid_answer(
        'Doia muito, numa escala de "bastante fraca" a "muito forte"?',
        min_value=1,
        max_value=10,
        cast_to=int
    )

    print('Obrigado!')
    print('E além das dores, ')
    medical_record.input['joint_edema'] = wait_valid_answer(
        'Percebeu algum inchaço nas juntas, numa escala de "não apareceu" a "tinha por todo o corpo"?',
        min_value=0,
        max_value=10,
        cast_to=int
    )

    if not medical_record.input['joint_edema']:
        medical_record.input['joint_edema_intensity'] = 0
        return medical_record

    print('Tendo esses inchaços aparecidos,')
    medical_record.input['joint_edema_intensity'] = wait_valid_answer(
        'Conseguiria me informar o quão inchado estava, numa escala de "pouco inchadas" a "bastante inchadas"?',
        min_value=1,
        max_value=10,
        cast_to=int
    )

    return medical_record


def ask_about_conjuctivitis(medical_record, section):
    if wait_valid_answer(
        'Em algum momento nesta última semana, teve conjuntivite?',
        ['sim', 'não']
    ) == 'não':
        print(NO_SYMPTOMS_MSG.format(section))

        medical_record.input['conjunctivitis'] = 0
    else:
        medical_record.input['conjunctivitis'] = 1

    return medical_record


def ask_about_headache(medical_record, section):
    if wait_valid_answer('Nesta última semana, sentiu dor de cabeça?', ['sim', 'não']) == 'não':
        medical_record.input['headache_frequency'] = 0
        medical_record.input['headache_intensity'] = 0

        print(NO_SYMPTOMS_MSG.format(section))

        return medical_record

    print('Já que teve dores de cabeça,')
    medical_record.input['headache_frequency'] = wait_valid_answer(
        'Consegui dizer se doia com frequência, numa escala de "pouco frequente" a "muito frequente"?',
        min_value=1,
        max_value=10,
        cast_to=int
    )

    medical_record.input['headache_intensity'] = wait_valid_answer(
        'E qual era a intensidade, numa escala de "bastante fraca" a "muito forte"?',
        min_value=1,
        max_value=10,
        cast_to=int
    )

    return medical_record


def ask_about_itch(medical_record, section):
    if wait_valid_answer('Em algum momento nesta última semana, teve coceira?', ['sim', 'não']) == 'não':
        medical_record.input['itch_intensity'] = 0

        print(NO_SYMPTOMS_MSG.format(section))

        return medical_record

    medical_record.input['itch_intensity'] = wait_valid_answer(
        'E coçou muito, numa escala "bastante fraca" a "muito forte"?',
        min_value=1,
        max_value=10,
        cast_to=int
    )

    return medical_record


def ask_about_ganglionic_hypertrophy(medical_record, section):
    resp = wait_valid_answer(
        '''Em algum momento nesta última semana, apareceu algum caroço ou inchaço perto do pescoço?
        numa escala de "não apareceu" a "quase não tinha espaço livre".''',
        min_value=0,
        max_value=10,
        cast_to=int
    )

    if not resp:
        print(NO_SYMPTOMS_MSG.format(section))

    medical_record.input['ganglionic_hypertrophy_frequency'] = resp

    return medical_record


def ask_about_hemorrhagic_dyscrasia(medical_record, section):
    resp = wait_valid_answer(
        '''Em algum momento nesta última semana, notou ou alguém notou se teve algum sangramento espontâneo,
        sem motivo aparente?
        numa escala de "não sangrou" a "constantemente"''',
        min_value=0,
        max_value=10,
        cast_to=int
    )

    if not resp:
        print(NO_SYMPTOMS_MSG.format(section))

    medical_record.input['hemorrhagic_dyscrasia_frequency'] = resp

    return medical_record


def ask_about_neurological_damage(medical_record, section):
    if wait_valid_answer('''Saberia informar se há alguma
        sequela neurológica ou se já tem o resultado de algum exame?''',
        ['tem', 'não']
    ) == 'não':
        medical_record.input['neurological_damage'] = 0

        print(NO_SYMPTOMS_MSG.format(section))

    else:
        medical_record.input['neurological_damage'] = 1

    return medical_record
