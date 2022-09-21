from math import sqrt

def figure():
    a = str(input())

    if a == 'triangle':
        def triangle():
            b = int(input())
            c = int(input())
            d = int(input())
            def tri():
                if b+c> d and c+d>b and d+b>c:                  
                    p = (b+c+d)/2
                    pl = sqrt(p*(p-b)*(p-c)*(p-d))
                    print(pl)
                else:
                    print('triangle does not exist')
            tri()
        triangle()

    if a == 'circle':
        def circle():
            pp = 3.14
            r = int(input())
            pl1  = (pp*r)**2
            print(pl1)
        circle()
        
    if a == 'rectangle':
        def rectangle():
            q = int(input())
            w = int(input())
            plt = q*w
            print(plt)
        rectangle()
        
figure()
            
