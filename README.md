# Pygame Beat'em Up 🥊🐉

Um jogo de luta estilo beat'em up desenvolvido em Python usando Pygame. O jogador controla um templário spartano em aventuras épicas enfrentando diferentes tipos de dragões em diversos cenários.

## 🎮 Sobre o Jogo

Este é um jogo 2D side-scrolling beat'em up onde o jogador deve derrotar inimigos enquanto percorre diferentes níveis. O jogo apresenta:

- **Personagem Principal**: Templário Spartano
- **Inimigos**: Diversos tipos de dragões (Zumbi, Morfeu, Tartaruga, Aquático, Mini-Dragão)
- **Múltiplos Níveis**: Calabouço, Lago, Selva, Rua e outros cenários
- **Sistema de Combate**: Ataques normais, fortes e projéteis
- **Modos de Jogo**: Arcade e Survival

## 🎯 Funcionalidades

### Controles
- **Movimento**: Setas direcionais ou HJKL (estilo vi)
- **Ataque Normal**: Z
- **Projétil**: X
- **Pause**: ESC
- **Suporte a Controle**: Joystick/Gamepad

### Sistema de Jogo
- **Health Points (HP)**: Sistema de vida do jogador
- **Múltiplos tipos de ataque**: Normal, forte, especial e projétil
- **Scroll horizontal**: Cenários que se movem conforme o jogador avança
- **Sistema de estados**: Menu, jogo, pause, game over
- **Animações**: Sprites animados para personagens e efeitos

## 🏗️ Arquitetura do Projeto

### Estrutura de Diretórios

```
pygame-beat-em-up/
├── main.py                 # Ponto de entrada do jogo
├── Game.py                 # Classe principal do jogo
├── GameConfig.py           # Configurações globais
├── Objeto.py               # Classe base para objetos do jogo
├── animacoes/              # Sistema de animações
│   ├── Animacao.py        # Classe base para animações
│   ├── AnimacaoPronta.py  # Animações predefinidas
│   └── [outros]           # Barril, Comida, Espada, Fumaca, etc.
├── controles/              # Sistema de controles
│   └── Controle.py        # Gerenciamento de input
├── criaturas/              # Personagens e criaturas
│   ├── Criatura.py        # Classe base para todas as criaturas
│   ├── Jogador.py         # Classe do jogador
│   ├── Inimigo.py         # Classe base para inimigos
│   └── [dragões]          # DragaoZumbi, DragaoMorfeu, etc.
├── estados/                # Estados do jogo (State Pattern)
│   ├── Estado.py          # Gerenciador de estados
│   ├── MenuEstado.py      # Estado do menu principal
│   ├── ArcadeEstado.py    # Estado do modo arcade
│   ├── SurvivalEstado.py  # Estado do modo survival
│   └── [outros]           # GameOver, MenuPause, etc.
├── estagio/                # Sistema de níveis
│   ├── Estagio.py         # Classe para gerenciar estágios
│   └── levels/            # Arquivos de configuração dos níveis
├── img/                    # Recursos gráficos
│   ├── background/        # Imagens de fundo
│   ├── personagens/       # Sprites dos personagens
│   ├── animacoes/         # Sprites de animações
│   └── [outros]           # icon, misc, projeteis
├── menu/                   # Sistema de menus
├── projetil/              # Sistema de projéteis
└── doc/                   # Documentação
    └── padroes.txt        # Padrões de código
```

### Padrões de Design Utilizados

1. **State Pattern**: Gerenciamento de estados do jogo (menu, jogo, pause, etc.)
2. **Sprite Pattern**: Uso do sistema de sprites do Pygame
3. **Factory Pattern**: Criação de diferentes tipos de dragões
4. **Observer Pattern**: Sistema de eventos e atualizações

## 🚀 Como Executar

### Pré-requisitos

- Python 3.6+
- Pygame 1.9.2+

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/itsManeka/pygame-beat-em-up.git
cd pygame-beat-em-up
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o jogo:
```bash
python main.py
```

## 🎮 Como Jogar

1. **Menu Principal**: Use as setas para navegar e Enter para selecionar
2. **Movimento**: Use as setas direcionais para mover o personagem
3. **Combate**: 
   - Pressione Z para atacar
   - Pressione X para lançar projéteis (espada)
4. **Pause**: Pressione ESC para pausar o jogo
5. **Objetivo**: Derrote todos os inimigos e avance pelos níveis

### Modos de Jogo

- **Arcade**: Percorra níveis sequenciais com dificuldade progressiva
- **Survival**: Enfrente ondas infinitas de inimigos

## 🔧 Configuração

O arquivo `GameConfig.py` contém todas as configurações principais:

- **Resolução**: 800x600 pixels
- **FPS**: 60 (configurável)
- **Tipos de inimigos e ataques**: Constantes predefinidas
- **Diretórios de recursos**: Caminhos para imagens e arquivos

## 📝 Padrões de Código

O projeto segue padrões específicos documentados em `doc/padroes.txt`:

- **Notação Húngara**: Para tipagem de variáveis
- **CamelCase**: Para métodos e variáveis
- **PascalCase**: Para classes
- **Idioma**: Português/Inglês misto
- **Constantes**: MAIÚSCULAS

## 🎨 Assets

O jogo inclui:
- **Sprites animados** para todos os personagens
- **Backgrounds** temáticos para cada nível
- **Efeitos visuais** (explosões, fumaça, etc.)
- **Fonte customizada** (Coder's Crux) licenciada sob Creative Commons

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## 🐛 Problemas Conhecidos

- O jogo foi desenvolvido para Python 2.7 e pode precisar de ajustes para versões mais recentes
- Alguns sprites podem ter problemas de transparência em sistemas específicos

## 🧑‍💻 Autor

- **Emanuel Ozorio Dias**

---

**Divirta-se jogando!** 🎮✨
