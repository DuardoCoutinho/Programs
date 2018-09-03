import formatacao as form
import sqlite3

db = sqlite3.connect('usuarios.db')
cur = db.cursor()

<<<<<<< HEAD
#resul = open('result.txt', 'w')

def escrevertxt(txt):
    print(txt)      
    sql = ('INSERT INTO user VALUES ('+txt[0]+', "'+txt[1]+'", "'+txt[2]+'", "'+txt[3]+'");')
    cur.execute(sql)
    form.newstring(txt[0],txt[1],txt[2])
    db.commit()

def main():
    newuser = open('Relatorio.Customizado.GUID.60.csv').readlines()
    zero = True
=======


resul = open('result.txt', 'w')




def escrevertxt(txt):
    print(txt)    
    
    
    
    sql = ('INSERT INTO user VALUES ("'+txt[0]+'", "'+txt[1]+'", '+txt[2]+');')
    cur.execute(sql)
    string = form.newstring(txt[0],txt[1],txt[2])
    db.commit()
    
    



def main():
    newuser = open('novosusuarios.txt').readlines()
    
    
    
    
    
>>>>>>> f86889e00e77cb5b2cea3c0c3b80f0d47e49cda9
    for txttest in newuser:
        
        txttest = form.formata(txttest)
        txttest2 = txttest
<<<<<<< HEAD
        if zero:
            zero = False
            continue
        cur.execute("SELECT matricula from user where matricula = "+txttest[0]+"")
        user = cur.fetchone()

        if  user is None:
=======
        
        txttest = txttest[2]
        print(txttest)
        cur.execute("SELECT matricula from user where matricula = "+txttest+"")
        user = cur.fetchone()
        if  user is None:
            print('danone')
>>>>>>> f86889e00e77cb5b2cea3c0c3b80f0d47e49cda9
            escrevertxt(txttest2)
        
                    

if __name__=='__main__':
    
    main()
    db.close()
    
