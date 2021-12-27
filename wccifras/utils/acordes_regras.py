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

acordes = [
    'Ab',
    'G#m',
    'Ab6',
    'Ab7',
    'Ab9',
    'G#m6',
    'G#m7',
    'Abmaj7',
    'G#dim',
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
    'Db',
    'C#m',
    'Db6',
    'Db7',
    'Db9',
    'C#m6',
    'C#m7',
    'Dbmaj7',
    'C#dim',
    'Db+',
    'Dbsus',
    'D',
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
    'Gb6',
    'F#7',
    'F#9',
    'F#m6',
    'F#m7',
    'Gbmaj7',
    'F#dim',
    'Gb+',
    'Gbsus',
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
    ###
    'G/B',
    'D/F#',
    'C/E',
    'Am7/G',
    'A5(9)',
]


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
        semitom = int(indice2)-int(indice1)
    else:
        semitom = int(indice1)-int(indice2)

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
    print(f'{valor} >>>>>>> {pular_linha}')
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
