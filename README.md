# Projeto UFF Chronos

Recebe um dataset padronizado, e retorna uma lista impressa no terminal com os CRs dos alunos e dos cursos, ordenadamente.

## Forma de usar

### Invocando o Python
Invoque o python e passe o Main do programa e o caminho do dataset como parametros:

```
$ python3 Main_cli.py /caminho/do/dataset.csv
```
### Como script Linux
Mude o tipo de arquivo para executavel (apenas uma vez):

```
$ chmod +x Main_cli.py
```

Então execute o arquivo e passe o dataset como argumento:
```
$ ./Main_cli.py /caminho/do/dataset.csv
```
> O shebang deste aquivo é `#! /usr/bin/env python3`, mas pode ser alterado para seu SO caso o PATH para o python aponte para outro lugar como `/usr/bin/python`.

## Extensibilidade

Este programa lê um arquivo do tipo csv, mas pode facilmente ser adaptado para outro formato de entrada. Basta criar uma outra classe de conversão com uma função com a assinatura ` def get_dict_dados(self, caminho: str) -> None:` e substituir a chamada `controle_csv = ControleCsv()` por `controle_csv = MeConversorCsv()`.

> Lembrando que em Python não existem interfaces, os contratos são controlados pelo usuário.

## Testes

Todos os testes são automatizados, bastando executar o arquivo `tests_main.py`.

## Ambiente

Foi usado no desenvolvimento a versão 3.8 do Python, mas rodará em outras versões, preferencialmente acima da 3.5.x.

Está incluso no projeto uma pasta devcontainer do Visual Studio Code. Caso queira também usar o mesmo ambiente conteinerizado de produção (Python 3.8, Node 10, extensões, linter, instalação automática de `requirements.txt`) você precisará do Docker instalado, além de possivelmente seu usuário como parte do grupo `docker`, a depender do SO/ SELinux.

## Licença

Uso aqui a licença MIT. Você pode copiar, modificar e inclusive vender, mas te agradeço se você der os créditos.