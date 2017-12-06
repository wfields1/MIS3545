trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}

def speak_Chinese(number):
    num = str(number)
    if str(num) <= 10:
        return trans[num]
    elif str(num) <= 19:
        return 'shi ' + trans[num[1]]
    elif str(num[1]) <= 99:
        return trans[num[0]] + ' shi ' + trans[num[1]]
    elif str(num) <= 999:
        return trans[num[0]] + ' bai ' + trans[num[1]] + ' shi ' + trans[num[2]]
    '''
    number: an integer, 0<=number<=999

    Returns: a string that is the number in Chinese
    '''

#For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()
