# README - Script de Automação Web com Selenium e Playwright

## Descrição
Este é um script Python que utiliza as bibliotecas Selenium e Playwright para automatizar tarefas em uma aplicação web específica. O objetivo é realizar o envio de XMLs por e-mail para clientes, de acordo com suas configurações específicas.

## Pré-requisitos
- Python 3.x instalado
- Bibliotecas Python:
  - json
  - selenium
  - playwright
- Um navegador web com suporte para automação (Chrome neste caso)
- Conexão à internet

## Configuração
1. Instale as bibliotecas necessárias:

2. Certifique-se de ter o navegador Chrome instalado, pois o script utiliza o driver do Chrome para automação.

3. Certifique-se de que os dados dos clientes estejam devidamente configurados no formato JSON dentro da variável `dados_json` no início do script. Cada cliente deve ter um nome, um e-mail e um nome de e-mail associados, além do campo `isPDV` que indica o tipo de cliente (0 = Somente NF-e, 1 = Somente NFC-e, 2 = NF-e e NFC-e).

## Como usar
1. Execute o script:

2. O script irá abrir uma instância do navegador Chrome e acessar a página de login da aplicação web especificada.

3. O script realizará o login na aplicação utilizando as credenciais definidas no código (e-mail e senha).

4. Para cada cliente configurado no JSON, o script realizará o seguinte procedimento:
- Verifica o tipo de cliente (NF-e, NFC-e ou ambos).
- Caso o cliente seja encontrado na lista correspondente (pdv_0_list, pdv_1_list ou pdv_2_list), ele será habilitado.
- O script navegará até a página de envio de XMLs por e-mail.
- O e-mail e o nome do cliente serão preenchidos nos campos necessários.
- O XML será enviado por e-mail ao cliente.
- Caso ocorra algum problema durante o envio, o script tentará novamente.

5. Após o procedimento para todos os clientes configurados, o navegador será fechado.

## Observações
- Certifique-se de que as informações de login (e-mail e senha) estejam corretas no script antes de executá-lo.
- O script foi desenvolvido para uma aplicação web específica e pode não funcionar em outras aplicações sem ajustes adequados.
- Verifique a compatibilidade do script com a versão do navegador Chrome instalada em sua máquina.
