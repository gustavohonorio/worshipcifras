from django.utils.safestring import mark_safe

escalas = {
    'C': '1',
    'C#': '2',
    'D': '3',
    'D#': '4',
    'E': '5',
    'F': '6',
    'F#': '7',
    'G': '8',
    'G#': '9',
    'A': '10',
    'A#': '11',
    'B': '12',
}

acordes_c = [
    'C',
    'Cm',
    'C6',
    'C7',
    'C9',
    'Cm6',
    'Cm7',
    'Cmaj7',
    'Cdim',
    'C+',
    'Csus',
    'C#m',
    'C#m6',
    'C#m7',
    'C#dim',
    'C/E',
]
acordes_d = [
    'D',
    'Db',
    'Dbmaj7',
    'Db+',
    'Dbsus',
    'Dm',
    'D6',
    'D7',
    'D9',
    'Dm6',
    'Dm7',
    'Dmaj7',
    'Ddim',
    'D+',
    'Dsus',
    'Db6',
    'Db7',
    'Db9',
    'D/F#',

]
acordes_e = [
    'E',
    'Em',
    'E5',
    'E6',
    'E7',
    'E9',
    'Em6',
    'Em7',
    'Emaj7',
    'Edim',
    'E+',
    'Esus',
    'Eb',
    'Ebm',
    'Eb6',
    'Eb7',
    'Eb9',
    'Ebm6',
    'Ebm7',
    'Ebmaj7',
    'Ebdim',
    'Eb+',
    'Ebsus',
]
acordes_f = [
    'F',
    'Fm',
    'F6',
    'F7',
    'F9',
    'Fm6',
    'Fm7',
    'Fmaj7',
    'Fdim',
    'F+',
    'Fsus',
    'F#',
    'F#m',
    'F#7',
    'F#9',
    'F#m6',
    'F#m7',
    'F#dim',
]
acordes_g = [
    'G',
    'Gm',
    'G6',
    'G7',
    'G9',
    'Gm6',
    'Gm7',
    'Gmaj7',
    'Gdim',
    'G+',
    'Gsus',
    'G#m',
    'G#m6',
    'G#m7',
    'G#dim',
    'Gb6',
    'Gbmaj7',
    'Gb+',
    'Gbsus',
    'G/B',
]
acordes_a = [
    'Ab',
    'Ab6',
    'Ab7',
    'Ab9',
    'Abmaj7',
    'Abmaj7',
    'Ab+',
    'Absus',
    'A',
    'Am',
    'A6',
    'A7',
    'A9',
    'Am6',
    'Am7',
    'Amaj7',
    'Adim',
    'A+',
    'Asus',
    'Am7/G',
    'A5(9)',
]
acordes_b = [
    'Bb',
    'Bbm',
    'Bb6',
    'Bb7',
    'Bb9',
    'Bbm6',
    'Bbm7',
    'Bbmaj7',
    'Bbdim',
    'Bb+',
    'Bbsus',
    'B',
    'Bm',
    'B6',
    'B7',
    'B9',
    'Bm6',
    'Bm7',
    'Bmaj7',
    'Bdim',
    'B+',
    'Bsus',
]

acordes = (acordes_c + acordes_d + acordes_e + acordes_f + acordes_g + acordes_a + acordes_b)


# TRANSPOSIÇÃO DE TONS
def transposicao_cifra(cifra, tonalidade_original, tonalidade_escolhida):
    # print(tonalidade_original + ' >>>> ' + tonalidade_escolhida)

    tonalidade_original = retorna_indice_escala(tonalidade_original)
    tonalidade_escolhida = retorna_indice_escala(tonalidade_escolhida)

    # print(tonalidade_original + ' >>>> ' + tonalidade_escolhida)

    semitons = retorna_semitons(tonalidade_original, tonalidade_escolhida)

    # print(semitons)

    for i, item in enumerate(cifra):
        if '$' in item:
            aux_indice = retorna_indice_escala(item[0:1])
            novo_acorde = retorna_indice_escala_acordes(int(aux_indice), semitons)
            novo_acorde = retorna_acorde_escala(novo_acorde)
            cifra[i] = item.replace(item[0:1], str(novo_acorde))


