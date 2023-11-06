# Задание 8

def acronym_func(user_input):
    try:
        data_type = isinstance(user_input,str)
        acronym = ''

        for w in user_input.split():
            acronym += w[0].upper()
        print(acronym)

    except:
        print("Другой тип данных")

acronym_func(8)