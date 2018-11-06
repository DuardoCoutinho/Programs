import xlstocsv
import sqlite3
import os

db = sqlite3.connect('usuarios.db')
cur = db.cursor()
resul = open("Usuarios-novos.", "w")
novosalunos = []

def main():
    #txttest[0] = Matricula
    #txttest[1] = Nome
    #txttest[2] = Sobrenome
    #txttest[3] = Descrição
    newuser = open('resultados.csv').readlines()
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
               novosalunos.append(txttest)
               
        else:
            veriestado(txttest)



def criaruser(txt):
    newstring(txt[1], txt[2], txt[0])
    sql = ('INSERT INTO user VALUES ('+txt[0]+', "'+txt[1]+'", "'+txt[2]+'","'+txt[3]+'")')
    cur.execute(sql)
    db.commit()
    
                    
def bloquear(user):
    print(user)
    sql = ('UPDATE user SET estado = "'+user[3]+'" WHERE matricula='+user[0]+'')
    command = 'dsmod user cn='+user[0]+',ou=alunos,dc=faculdademeta,dc=edu -disabled yes'
    os.system(command)
    cur.execute(sql)
    db.commit()
    
def desbloquear(user):
    print(user)
    sql = ('UPDATE user SET estado = "'+user[3]+'" WHERE matricula='+user[0]+'')
    command = 'dsmod user cn='+user[0]+',ou=alunos,dc=faculdademeta,dc=edu -disabled no'
    os.system(command)
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
    str1 = str1.replace("-","")
    str1 = str1.split(';')
    del(str1[5])
    del(str1[2])
    del(str1[0])

    return str1

def veriestado(user):
    sql = "SELECT estado FROM user WHERE matricula = "+user[0]
    cur.execute(sql)
    for row in cur.fetchone():
        if not user[3] == row:
            if user[3] == 'Cursando' or user[3] == 'Pre-matricula':  # se houver no banco, verificação do estado dele
                desbloquear(user)
            else:
                bloquear(user)


def veriestado_novosalunos():
    for aluno in novosalunos:
        veriestado(aluno())

if __name__=='__main__':
    xlstocsv.main()
    main()
    resul.close()
    os.system('csvde -i -f C:\\Users\\Administrador.WIN-TRRJKTG898F\\Desktop\\Programs-master(3)\\Programs-master\\comparador\\Usuarios-novos.txt')
    os.system('dsquery user -stalepwd 2000 | dsmod user -pwd @gt1-m3t4 -mustchpwd yes ')

    veriestado_novosalunos()
    os.remove('resultados.csv')
    os.remove('relaotrio.xls')
    
    db.close()
        





        
