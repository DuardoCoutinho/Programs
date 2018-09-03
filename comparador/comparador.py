import formatacao as form
import sqlite3

db = sqlite3.connect('usuarios.db')
cur = db.cursor()



def escrevertxt(txt):
    print(txt)    
    
    
    
    sql = ('INSERT INTO user VALUES ("'+txt[0]+'", "'+txt[1]+'", '+txt[2]+');')
    cur.execute(sql)
    string = form.newstring(txt[0],txt[1],txt[2])
    db.commit()
    

def main():
    newuser = open('Relatorio.Customizado.GUID.60.csv').readlines()
    zero = True

    for txttest in newuser:
        
        txttest = form.formata(txttest)
        if zero:
            zero = False
            continue

        
        cur.execute('SELECT matricula FROM user WHERE matricula = '+txttest[0]+'')
        user = cur.fetchone()

        if  user is None:
               escrevertxt(txttest)


            
        
                    

if __name__=='__main__':
    main()
    db.close()
    