def retorna_indice_escala_acordes(indice, semitons):
    aux = indice + semitons

    if 0 < aux < 13:
        return aux
    elif aux > 12:
        return aux - 12
    else:
        return 12 + aux


def retorna_indice_escala(acorde):
    for chave in escalas.keys():
        if chave == acorde:
            acorde = escalas[chave]
            break
    return acorde


def retorna_acorde_escala(indice):
    for acorde, i in escalas.items():
        if i == str(indice):
            return acorde


def retorna_semitons(indice1, indice2):
    semitom = 0
    if indice1 > indice2:
        semitom = int(indice2) - int(indice1)
    else:
        semitom = int(indice1) - int(indice2)

    return semitom


# ESTE MÉTODO IRÁ PERSISTIR A CIFRA E ATRIBUIR AS TAGS HTML PARA EXIBIÇÃO EM TELA
# REGRAS #
# -> @@ = Pular linha no final
# -> $ = Se o index+1 não conter '$', pular linha no final
# -> @[ = Pular linha no inicio
# -> ]@ = Pular linha no final
# -> Outros = Se index-1 conter $ ou @, pular linha no final
def formatar_cifra(cifra):
    for i, valor in enumerate(cifra):
        if '@@' in valor:
            cifra[i] = add_tags('strong', valor.replace('@@', ''), 0)
            continue

        if '@[' in valor:
            cifra[i] = add_tags('strong', valor.replace('@', ''), 1)
            continue

        if ']@' in valor:
            cifra[i] = add_tags('strong', valor.replace('@', ''), 2)
            continue

        if '$' in valor:
            go = (i + 1 < len(cifra))
            if go and '$' in cifra[i + 1]:
                cifra[i] = add_tags('strong', valor.replace('$', ''), 3)
            else:
                cifra[i] = add_tags('strong', valor.replace('$', ''), 2)
            continue

        go = (i + 1 < len(cifra))
        if go and '$' in cifra[i + 1]:
            cifra[i] = add_tags('nA', valor, 4)

        if go and '@' in cifra[i + 1]:
            cifra[i] = add_tags('nA', valor, 4)

    return cifra


# MODO DE VISUALIZAÇÃO SOMENTE DA LETRA
def formatar_letra(cifra):
    formatar_cifra(cifra)

    cifra = [valor for valor in cifra if not 'strong' in valor or '[' in valor or ']' in valor]

    return cifra


# ESTE METODO É USADO NO STAFF PARA ADICIONAR OS ESCAPES DAS CIFRAS
def tag_cifra(cifra):
    for i, valor in enumerate(cifra):
        if '[' in valor and ']' in valor and not '@' in valor:
            cifra[i] = cifra[i] + '@@'
            continue

        if '[' in valor and not '@' in valor:
            cifra[i] = '@' + cifra[i]
            continue

        if ']' in valor and not '@' in valor:
            cifra[i] = cifra[i] + '@'
            continue

        for a in acordes:
            if valor == a:
                cifra[i] = cifra[i] + '$'
                break

    return cifra


# ESTE METODO INSERE AS TAGS HTML PARA EXIBIÇÃO EM TELA
def add_tags(tag, valor, pular_linha):
    # print(f'{valor} >>>>>>> {pular_linha}')
    if pular_linha == 0:
        return mark_safe(f'<br><%s>%s</%s><br>' % (tag, valor, tag))
    elif pular_linha == 1:
        return mark_safe(f'<br><%s>%s</%s>' % (tag, valor, tag))
    elif pular_linha == 2:
        return mark_safe(f'<a><%s>%s</%s></a><br>' % (tag, valor, tag))
    elif pular_linha == 3:
        return mark_safe(f'<a><%s>%s</%s></a>' % (tag, valor, tag))
    elif pular_linha == 4:
        return mark_safe(f'%s<br>' % valor)
