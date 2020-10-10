def ask_about_fiver(medical_record):

    print('Poderia nos informar a sua temperatura?')
    resp = float(input().replace(',', '.'))
    medical_record.input['temperatura'] = resp

    print('E por quantos dias?')
    resp = int(input())
    medical_record.input['duração da febre'] = resp

    return medical_record


def ask_about_melasma(medical_record):
    from random import randint
    while(True):
        print('Apareceram algumas manchas na sua pele na última semana? (sim/não)')
        resp = input()

        if resp == 'não':
            medical_record.input['melasma'] = 0
            medical_record.input['melasma_occurence'] = 0
            return medical_record

        if resp == 'sim':
            break

    print('Saberia dizer há quantos dias elas apareceram?')
    resp = 7 - int(input())

    medical_record.input['melasma'] = resp
    medical_record.input['melasma_occurence'] = randint(0, 10)

    return medical_record


def ask_about_muscle_pain(medical_record):
    while True:
        print('Sentiu dor muscular durante a última semana? (sim/não)')
        resp = input()

        if resp == 'não':
            medical_record.input['muscle_pain'] = 0
            return medical_record

        if resp == 'sim':
            break

    print('Entre 1 (pouco frequente) e 3 (muito frequente), qual foi a frequência com que sentiu dores musculares? (1/2/3)')
    resp = int(input())

    medical_record.input['muscle_pain'] = resp

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
    print('E quanto à intensidada, doia muito?')

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

        if resp >= 1 and resp <= 10:
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
