# app Agromarkers
app da agromarkers gestao de laboratorio molecular

## Problema
Os laboratórios de Marcadores Moleculares enfrentam diversos problelmas para gerenciar seu pipeline de produção de resultados. 
A rastreabilidade das amostras e das placas durante o processo é fundamental para a qualidade de apresentação dos resultados. 
Em geral as amostras são entregues em placas de 96 posições que precisam ser tratadas e transferidas para placas de 384 posições e estas por sua vez para 1.536. Rastrear as amostras nestas placas é um desafio considerável. 
Segue uma lista de problemas que se pretende resolver.
- rastrear as amostras nas diferentes placas e etapas do processo.
- possibilitar o controle através da leitura e geração de código de barras.
- manter o histórico das operações.

## Solução
Desenvolvimento de banco de dados, tabelas e processo utilizando o framework Django do Python. A escolha desta ferramenta deu-se pela velocidade de implementação, por sua facilidade de manutenção. 

## Funcionalidades

### Cadastros
- Empresas
- Projetos
- Placas
- Etapadas
- Status
- Resultados
- Posições

### Processos
- Sistema de autenticação padrão Django
- CRUD para todos os cadastros.
- Criação automática das placas e amostras após a criação do projeto, com registro de posição na placa. 
- Transferência automática de amostras para novas placas, com registro de posição na placa.
- Carga de arquivo de resultados e atualização automática da amostra com rastreio para placa e posição.
- Congelamento do projeto para evitar alterações após carga de resultados.

### Dash Board
- Quantidade de empresas cadastradas
- Quantidade de projetos executados
- Quantidade de projetos em andamento
- Quantidade de amostras analisadas
- Quantidade de amostras em análise
- Back de log de amostras a sereme analisadas
    
