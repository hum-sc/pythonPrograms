def run() :
    myList = [1, 'Hello', True, 4.5]
    myDict = {
        'firstName' : 'Humberto',
        'surName' : 'SC'
    }
    superList = [
        {'firstName' : 'Humberto','surName' : 'SC'},
        {'firstName' : 'Humberto','surName' : 'SalinasC'},
        {'firstName' : 'Humberto','surName' : 'SCortés'},
        {'firstName' : 'Humberto','surName' : 'Salinas Cortés'}
    ]
    superDic = {
        'integerNums' : [1,2,3,4,5],
        'floatingNums' : [1.2,2.3,3.4,4.5]
    }


    print('We going to print list values')
    for i in myList : 
        print(i)
    
    print('we going to print Dictoinary values')
    for key, value in myDict.items() :
        print('the ', key, ' is ', value)
    
    print('We going to print Super List values')
    for i in superList :
        for key, value in i.items():
            print (key, ' - ', value)
    
    print('We going to print Super Dictionary values')
    for key, value in superDic.items() :
        print('the ', key, ' values are')
        for i in value :
            print(i)
    
            


if __name__ == '__main__':
    run()