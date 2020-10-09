def ask_about_fiver(medical_record):

    print('Poderia nos informa a sua temperatura?')
    resp = float(input().replace(',', '.'))
    print('\tresp', resp)
    medical_record.input['temperatura'] = resp

    print('E por quantos dias?')
    resp = int(input())
    print('\tresp', resp)
    medical_record.input['duração da febre'] = resp

    return medical_record
