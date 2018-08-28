import formatacao as form
import sqlite3

db = sqlite3.connect('usuarios.db')
cur = db.cursor()



resul = open('result.txt', 'w')




def escrevertxt(txt):
    print(txt)    
    
    
    
    sql = ('INSERT INTO user VALUES ("'+txt[0]+'", "'+txt[1]+'", '+txt[2]+');')
    cur.execute(sql)
    string = form.newstring(txt[0],txt[1],txt[2])
    db.commit()
    
    



def main():
    newuser = open('novosusuarios.txt').readlines()
    
    
    
    
    
    for txttest in newuser:
        
        txttest = form.formata(txttest)
        txttest2 = txttest
        
        txttest = txttest[2]
        print(txttest)
        cur.execute("SELECT matricula from user where matricula = "+txttest+"")
        user = cur.fetchone()
        if  user is None:
            print('danone')
            escrevertxt(txttest2)
        
                    

if __name__=='__main__':
    #form.main()
    main()
    db.close()
    
