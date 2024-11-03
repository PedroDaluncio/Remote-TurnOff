Remote Turn-OFF

Esse projeto foi feito em Flask com o objetivo de desligar o computador diretamente pelo celular usando chamadas de API.
Ao ser executado, ele cria um servidor em Flask que espera o usuário clicar no botão "Desligar Computador".
Ao clicar, ele inicia o processo de desligar o computador através de uma chamada de API, utilizando a biblioteca subprocess.

-----------------------------------------------------------------------------------------------------

## Instalação

Para instalar o projeto, siga os passos abaixo:

```bash
git clone https://github.com/PedroDaluncio/Remote-TurnOff.git
cd local/do/projeto
pip install -r requirements.txt
flask --app servidor run --host=0.0.0.0

-----------------------------------------------------------------------------------------------------

Configurações de IP e Porta

IP: Por padrão, o projeto usa 0.0.0.0, o que permite que o computador esteja acessível a toda a rede na qual está conectado.
Para usar um IP específico, basta substituir 0.0.0.0 pelo IP desejado.

Porta: Por padrão, o projeto usa a porta 5000, mas pode ser utilizada qualquer porta livre. Basta substituir 5000 pela porta desejada.

-----------------------------------------------------------------------------------------------------
Inicialização Automática

Para iniciar o projeto sempre que o computador for ligado, siga os passos abaixo:

    1.Dê o comando: pyinstaller --add-data "templates:templates" --add-data "static:static" --onefile --windowed  servidor.py
    Explicação: Esse comando transforma o script em um executável sem console, mas que funciona normalmente, mantendo tanto o HTML quanto o CSS.

    2.Abra a pasta de inicialização do sistema operacional(windows: shell:startup)

    3.Coloque o executável nessa pasta. Dessa forma, sempre que o computador ligar, o executável será iniciado,
    e basta acessar o IP e a porta alocada para desligar o computador ao apertar o botão.

-----------------------------------------------------------------------------------------------------
Observações Finais

    - Certifique-se de que as permissões de firewall estejam configuradas para permitir o acesso ao servidor Flask.
    - O projeto foi testado em ambientes Windows; resultados em outros sistemas operacionais podem variar.