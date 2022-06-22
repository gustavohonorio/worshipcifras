class VarsCifraForm:
    # tom
    tom_choices = (
        ('0', 'Selecionar tom'),
        # maiores
        ('C', 'C'),
        ('Db', 'Db'),
        ('D', 'D'),
        ('Eb', 'Eb'),
        ('E', 'E'),
        ('F', 'F'),
        ('F#', 'F#'),
        ('G', 'G'),
        ('Ab', 'Ab'),
        ('A', 'A'),
        ('Bb', 'Bb'),
        ('B', 'B'),
        # menores
        ('Cm', 'Cm'),
        ('C#m', 'C#m'),
        ('Dm', 'Dm'),
        ('Ebm', 'Ebm'),
        ('Em', 'Em'),
        ('Fm', 'Fm'),
        ('F#m', 'F#m'),
        ('Gm', 'Gm'),
        ('G#m', 'G#m'),
        ('Am', 'Am'),
        ('Bbm', 'Bbm'),
        ('Bm', 'Bm'),
    )
    # capotraste
    capotraste_choices = (
        ('0', 'Sem capotraste'),
        ('1º Casa', '1º Casa'),
        ('2º Casa', '2º Casa'),
        ('3º Casa', '3º Casa'),
        ('4º Casa', '4º Casa'),
        ('5º Casa', '5º Casa'),
    )
    # afinacao
    afinacao_choices = (
        ('0', 'Afinação'),
        ('E A D G B E', 'E A D G B E'),
        ('Eb Ab Db Gb Bb Eb', 'Eb Ab Db Gb Bb Eb'),
        ('D G C F A D', 'D G C F A D'),
        ('Db Gb Cb Fb Ab Db', 'Db Gb Cb Fb Ab Db'),
        ('C F Bb Eb G C', 'C F Bb Eb G C'),
    )
    # versao
    versao_choices = (
        ('0', 'Versão'),
        ('Ao vivo', 'Ao vivo'),
        ('Completa', 'Completa'),
        ('Simplificada', 'Simplificada'),
        ('Acústico', 'Acústico'),
        ('Padrão', 'Padrão'),
    )

    # genero
    genero_choices = (
        ('0', 'Gênero principal'),
        ('Worship', 'Worship'),
        ('Clássicos', 'Clássicos'),
        ('Poprock', 'Poprock'),
        ('Rock', 'Rock'),
        ('Reggae', 'Reggae'),
    )

    # status
    status_choices = (
        ('P', 'Pendente de aprovação'),
        ('A', 'Ativa'),
        ('AV', 'Ativa e Verificada'),
        ('AP', 'Ativa e Patrocinada'),
        ('E', 'Excluida'),
        ('R', 'Reprovada'),
    )
    # patrocinada
    patrocinada_choices = (
        ('True', 'Sim'),
        ('False', 'Não'),
    )


class Vars:
    # modo visualização
    modo_choices = ('Cifra', 'Letra')
