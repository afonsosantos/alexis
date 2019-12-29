# Alexis

Alexis é uma pequena aplicação criada em Python com o intuito de demonstrar as funcionalidades da biblioteca `speechrecognition`.

## Funcionalidades

- Responde a comandos de voz simples, como
    - `nome` - O meu nome é Alexis
    - `data` - Devolve a data e hora do sistema através da biblioteca `time`
    - `pesquisar` - Pergunta o que queremos pesquisar e abre o Google no navegador de Internet padrão do sistema
    - `localização` - Pergunta qual a localização e abre o Google Maps com a localização pesquisada
    - `sair` - Termina a execução do programa

## Uso

```
python main.py
```

## Bibliotecas

### Nativas:

- os
- random
- time
- webbrowser

### Disponíveis no PyPi:

- playsound
- speech_recognition
- gtts

## Contribuição

Novas funcionalidades são bem-vindas! Antes de qualquer alteração, abra uma [Questão (_Issue_)](https://github.com/afonsosantos/alexis/issues) para discutirmos o problema e as possíveis soluções.

## Licença

[Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)

## Agradecimentos

- [Traversy Media](https://www.youtube.com/user/TechGuyWeb) por fazer o vídeo ["Build A Python Speech Assistant App"](https://www.youtube.com/watch?v=x8xjj6cR9Nc), que inspirou a criação da Alexis.