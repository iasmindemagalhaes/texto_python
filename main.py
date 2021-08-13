texto = input('Insira um texto: ')
alfabeto = ('abcdefghijklmnopqrstuvxwyz_')
texto = texto.lower()
texto = texto.replace('\\n', '_')
novo_texto = texto
for x in range(len(texto)):
    if texto[x] == ' ':
        novo_texto = novo_texto.replace(texto[x], '_')
    if texto[x] == 'á' or texto[x] == 'à' or texto[x] == 'ã' or texto[x] == 'â' or texto[x] == 'ä':
        novo_texto = novo_texto.replace(texto[x], 'a')
    if texto[x] == 'é' or texto[x] == 'ê' or texto[x] == 'è' or texto[x] == 'ë':
        novo_texto = novo_texto.replace(texto[x], 'e')
    if texto[x] == 'í' or texto[x] == 'ì'or texto[x] == 'î' or texto[x] == 'ï':
        novo_texto = novo_texto.replace(texto[x], 'i')
    if texto[x] == 'ó' or texto[x] == 'ò' or texto[x] == 'õ' or texto[x] == 'ô' or texto[x] == 'ö':
        novo_texto = novo_texto.replace(texto[x], 'o')
    if texto[x] == 'ú' or texto[x] == 'ü':
        novo_texto = novo_texto.replace(texto[x], 'u')
    if texto[x] == 'ç':
        novo_texto = novo_texto.replace(texto[x], 'c')
    if texto[x] not in alfabeto:
        novo_texto = novo_texto.replace(texto[x], '')
palavras = novo_texto.split('_')
letras = novo_texto.replace('_', '')
qtd_letras_texto = len(letras)
qtd_letras_texto = int(qtd_letras_texto)
qtd_letra_a = 0
qtd_letra_b = 0
qtd_letra_c = 0
qtd_letra_d = 0
qtd_letra_e = 0
qtd_letra_f = 0
qtd_letra_g = 0
qtd_letra_h = 0
qtd_letra_i = 0
qtd_letra_j = 0
qtd_letra_k = 0
qtd_letra_l = 0
qtd_letra_m = 0
qtd_letra_n = 0
qtd_letra_o = 0
qtd_letra_p = 0
qtd_letra_q = 0
qtd_letra_r = 0
qtd_letra_s = 0
qtd_letra_t = 0
qtd_letra_u = 0
qtd_letra_v = 0
qtd_letra_x = 0
qtd_letra_w = 0
qtd_letra_y = 0
qtd_letra_z = 0

for i in range(len(letras)):
    if letras[i] == 'a':
        qtd_letra_a += 1
    elif letras[i] == 'b':
        qtd_letra_b += 1
    elif letras[i] == 'c':
        qtd_letra_c += 1
    elif letras[i] == 'd':
        qtd_letra_d += 1
    elif letras[i] == 'e':
        qtd_letra_e += 1
    elif letras[i] == 'f':
        qtd_letra_f += 1
    elif letras[i] == 'g':
        qtd_letra_g += 1
    elif letras[i] == 'h':
        qtd_letra_h += 1
    elif letras[i] == 'i':
        qtd_letra_i += 1
    elif letras[i] == 'j':
        qtd_letra_j += 1
    elif letras[i] == 'k':
        qtd_letra_k += 1
    elif letras[i] == 'l':
        qtd_letra_l += 1
    elif letras[i] == 'm':
        qtd_letra_m += 1
    elif letras[i] == 'n':
        qtd_letra_n += 1
    elif letras[i] == 'o':
        qtd_letra_o += 1
    elif letras[i] == 'p':
        qtd_letra_p += 1
    elif letras[i] == 'q':
        qtd_letra_q += 1
    elif letras[i] == 'r':
        qtd_letra_r += 1
    elif letras[i] == 's':
        qtd_letra_s += 1
    elif letras[i] == 't':
        qtd_letra_t += 1
    elif letras[i] == 'u':
        qtd_letra_u += 1
    elif letras[i] == 'v':
        qtd_letra_v += 1
    elif letras[i] == 'w':
        qtd_letra_w += 1
    elif letras[i] == 'x':
        qtd_letra_x += 1
    elif letras[i] == 'y':
        qtd_letra_y += 1
    elif letras[i] == 'z':
        qtd_letra_z += 1

