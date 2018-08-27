import formatacao as form
import sqlite3

db = sqlite3.connect('usuarios.db')
cur = db.cursor()

cur.execute("SELECT matricula from user")

resul = open('result.txt', 'w')




def escrevertxt(txt):
    print(type(txt))    
    #resul.write(txt)
    
    #print(len(j))
    sql = ('INSERT INTO user VALUES ("'+txt[0]+'", "'+txt[1]+'", '+txt[2]+');')
    cur.execute(sql)
    #string = form.newstring(j[0],j[1],j[2])
    db.commit()
    
    print(txt)



def main():
    newuser = open('novosusuarios.txt').readlines()
    
    user = cur.fetchall()
    
    
    
    for txttest in newuser:
        
        txttest = form.formata(txttest)
        txttest2 = txttest
        #print(type(txttest2))
       
        txttest = txttest[2]
        
        print('passou por aqui')
        
        cont = 0
        if len(user) == 0:
            escrevertxt(txttest)
        else:
            for txttuple in user:
                    for txtofic in txttuple:
                        
                        cont += 1
                        print(txttest)
                        print(len(txttest))
                        print(txtofic)
                        print(len(str(txtofic)))
                        print(txttest == txtofic)
                        if cont == len(user):
                            print(cont)
                            print('oi')
                            escrevertxt(txttest2)
                        elif str(txtofic) == str(txttest):
                            print('break')
                            break

if __name__=='__main__':
    #form.main()
    main()





#db.close()
    
