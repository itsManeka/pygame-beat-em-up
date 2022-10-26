class GameConfig(object):

    TIPO_ANIMACAO_ATINGIDO = 1
    TIPO_ANIMACAO_DORMINDO = 2 

    TIPO_ITEM_VIDA      = 1
    TIPO_ITEM_PROJETIL  = 2

    TIPO_INIMIGO_DRAGAO_ZUMBI       = 1
    TIPO_INIMIGO_DRAGAO_MORFEU      = 2
    TIPO_INIMIGO_DRAGAO_TARTARUGA   = 3
    TIPO_INIMIGO_MINI_DRAGAO        = 4
    TIPO_INIMIGO_DRAGAO_AQUATICO    = 5

    ATAQUE_NORMAL   = 1
    ATAQUE_FORTE    = 2
    ATAQUE_ESPECIAL = 3
    ATAQUE_PROJETIL = 4

    WIDTH = 800
    HEIGHT = 600
    CENTER = 300

    MARGIN_RIGHT = 700
    MARGIN_LEFT = 100

    DIR_LEVEL = "estagio/levels/"
    DIR_BACKGROUND = "img/background/"
    DIR_PERSONAGENS = "img/personagens/"
    DIR_ANIMACOES = "img/animacoes/"
    DIR_PROJETEIS = "img/projeteis/"
    DIR_ARQUIVO_PONTUACAO = "pontuacao.txt"

    ARQUIVO_READ = 'r'
    ARQUIVO_WRITE = 'w'

    IMAGE_TYPE = ".png"

    OUT_MENU            = "menu"
    OUT_QUIT            = "quit"
    OUT_CONTINUE        = "continue"
    OUT_GAME_OVER       = "game-over"
    OUT_END_ARCADE      = "end-arcade"
    OUT_PROXIMO_LEVEL   = "next-level"

    FULLSCREEN = False
