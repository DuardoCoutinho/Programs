from datetime import datetime

now = datetime.now()
txt1 = open('novosusuarios.txt') 
resul = open('newuseradd.txt', "w")
zero = True

def main():
       
    for txt in txt1.readlines():
        
        j = txt.split('\t')
        #newstring(formata(j[0]), formata(j[1]), formata(j[2]))
        
def newstring(matri, name, sobname):
    global zero
    if zero:
        string = 'DN,objectClass,sAMAccountName,givenName,userPrincipalName,sn'
        zero = False
    else:
        string = "\n\"CN=" + sobname +",OU=Alunos,DC=FaculdadeMeta,DC=EDU\",user,"+matri+","+name+","+matri+"@faculdademeta.edu,"+sobname
    escrevertxt(string)
    
    

def escrevertxt(txt):
    resul.write(txt)
    
def formata(str1):
    
    str1 = str1.replace("\n","")
    str1 = str1.replace("\r", "")
    str1 = str1.split(';')
    return str1
    


if __name__=="__main__":
    main()
    

