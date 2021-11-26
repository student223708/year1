text = input("Write something: ")

def function(text):
    x=0
    i=0
    while i<len(text):
        if ((text[i]=='e') or (text[i]=='E')):
            x=x+1
        i=i+1
    return print(x)
        
function(text)