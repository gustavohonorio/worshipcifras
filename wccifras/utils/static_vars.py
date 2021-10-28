class VarsCifraForm:
    # tom
    tom_choices = (
        ('0', 'Selecionar tom'),
        ('A', 'A'),
        ('Bb', 'Bb'),
        ('B', 'B'),
        ('C', 'C'),
        ('Db', 'Db'),
        ('D', 'D'),
        ('Eb', 'Eb'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('Ab', 'Ab'),
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

