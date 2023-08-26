class Assignment2():
    def Subfields():
        print('Sub-fields in AI are:','\nMachine Learning', '\nNeural Networks', '\nVision', '\nRobotics','\nSpeech Processing', '\nNatural Language Processing')
    
    
    def evenOdd():
        num=int(input('Enter a number:'))    
        if (num % 2 == 0):
            print(num,"is Even number")
            message= num,"is Even number"
        else:
            print(num,"is Odd number")
            message= num,"is Odd number"
            return message
    
    
    def eligible():
        gen=input('Your Gender(Male, Female):')
        age=int(input('Your Age:'))
        a='Male'
        b='Female'
        if(gen==a):
            if(age>=21):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        elif(gen==b):
            if(age>=18):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        else:
            print("Invalid Input")

   
    def percentage():
        s1=int(input('Subject1='))
        s2=int(input('Subject2='))
        s3=int(input('Subject3='))
        s4=int(input('Subject4='))
        s5=int(input('Subject5='))
        print()
        Tot=s1+s2+s3+s4+s5
        print('Total:',Tot )
        percent=(Tot/500)*100
        print("Percentage:", percent)
        return percent

   
    def triangle():
        h=int(input('Height:'))
        b=int(input('Breadth:'))
        Af=(h*b)/2
        print('Area formula: (Height*Breadth)/2''\nArea of Triangle:', Af)
        h1=int(input('Height1:'))
        h2=int(input('Height2:'))
        b1=int(input('Breadth:'))
        p=h1+h2+b1
        print('Perimeter formula:Height1+Height2+Breadth','\nPerimeter of Triangle:',p)
