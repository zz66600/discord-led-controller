# discord-led-controller
Este projeto utiliza um bot do Discord para controlar um LED conectado a um Arduino. Quando comandos específicos são enviados via Discord, o bot interage com o Arduino para ligar ou desligar o LED. O projeto inclui integração com a biblioteca pySerial para comunicação com o Arduino e discord.py para a criação e gerenciamento do bot do Discord.

# Pré-requisitos e recursos utilizados
Os recursos utilizados neste projeto foram:


## Hardware
1.Arduino Nano (outras placas podem ser utilizadas, utilizadas as devidas adaptações)

2.Jumpers/cabos para fazer a conexão entre os componentes

3.Cabo para conectar o Arduino em um computador

4.LED ou buzzer

### Imagem do circuito com LED:

 ![image](https://github.com/user-attachments/assets/5514ced9-8fc3-4c34-aa95-1e0e853b2121)

ligação:

| Arduino       | LED/buzzer    |
| ------------- |:-------------:|
| 13            |       +       |
| GND           |       -       |

## Software

1.Arduino IDE 2.0 (para fazer upload do código para o Arduino)

2.Python (para integração com o Arduino e automação via Discord)

# Passo a passo

## Criar o Bot no Discord

Acesse o Discord Developer Portal:

[Discord Developer Portal](https://discord.com/developers/applications/)

Vá para Discord Developer Portal.
Criar uma Nova Aplicação:

![image](https://github.com/user-attachments/assets/78808825-ddc5-47f2-aa6a-eababfcd6259)


Clique em "New Application".
Dê um nome à sua aplicação (ex.: "ArduinoBot") e clique em "Create".
Adicionar o Bot:

![image](https://github.com/user-attachments/assets/9155d761-e5f6-4e26-a095-55b9ca72bf15)


No menu lateral, clique em "Bot".
Clique em "Add Bot" e confirme clicando em "Yes, do it!".
Configurar o Token do Bot:

Após criar o bot, anote o Token. Este token será usado no seu código Python para autenticar o bot.
### ⚠️Cuidado: Não compartilhe esse token com ninguém. Ele dá acesso total ao seu bot.

![image](https://github.com/user-attachments/assets/bbe92e60-451c-49e1-b3b8-b3798f5e910b)


Configurar as Intenções Privilegiadas:

Role para baixo até Privileged Gateway Intents e ative as opções de "PRESENCE INTENT" e "SERVER MEMBERS INTENT" se o seu bot precisar dessas funcionalidades.
Gerar o Link de Convite:

![image](https://github.com/user-attachments/assets/8786092d-ad8b-4622-a758-fb7120a4a1cc)


No menu lateral, clique em "OAuth2" e depois em "URL Generator".

Marque a opção "bot" em "SCOPES".

Marque as permissões desejadas para o bot (ex.: "Send Messages", "Read Messages", etc.).

Copie o link gerado e cole no navegador para adicionar o bot ao seu servidor.


# Configurar o Ambiente Python

Instalar o Python e Bibliotecas Necessárias:

Baixe e instale o Python 3.x 

[python](https://www.python.org/downloads/)

Abra o terminal (ou prompt de comando) e instale as bibliotecas necessárias:

`pip install discord.py pyserial`

# programação

### Parte do Arduino

1.Abra a IDE do Arduino, com o código do arquivo arduino.ino

2.Conecte a sua placa Arduino ao computador

3.Na IDE, selecione o modelo correto de Arduino e a porta na qual se encontra a placa

4.Realize a compilação e envio do código para a placa
 
 ### Parte do Python

1.Abra a Python e selecione o a arquivo bot.py

2.mude o token para o do seu bot:

![image](https://github.com/user-attachments/assets/2dbce8eb-53ea-4992-b7d0-cbcf9012475b)

3.verifique a porta q o seu arduino esta conectada e mude caso for necessário:

![image](https://github.com/user-attachments/assets/d6534a7f-d3bc-48ec-92dd-63d56388023c)

4.conecte a placa arduino na porta usb celecionada

5.execute o código(run)

## controle do LED/buzzer

### mande isso no chat com o bot

|   $led_on     |   $led_off    |
| ------------- |:-------------:|
| ligado        |    desligado  |


## Problemas conhecidos:
### Atualmente, o projeto se encontra com algumas limitações:

- É necessário ter o Arduino conectado (via cabo) ao mesmo computador que está rodando o bot de Discord

# token vazou ⚠️

## caso o seu token vaze faça o seginte processo para reinicialo o mais rapido possivel

1.Acesse o Portal de Desenvolvedores do Discord:

[Portal de Desenvolvedores do Discord](https://discord.com/developers/applications)


2.Vá para o site do Discord Developer Portal.
Faça login na sua conta:

3.Use suas credenciais do Discord para entrar.
Selecione seu aplicativo:

4.Na página inicial do portal, localize e clique no seu aplicativo (bot) que você deseja editar.
Vá para a seção "Bot":

5.No menu lateral esquerdo, clique em "Bot". Isso abrirá as configurações do seu bot.
Regenerar o token:

6.Na seção "Token", você verá seu token atual do bot.
Clique no botão "Regenerate" (Regenerar). Uma janela pop-up aparecerá para confirmar a ação.

7.Confirme a regeneração. Isso irá criar um novo token e invalidar o antigo.
Copie o novo token:

8.Após regenerar, copie o novo token e subistiua no código bot.py

# Guarde-o em um lugar seguro. Não compartilhe esse token com ninguém.

## Autores:


#### - zz66600 [zz66600](https://github.com/zz66600/)
