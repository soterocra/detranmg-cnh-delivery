# detranmg-cnh-delivery
> Acompanhe a entrega da sua CNH no Detran MG utilizando Python, Selenium e Telegram

Quem não fica ancioso para receber sua carteira de motorista? Ainda mais quando é a primeira!

Com poucos cliques e configurações você vai começar a receber um print da tela do Detran MG informando o status da entrega da sua habilitação.

## Instalação

Primeiro faça o download e instale o Python 3.7 ou superior. [Clique aqui](https://www.python.org/downloads).

Em seguida, execute o seguinte comando na pasta do projeto:

Windows:

```sh
pip install -r requirements.txt
```

## Exemplo de uso

Alguns exemplos interessantes e úteis sobre como seu projeto pode ser utilizado. Adicione blocos de códigos e, se necessário, screenshots.


## Configuração para Desenvolvimento

1. Crie seu bot no telegram para obter o token de autenticação. Para isso siga [esses passos](https://core.telegram.org/bots#6-botfather).
2. Com o token em mãos substitua essa parte do código:
```python

# ...

class TelegramBOT:
    
    TOKEN_BOT = 'SEU_TOKEN_AQUI'
    
    def __init__(self):

# ...

```
3. Substitua agora essa outra parte do código pelo seu **CPF e Data de Nascimento**.
```python
    
# ...

    CPF_TEXT = "12345678910"
    BIRTH_DATE_TEXT = "01/01/1991"

# ...
    
```
4. Dê um Oi para seu Bot no Telegram, quando mandarmos executar o código ele vai enviar o status da CNH para todos que deram um "Alô" a ele recentemente.
5. Finalmente execute via termina o comando `python App.py` para começar a receber o status.

Ps: O status vai ser enviado imediatamente e em seguida de hora em hora, isso pode ser alterado facilmente no código.

## Histórico de lançamentos

* 0.0.1
    * Versão inicial

## Meta

Rafael Sotero Rocha – [@soterocra](https://twitter.com/soterocra)

## Contributing

1. Faça o _fork_ do projeto (<https://github.com/soterocra/detranmg-cnh-delivery/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_
