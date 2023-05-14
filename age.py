driving = input('請問是否有駕照_(請回答有/無):')
age = input('請問您今年芳齡?')
age = int(age)

if driving == '有':
    if age <=18:
        print('無照駕駛，得罰款2萬4千元整，請勿再以身試法')
    elif age >=19 and age <=74:
        print('喝酒不開車、開車不喝酒、行車安全人人有責')
    else:
        print('很抱歉，您屬於老年駕駛者，需重新完成考照與體檢程序，方可繼續駕駛，且駕照有效期限2年為限')

elif driving == '無':
    if age <=17:
        print('您尚未年滿18，不得行駛車輛，腳踏車除外')
    else:
        print('您符合考照資格，若有意願考照，請洽_____專線____，謝謝!')