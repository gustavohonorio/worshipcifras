## WORSHIP CIFRAS
##### Descrição: O sistema Worship Cifras tem como propósito o consumo de cifras musicais de cunho religioso.
___
### Visão geral
##### **Métodologia:** *Agile / Kanban*
##### **Board:** *https://www.meistertask.com/app/project/sRAmfb9w/worship-cifras*
##### **Time:** *Gustavo Honório (PO / Desenvolvedor)*
##### **Tecnologias:** *Front-end (HTML5, CSS, JS) , Back-end (Django, Python) , Data (MySQL)*
___
### Módulos - *Macro*
##### **Core:** *Index do sistema, onde estão alocadas todas as regras da tela inicial.*
##### **Wcartista:** *Aqui estão registradas todas as regras para os objetos artistas do sistema.*
##### **Wccifra:** *Aqui estão registradas todas as regras para os objetos cifras do sistema.*
##### **Wclogon:** *As regras de cadastro de novos usuários e login / logout dos mesmos, ficam neste módulo.*
##### **Wcstaff:** *Neste módulo estão alocadas todas as telas e regras de negócio, da área privada da equipe.*
##### **Worshipcifras:** *Este é o modulo que contem todas as configurações do projeto Django.*
___
### Preparando o ambiente para receber a aplicação
##### **Passo 1:** *Tendo como premissa que o MySql, Python e IDE ja estejam instaladas na maquina, após o download do projeto, é necessário realizar a alteração do usuário e senha de conexão do banco de dados (de acordo com a instalação na sua máquina) no arquivo settings do projeto.*
##### **Passo 2:** *Agora iremos dar a carga de dados para começar a utilizar o projeto. Execute o arquivo "configurando-wcifras-development.sql" no MySql.*
##### **Passo 3:** *Crie o seu usuário na aplicação, e conceda (no mysql) acesso admin para ele no sistema.*
