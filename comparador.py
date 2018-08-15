

txt1 = open('Cria-Usuarios-CSV PRONTO - User.csv')
txt2 = open('Cria-Usuarios-CSV PRONTO - User (copia).csv')
texto_oficial = txt1.readlines()
resul = open('result.txt', 'w')


def escrevertxt(txt):
    resul.write(txt)
    

for txttest in txt2.readlines():
    
    cont = 0
    for txtofic in texto_oficial:
        
        
        cont = 1 + cont
        if txttest == txtofic:
            break
        elif cont == len(texto_oficial):
            print(txttest)
            escrevertxt(txttest)





            

        
        
        

                
        