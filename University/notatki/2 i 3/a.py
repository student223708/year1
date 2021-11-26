import mymath

def display_university_address():
    print("Cracow University of Economics Rakowicka 27 31-510 Kraków, POLAND")

    
def kwadrat():
    i=0
    j=0
    for i in range(0,8,3):
        for j in range(1,4):
            print(f' {i+j}',end='')
        print()
    return 0

def multiplication(x, y):
    print( f"{x} * {y} = {x*y}")


def function(n):
    for n in range(1,n+1,1):
        print(n)
        


def main():
    while True:
        x=mymath.generate_number()
        if x==mymath.read_number():break
    print("You won")



