
import sqlite3
import os

db = sqlite3.connect('usuarios.db')
cur = db.cursor()

resul = open("Usuarios-novos.txt", "w")

usuarios_para_desbloquear = []
    
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
        if zero or txttest[0] == user:
            zero = False
            continue
        
       
        if  user is None: #Cria user no banco
               criaruser(txttest)
               usuarios_para_desbloquear.append(txttest[0])
               
        else:
            veriestado(txttest, False)



def criaruser(txt):
    newstring(txt[1], txt[2], txt[0])
    sql = ('INSERT INTO user VALUES ('+txt[0]+', "'+txt[1]+'", "'+txt[2]+'","'+txt[3]+'")')
    cur.execute(sql)
    db.commit()        
                    
def block(matri):
    sql = ('UPDATE user SET estado = "Bloqueado" WHERE matricula='+matri+'')
    cur.execute(sql)
    db.commit()
    
def unblock(matri):

    sql = ('UPDATE user SET estado = "Cursando" WHERE matricula='+matri+'')

    cur.execute(sql)
    db.commit()
    
def exclui(matri):
    sql = ('DELETE FROM user WHERE matricula='+matri+'')
    cur.execute(sql)
    db.commit()


zero = True
def newstring(name, sobname, matri):
    global zero
    if zero:
        string = 'DN,objectClass,sAMAccountName,givenName,userPrincipalName,sn'
        zero = False
    else:
        string = "\n\"CN={nome},OU=Alunos,DC=FaculdadeMeta,DC=EDU\",user,{matricula},{nome},{matricula}@faculdademeta.edu,{sobrenome}".format(sobrenome = sobname, matricula = matri, nome=name)
    print(string)
    resul.write(string)


def formata(str1):
    str1 = str1.replace("\n", "")
    str1 = str1.replace("\r", "")
    str1 = str1.split(';')
    return str1

def veriestado(user, veri):
    if not veri:
        if user[3] == 'Cursando':  # se houver no banco, verificação do estado dele
            unblock(user[0])

        elif user[3] == 'Trancado':
            block(user[0])

        elif user[3] == 'Concluido' or user[3] == 'Saiu' or user[3] == 'Cancelado':
            exclui(user[0])
        else:
            print('Não deu certo')

    else:
        pass





if __name__=='__main__':
    main()
    db.close()
    local = input('Local dos arquivo:')
    #os.system('csvde -i -f {} -j C:'.format(local))
    print('csvde -i -f {}Usuarios-novos.txt -j C:'.format(local))

    #veriestado()
    print(usuarios_para_desbloquear)
    print(len(usuarios_para_desbloquear))