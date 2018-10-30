
import sqlite3
import os

db = sqlite3.connect('usuarios.db')
cur = db.cursor()

resul = open("Usuarios-novos.txt", "w")
bloquear = open("Usuarios-bloqueados.txt", "w")

    
def main():

    #txttest[0] = Matricula
    #txttest[1] = Nome
    #txttest[2] = Sobrenome
    #txttest[3] = Descrição

    
    newuser = open('Relatorio.Customizado.GUID.60.csv').readlines()
    zero = True
    
    for txttest in newuser:
        
        txttest = formata(txttest)
        cur.execute('SELECT matricula FROM user WHERE matricula = '+txttest[0]+'')
        user = cur.fetchone()
        if zero:
            zero = False
            continue
        
       
        if  user is None: #Cria usuario no banco
               criaruser(txttest)
           
               
        else:
            veriestado(txttest)



def criaruser(txt):
    newstring(txt[1], txt[2], txt[0])
    veriestado(txt)
    sql = ('INSERT INTO user VALUES ('+txt[0]+', "'+txt[1]+'", "'+txt[2]+'","'+txt[3]+'")')
    cur.execute(sql)
    db.commit()
    
                    
def block(matri):
    bloquear.write(matri)
    sql = ('UPDATE user SET estado = "Bloqueado" WHERE matricula='+matri+'')
    cur.execute(sql)
    db.commit()
    
def unblock(matri):
    sql = ('UPDATE user SET estado = "Cursando" WHERE matricula='+matri+'')
    cur.execute(sql)
    db.commit()
    



zero = True
def newstring(name, sobname, matri):
    global zero
    if zero:
        string = 'DN,objectClass,sAMAccountName,givenName,userPrincipalName,sn'
        zero = False
        resul.write(string)

    string = "\n\"CN={matricula},OU=Alunos,DC=FaculdadeMeta,DC=EDU\",user,{matricula},{nome},{matricula}@faculdademeta.edu,{sobrenome}".format(sobrenome = sobname, matricula = matri, nome=name)
    print(string)
    resul.write(string)


def formata(str1):
    str1 = str1.replace("\n", "")
    str1 = str1.replace("\r", "")
    str1 = str1.split(';')
    return str1

def veriestado(user):
    
    if user[3] == 'Cursando' or user[3] == 'Pre-matricula' :  # se houver no banco, verificação do estado dele
        unblock(user[0])
    else:
        block(user[0])




if __name__=='__main__':
    main()
    resul.close()
    bloquear.close()
    
    os.system('csvde -i -f C:\\Users\\Administrador.WIN-TRRJKTG898F\\Desktop\\Programs-master(3)\\Programs-master\\comparador\\Usuarios-novos.txt')
    os.system('dsquery user -stalepwd 2000 | dsmod user -pwd @gt1-m3t4 -mustchpwd yes -disabled no')
    
    db.close()
        





        
