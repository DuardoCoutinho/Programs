import formatacao as form

resul = open('result.txt', 'w')
todo_user = open('todosusuarios.csv','a')

def escrevertxt(txt):
    
    resul.write(txt)
    todo_user.write(txt)
    
    #print (txt)



def main():
    newuser = open('txtformatado.csv').readlines()
    user = open('todosusuarios.csv').readlines()
    

    for txttest in newuser:
        cont = 0
        if len(user) == 0:
            escrevertxt(txttest)
        else:
            for txtofic in user:
                cont += 1
                if cont == len(user):
                    escrevertxt(txttest)
                elif str(txtofic) == str(txttest):
                    
                    break
            
                





if __name__=='__main__':
    form.main()
    main()
    