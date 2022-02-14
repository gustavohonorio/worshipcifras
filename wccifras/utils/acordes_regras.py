from django.utils.safestring import mark_safe

escalas = {
    # maiores
    'C': '1',
    'Db': '2',
    'D': '3',
    'Eb': '4',
    'E': '5',
    'F': '6',
    'F#': '7',
    'G': '8',
    'Ab': '9',
    'A': '10',
    'Bb': '11',
    'B': '12',
    # menores
    'Cm': '1',
    'C#m': '2',
    'Dm': '3',
    'Ebm': '4',
    'Em': '5',
    'Fm': '6',
    'F#m': '7',
    'Gm': '8',
    'G#m': '9',
    'Am': '10',
    'Bbm': '11',
    'Bm': '12',
}

escalas_maiores = (
    'C',
    'Db',
    'D',
    'Eb',
    'E',
    'F',
    'F#',
    'G',
    'Ab',
    'A',
    'Bb',
    'B',
)

escalas_menores = (
    'Cm',
    'C#m',
    'Dm',
    'Ebm',
    'Em',
    'Fm',
    'F#m',
    'Gm',
    'G#m',
    'Am',
    'Bbm',
    'Bm',
)

# TODO : LIMPAR AS DUPLICATAS DOS ACORDES PARA OTIMIZAR (UM TICO rs) A APPS
acordes_c = [
    'C',
    'C5',
    'C6',
    'C7',
    'C9',
    'C11',
    'C13',
    'Cm',
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
    'C',
    'C/E',
    'C/G',
    'C/D',
    'C/F',
    'C7M',
    'C7M/E',
    'C7M/G',
    'C/B',
    'C7M(5)',
    'C7',
    'C7/E',
    'C7/G',
    'C/Bb',
    'C7/F',
    'Cm',
    'Cm/Eb',
    'Cm/G',
    'Cm/A',
    'Cm7',
    'Cm7/Eb',
    'Cm7/G',
    'Cm7/Bb',
    'Cm7/F',
    'C4',
    'C°',
    'C5',
    'C6',
    'C(7/4)',
    'C(7/4)(-9)',
    'Cadd9',
    'Cadd9/G',
    'C(-9/7)',
    'C(9/7)',
    'C13',
    'Cm(-5)',
    'Cm6',
    'Cm7M',
    'Cm(7/-5)',
    'C#',
    'C#/E#',
    'C#/G#',
    'C#/D#',

]
acordes_d = [
    'D',
    'Db',
    'Dbmaj7',
    'Db+',
    'Dbsus',
    'Dm',
    'D5',
    'D6',
    'D6(9)',
    'D7',
    'D9',
    'D11',
    'D13',
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
    'D4',
    'D°',
    'D5',
    'D6',
    'D(7/4)',
    'D(7/4)/A',
    'D(-7/5)',
    'D(7/5)',
    'Daad9',
    'D-(9/7)',
    'D(9/7)',
    'D(-13/7)',
    'Dm-5',
    'Dm6',
    'Dm7M',
    'Dm(-7/5)',
    'Dmadd9',
    'Dm-5/C',
    'Dm-5/Eb',
    'Dm/B',
    'Db4',
    'Db°',
    'Db5',
    'Db6',
    'Db(7/4)',
    'Dbm-5',
    'Dbm(-7/5)',
    'D9/A',

]
acordes_e = [
    'E',
    'Em',
    'E5',
    'E6',
    'E7',
    'E9',
    'E11',
    'E13',
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
    'E/G#',
    'E/G#',
    'E/B',
    'E/F#',
    'E/A',
    'E7M',
    'E/D#',
    'E/C',
    'E7',
    'E7/G#',
    'E7/B',
    'E/D',
    'E7/A',
    'Em',
    'Em/G',
    'Em/B',
    'Em/F#',
    'Em/A',
    'Em7',
    'Em7/G',
    'Em7/B',
    'Em/D',
    'Em7/A',
    'E°',
    'E5',
    'E6',
    'E(7/4)',
    'E(+7/5)',
    'E-(9/7)',
    'E(9/7)',
    'E13',
    'Em-5',
    'Em6',
    'Emadd9',
    'Em(-7/5)',
    'Em(9/7)',
    'Em-5/F',
    'Em/D#',
    'Em/Eb',
    'Em(-7/5)/A',
    'Em/C#',
    'Eb4',
    'Eb°',
    'Eb5',
    'Eb6',
    'Eb(7/4)',
    'Eb(7/6)/Bb',
    'Eb(-7/5)',
    'Eb(9/7)',
    'Ebm-5',
    'Ebm6',
    'Ebm7M',
    'Ebm(-7/5)',

]
acordes_f = [
    'F',
    'Fm',
    'F5',
    'F6',
    'F7',
    'F9',
    'F11',
    'F13',
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
    'F#m7(11)/C#',
    'F#dim',
    'F4',
    'F°',
    'F5',
    'F6',
    'F(7/4)',
    'F(+7/5)',
    'Fadd9',
    'F(9/7)/C',
    'F(13/7)',
    'Fadd9A',
    'Fm-5',
    'Fm6',
    'Fm7M',
    'Fm(-7/5)',
    'F/A',
    'F/C',
    'F/G',
    'F7M',
    'F7M/A',
    'F7M/C',
    'F/E',
    'F7',
    'F7/A',
    'F7/C',
    'F/Eb',
    'F7/Bb',
    'Fm',
    'Fm/Ab',
    'Fm/C',
    'Fm/G',
    'Fm7',
    'Fm/Fb',
    'Fm7/Rb',
    'Fm/D',
    'F#',
    'F#/A#',
    'F#/C#',
    'F#/G#',
    'F#7M',
    'F#7',
    'F#/E',
    'F#M',
    'F#m/A',
    'F#m/C',
    'F#m/D#',
    'F#m7',
    'F#m7/A',
    'F#m/E',
    'F#m7/B',
    'F#4',
    'F#°',
    'F#6',
    'F#(7/4)',
    'F#(-7/5)',
    'F#(+7/5)',
    'F#(-9/7)',
    'F#m-5',
    'F#m(-7/5)',
    'F#m(-7/5)/B',
    'F#madd9',
    'F#m11',

]
acordes_g = [
    'G',
    'Gm',
    'G5',
    'G6',
    'G7',
    'G9',
    'G11',
    'G13',
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
    'G/B',
    'G/D',
    'G/A',
    'G/C',
    'G7M',
    'G7M/D',
    'G/F#',
    'G7M/A',
    'G7',
    'G7/B',
    'G7/D',
    'G/F',
    'G7/C',
    'Gm',
    'Gm/Bb',
    'Gm/D',
    'Gm/C',
    'Gm/E',
    'Gm7',
    'Gm7/Bb',
    'Gm7/D',
    'Gm/F',
    'Gm7/C',
    'G4',
    'G°',
    'G5',
    'G6',
    'G(7/4)',
    'G5',
    'G(+7/5)',
    'Gadd9',
    'G(-9/7)',
    'G(9/7)',
    'G(-13/7)',
    'Gm-5',
    'Gm6',
    'Gm7M',
    'Gm(-7/5)',
    'Gm(9/7)',
    'Gm(-7/5)/C',
    'Gb4',
    'Gb°',
    'Gb6',
    'Gb(7/4)',
    'Gb(-7/5)',
    'Gb(+7/5)',
    'Gb(-9/7)',
    'Gbm-5',
    'Gbm(-7/5)',
    'Gbm(-7/5)Cb',
    'Gbmadd9',
    'Gb',
    'Gb/Bb',
    'Gb/Dd',
    'Gb7M',
    'Gb7',
    'Gb/Fb',
    'Gbm',
    'Gbm/Bbb',
    'Gbm/Db',
    'Gbm/Eb',
    'Gbm7',
    'Gbm7/Bbb',
    'Gbm/Fb',
    'Gbm7/Cb',
    'Gb4',
    'Gb°',
    'Gb(7/4)',
    'Gb(-7/5)',
    'Gb(+7/5)',
    'Gb(-9/7)',
    'Gbm-5',
    'Gbm-(7/5)',
    'Gbm(-7/5)/Cb',
    'Gbmadd9',
    'G9/D',

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
    'A4',
    'A4(7/9)',
    'A5',
    'A6',
    'A7',
    'A9',
    'A11',
    'A13',
    'Am6',
    'Am7',
    'Amaj7',
    'Adim',
    'A+',
    'Asus',
    'Am7/G',
    'A5(9)',
    'A/C#',
    'A/E',
    'A/B',
    'A/D',
    'A7M',
    'A/G#',
    'A7',
    'A7/C#',
    'A7/E',
    'A/G',
    'A7/D',
    'Am',
    'Am/C',
    'Am/E',
    'Am/F#',
    'Am/D',
    'Am7',
    'Am/G',
    'Am7/D',
    'Ab4',
    'Ab°',
    'Ab5',
    'Ab6',
    'Ab(7/4)',
    'Ab(-7/5)',
    'Abadd9',
    'Ab(-9/7)',
    'Ab(9/7)',
    'Abm-5',
    'Abm6',
    'Abm(-7/5)',
    'Abm-5/Bbb',
    'Ab',
    'Ab/C',
    'Ab/Eb',
    'Ab/Bb',
    'Ab/Dd',
    'Ab7M',
    'Ab7M/C',
    'Ab/G',
    'Ab7M/Bb',
    'Ab7',
    'Ab/Gb',
    'Abm',
    'Abm/Cb',
    'Abm/Eb',
    'Abm7',
    'A4',
    'A°',
    'A5',
    'A6',
    'A(7/4)',
    'A(7/4)/E',
    'A(-7/5)',
    'Aadd9',
    'A(-9/7)',
    'A(9/7)',
    'A(-13/7)',
    'A13',
    'A(9/6)',
    'Am-5',
    'Am6',
    'Am(-7/5)',
    'Amadd9',
    'A(9/7)M',
    'A(+11)',
    'A5/C#',
    'A9/C#',

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
    'B5',
    'B6',
    'B7',
    'B9',
    'B11',
    'B13',
    'Bm',
    'Bm5',
    'Bm6',
    'Bm7',
    'Bm9',
    'Bm11',
    'Bmaj7',
    'Bdim',
    'B+',
    'Bsus',
    'B/D#',
    'B/F#',
    'B7M',
    'B7',
    'B/C#',
    'B7/D#',
    'B7/F#',
    'B/A',
    'B7/E',
    'Bm',
    'Bm/D',
    'Bm/F#',
    'Bm7',
    'Bm7/F#',
    'Bm/A',
    'Bm7/E',
    'Bb',
    'Bb/D',
    'Bb/F',
    'Bb/C',
    'Bb/Eb',
    'Bb7M',
    'Bb',
    'Bb/F',
    'Bb/A',
    'Bb7M/C',
    'Bb7',
    'Bb7/D',
    'Bb7/F',
    'Bb/Ab',
    'Bb7/Eb',
    'Bbm',
    'Bbm/Db',
    'Bbm/F',
    'Bbm/Eb',
    'Bbm7',
    'Bbm/ab',
    'Bbm7/Eb',
    'Bb4',
    'Bb°',
    'Bb5',
    'Bb6',
    'Bb(7/4)',
    'Bbadd9',
    'Bb(-9/7)',
    'Bb(9/7)',
    'Bb13',
    'Bbm-5',
    'Bbm6',
    'Bb(-7/5)',
    'Bb',
    'Bb/D',
    'Bb/F',
    'Bb/F',
    'Bb/Eb',
    'Bb7M',
    'Bb/F',
    'Bb/A',
    'Bb7M/C',
    'Bb7',
    'Bb7/D',
    'Bb7/F',
    'Bb/Ab',
    'Bb7/Eb',
    'Bbm',
    'Bbm/Db',
    'Bbm/F',
    'Bbm/Eb',
    'Bbm7',
    'Bbm/Ab',
    'Bbm7/Eb',

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
    semitom = int(indice2) - int(indice1)
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