print('a = {:.2f} %'.format(qtd_letra_a * 100 / qtd_letras_texto))
print('b = {:.2f} %'.format(qtd_letra_b * 100 / qtd_letras_texto))
print('c = {:.2f} %'.format(qtd_letra_c * 100 / qtd_letras_texto))
print('d = {:.2f} %'.format(qtd_letra_d * 100 / qtd_letras_texto))
print('e = {:.2f} %'.format(qtd_letra_e * 100 / qtd_letras_texto))
print('f = {:.2f} %'.format(qtd_letra_f * 100 / qtd_letras_texto))
print('g = {:.2f} %'.format(qtd_letra_g * 100 / qtd_letras_texto))
print('h = {:.2f} %'.format(qtd_letra_h * 100 / qtd_letras_texto))
print('i = {:.2f} %'.format(qtd_letra_i * 100 / qtd_letras_texto))
print('j = {:.2f} %'.format(qtd_letra_j * 100 / qtd_letras_texto))
print('k = {:.2f} %'.format(qtd_letra_k * 100 / qtd_letras_texto))
print('l = {:.2f} %'.format(qtd_letra_l * 100 / qtd_letras_texto))
print('m = {:.2f} %'.format(qtd_letra_m * 100 / qtd_letras_texto))
print('n = {:.2f} %'.format(qtd_letra_n * 100 / qtd_letras_texto))
print('o = {:.2f} %'.format(qtd_letra_o * 100 / qtd_letras_texto))
print('p = {:.2f} %'.format(qtd_letra_p * 100 / qtd_letras_texto))
print('q = {:.2f} %'.format(qtd_letra_q * 100 / qtd_letras_texto))
print('r = {:.2f} %'.format(qtd_letra_r * 100 / qtd_letras_texto))
print('s = {:.2f} %'.format(qtd_letra_s * 100 / qtd_letras_texto))
print('t = {:.2f} %'.format(qtd_letra_t * 100 / qtd_letras_texto))
print('u = {:.2f} %'.format(qtd_letra_u * 100 / qtd_letras_texto))
print('v = {:.2f} %'.format(qtd_letra_v * 100 / qtd_letras_texto))
print('x = {:.2f} %'.format(qtd_letra_w * 100 / qtd_letras_texto))
print('w = {:.2f} %'.format(qtd_letra_x * 100 / qtd_letras_texto))
print('y = {:.2f} %'.format(qtd_letra_y * 100 / qtd_letras_texto))
print('z = {:.2f} %'.format(qtd_letra_z * 100 / qtd_letras_texto))

tam_palavras = len(palavras)
tam_palavras = int(tam_palavras)
p_maior3 = []
for j in range(tam_palavras):
    if len(palavras[j]) > 3:
        p_maior3.append(palavras[j])
for y in range (len(p_maior3)):
    palavra_teste = p_maior3[y]
    qtd = p_maior3.count(palavra_teste)
    
palv_mais = ''
qtd_mais = 0
for y in range (len(p_maior3)):
    palavra_teste = p_maior3[y]
    qtd = p_maior3.count(palavra_teste)
    if qtd > qtd_mais:
        qtd_mais = qtd
        palv_mais = p_maior3[y]    
print(palv_mais)

if qtd_letra_a > qtd_letra_e > qtd_letra_o > qtd_letra_i:
    print('Português')
if qtd_letra_e  > qtd_letra_t  > qtd_letra_a > qtd_letra_i:
    print('Inglês')
if qtd_letra_e  > qtd_letra_a > qtd_letra_i > qtd_letra_t:
    print('Italiano')