# criador de mascara de cnpj (xx.xxx.xxx/xxxx-xx)
def mascara_cnpj(numeros):
    if len(numeros) != 14 or not numeros.isdigit():
        return "CNPJ inválido"
    else:
        cnpj_formatado = f"{numeros[:2]}.{numeros[2:5]}.{numeros[5:8]}/{numeros[8:12]}-{numeros[12:]}"
        return cnpj_formatado
    
numeros = input('Digite os numeros do seu cnpj: ')
cnpj_com_mascara = mascara_cnpj(numeros)
print(cnpj_com_mascara)