class VarsCifraForm:
    # tom
    tom_choices = (
        ('0', 'Selecionar tom'),
        ('1', 'A'),
        ('2', 'Bb'),
        ('3', 'B'),
        ('4', 'C'),
        ('5', 'Dd'),
        ('6', 'D'),
        ('7', 'Eb'),
        ('8', 'E'),
        ('9', 'F'),
        ('10', 'G'),
        ('11', 'Ab'),
    )
    # capotraste
    capotraste_choices = (
        ('0', 'Sem capotraste'),
        ('1', '1º Casa'),
        ('2', '2º Casa'),
        ('3', '3º Casa'),
        ('4', '4º Casa'),
        ('5', '5º Casa'),
    )
    # afinacao
    afinacao_choices = (
        ('0', 'Afinação'),
        ('1', 'E A D G B E'),
        ('2', 'Eb Ab Db Gb Bb Eb'),
        ('3', 'D G C F A D'),
        ('4', 'Db Gb Cb Fb Ab Db'),
        ('5', 'C F Bb Eb G C'),
    )
    # versao
    versao_choices = (
        ('0', 'Versão'),
        ('1', 'Ao vivo'),
        ('2', 'Completa'),
        ('3', 'Simplificada'),
        ('4', 'Acústico'),
        ('5', 'Padrão'),
    )
    # genero
    genero_choices = (
        ('0', 'Gênero principal'),
        ('1', 'Worship'),
        ('2', 'Clássicos'),
        ('3', 'Poprock'),
        ('4', 'Rock'),
        ('5', 'Reggae'),
    )

