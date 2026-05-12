# Proveniência em Dados de Saúde Mental em Redes Sociais

Este repositório apresenta o trabalho final da disciplina **eScience 2026.1**. O projeto tem como foco a coleta reprodutível de dados do Reddit, com captura automática de proveniência utilizando a ferramenta **noWorkflow**.


## Motivação

O Reddit é uma plataforma que, devido ao anonimato dos usuários, concentra relatos espontâneos e autênticos sobre saúde mental — muitos deles não capturados por métodos tradicionais, como surveys clínicos.

Entretanto, identificamos uma lacuna crítica na literatura:

- **Estudos prévios:** Pelo menos 54 estudos científicos já utilizaram dados do Reddit para investigar depressão e ansiedade.
- **Problema:** A ausência de registro detalhado (data, hora, parâmetros da API e etapas de processamento) torna esses estudos pouco transparentes e difíceis de reproduzir.

Sem rastreabilidade, os experimentos tornam-se verdadeiras **“caixas pretas”**.



## Objetivos

O objetivo principal deste projeto é realizar a coleta de dados com **proveniência completa e rastreável**, garantindo transparência e reprodutibilidade.

- **Coleta:** Utilizar Python + PRAW para capturar posts públicos via API do Reddit.
- **Proveniência:** Empregar o noWorkflow para registrar automaticamente a linhagem dos dados.
- **Transparência:** Disponibilizar um repositório público com código documentado e demonstração funcional.

## Instalação

### Requisitos
- Python 3.11 (recomendado — versões mais novas podem causar incompatibilidade com o noWorkflow)
- pip
- virtualenv

### Passo a passo

1. Clone o repositório:
```bash
   git clone <url-do-repositorio>
   cd EScienceReddit
```

2. Crie e ative o ambiente virtual com Python 3.11:
```bash
   python3.11 -m venv venv
   source venv/bin/activate
```

3. Instale as dependências:
```bash
   pip install "setuptools<68"
   pip install "noworkflow[all]"
   pip install praw
```
   > ⚠️ O `setuptools<68` é necessário para resolver incompatibilidade do noWorkflow com versões mais novas do pip.

4. Verifique a instalação do noWorkflow:
```bash
   now --version
```
   Deve retornar: `noWorkflow 2.0.1`



## Metodologia

O fluxo de trabalho está estruturado em quatro etapas principais:

1. **Coleta**  
   Extração de posts dos subreddits:
   - r/depression  
   - r/anxiety  
   - r/mentalhealth  

2. **Registro de Proveniência**  
   Execução do pipeline com noWorkflow, capturando automaticamente:
   - Parâmetros de execução  
   - Dependências  
   - Transformações aplicadas  

3. **Processamento**  
   Limpeza e transformação dos dados com rastreamento completo de cada etapa no grafo de proveniência.

4. **Visualização**  
   Geração de um grafo detalhado representando toda a cadeia de dados, desde a coleta via API até os resultados finais.


## Fonte de Dados

### Opção Principal — Reddit API (PRAW)
A coleta primária será feita via API oficial do Reddit usando a biblioteca PRAW.
O acesso à API está sendo solicitado formalmente ao Reddit para fins acadêmicos.

**Status:** aguardando aprovação do Reddit Data API Team.

### Plano B — Dataset Público (Kaggle)
Caso o acesso à API não seja aprovado dentro do prazo do projeto, utilizaremos
um dataset público disponível no Kaggle contendo posts de subreddits de saúde mental.

Esta alternativa é igualmente válida para os objetivos do projeto, pois o foco
do trabalho é a **captura de proveniência do processamento dos dados** — não a
coleta em si. O noWorkflow registrará todas as etapas de transformação
independentemente da fonte dos dados.

**Dataset de referência:** [Mental Health Reddit Dataset — Kaggle](https://www.kaggle.com/datasets/neelghoshal/reddit-mental-health-data)

### Justificativa
A escolha do Reddit como fonte de dados é embasada na literatura científica:
- **Boettcher et al. (2021)** — *JMIR Mental Health*: revisão sistemática com 54 estudos
  que usaram dados do Reddit para pesquisar depressão e ansiedade.
- **Evkoski et al. (2026)** — *Journal of Medical Internet Research*: análise de rede
  com dados de 545 mil usuários em 114 subreddits de saúde mental, destacando o valor
  do anonimato da plataforma para capturar perspectivas sub-representadas em dados clínicos.



## Entregáveis

- **Script em Python:** Pipeline completo de coleta e processamento, com parâmetros configuráveis  
- **Visualização:** Grafo de proveniência representando todo o fluxo de dados  
- **Repositório:** Código documentado com instruções de uso e demonstração funcional  



# Cronograma (Resumo)

- **Configuração (Semana 2):**  
  Setup do PRAW, noWorkflow e acesso à API do Reddit  

- **Implementação (Semanas 3–4):**  
  Desenvolvimento da coleta e captura da proveniência  

- **Finalização (Semanas 5–7):**  
  Refinamento dos grafos, testes e preparação da apresentação  



## Equipe

- Giovana Beltrame  
- Julia Staudohar  
- Marianna Brito  

**Graduação em eScience**
