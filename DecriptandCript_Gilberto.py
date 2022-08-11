# -*- coding: utf-8 -*-

def cript(str_, chave):
    str_retorno =  ""
    max = 126
    for a in str_:
        num_cript = ord(a) + chave
    
        if(num_cript > max):
            num_cript = 32 + (num_cript % max)
        
        char_crip = chr(num_cript)
    
        str_retorno = str_retorno + char_crip
        
    return str_retorno

chave = 18
str_ = "oi"
out = cript(str_, chave)
print(out)  


def decript(msg, chave):
    str_retorno =  ""
    min = 32
    for a in msg:
        num_cript = ord(a) - chave
    
        if(num_cript < min):
            num_cript = 126 - (min % num_cript)
        
        char_crip = chr(num_cript)
    
        str_retorno = str_retorno + char_crip
        
    return str_retorno


chave = 18
str_ = "#{"
out = decript(str_, chave)
print(out)  

'''
filename = "test.txt"
filename_out = "out.txt"

file_out = open(filename_out, 'w+')

with open(filename, 'r', errors='ignore') as file:
    for line in file:
        print(line)
        cript_line = cript(line[:len(line)-1], chave)
        print(cript_line)
        file_out.write(cript_line + "\n")
        
file_out.close()



filename = "test.txt"
filename_out = "out.txt"

file_out = open(filename_out, 'w+')

with open(filename, 'r', errors='ignore') as file:
    for line in file:
        print(line)
        decript_line = decript(line[:len(line)-1], chave)
        print(decript_line)
        file_out.write(decript_line + "\n")
        
file_out.close()
'''




