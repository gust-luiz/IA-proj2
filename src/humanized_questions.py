def ask_about_fiver(medical_record):

    print('Poderia nos informa a sua temperatura?')
    resp = float(input().replace(',', '.'))
    medical_record.input['temperatura'] = resp

    print('E por quantos dias?')
    resp = int(input())
    medical_record.input['duração da febre'] = resp

    return medical_record


def ask_about_melasma(medical_record):
    from random import randint
    while(True):
        print('Apareceu algumas manchas na sua pele na última semana? (sim/não)')
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
