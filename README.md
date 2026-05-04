#Proveniência em Dados de Saúde Mental em Redes Sociais
Este repositório apresenta o trabalho final da disciplina eScience 2026.1. O foco do projeto é a coleta reprodutível de dados do Reddit através da captura automática de proveniência, utilizando a ferramenta noWorkflow.  

##Motivação
O Reddit é uma plataforma onde o anonimato gera dados únicos sobre saúde mental, com relatos que muitas vezes não aparecem em surveys clínicos tradicionais. No entanto, identificamos uma lacuna crítica: a falta de rastreabilidade e reprodutibilidade nos estudos que utilizam esses dados.  

Estudos Prévios: Pelo menos 54 estudos científicos já utilizaram dados do Reddit para pesquisar depressão e ansiedade.  

Problema Identificado: Sem registro de data, hora, filtros de API e transformações, os experimentos tornam-se "caixas pretas" impossíveis de replicar.  

##Objetivos
O objetivo principal é coletar dados de saúde mental com proveniência registrada:  

Coleta: Utilizar Python + PRAW para capturar posts públicos via API do Reddit.  

Proveniência: Usar o noWorkflow para capturar automaticamente a linhagem dos dados.  

Transparência: Disponibilizar um repositório público no GitHub com uma demonstração funcional.  

##Metodologia
O fluxo de trabalho está dividido em quatro etapas principais:  

Coleta: Extração de posts dos subreddits r/depression, r/anxiety e r/mentalhealth.  

Registro: Execução via noWorkflow para capturar a proveniência sem alterar o código original.  

Processamento: Limpeza e transformação dos dados com rastreio de cada etapa no grafo.  

Visualização: Geração do grafo de proveniência completo, desde a API até os dados finais.  

##Entregáveis

Script Python: Pipeline de coleta completo e parametrizável.  

Visualização: Grafo de proveniência detalhando a cadeia de dados.  

Repositório: Código documentado com instruções de uso e demo ao vivo.  


##Cronograma (Resumo)

Configuração (Sem. 2): PRAW, noWorkflow e API do Reddit.  

Implementação (Sem. 3-4): Coleta, captura e análise da proveniência.  

Finalização (Sem. 5-7): Refinamento dos grafos e apresentação final.  

##Equipe
Giovana Beltrame   
Julia Staudohar   
Marianna Brito   


Graduação em eScience   
+1
