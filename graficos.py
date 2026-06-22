import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

plt.style.use('dark_background')

plt.rcParams['font.family'] = 'monospace'
plt.rcParams['text.color'] = '#94A3B8'          
plt.rcParams['axes.labelcolor'] = '#64748B'     
plt.rcParams['xtick.color'] = '#475569'         
plt.rcParams['ytick.color'] = '#475569'
plt.rcParams['grid.color'] = '#334155'         
plt.rcParams['grid.alpha'] = 0.15

COR_CARD_FUNDO = '#090A0F'  
PALETA_CUSTOM = ['#2E4057', '#4A6FA5', '#6D9DC5', '#84A98C', '#A3B19B']

arquivos_especificos = {
    'Estresse': 'posts_stress.csv',
    'Depressão': 'posts_depression.csv',
    'Transtorno Bipolar': 'posts_bipolar_disorder.csv',
    'Transtorno de Personalidade': 'posts_personality_disorder.csv',
    'Ansiedade': 'posts_anxiety.csv'
}


lista_df = []
for categoria, arquivo in arquivos_especificos.items():
    if os.path.exists(arquivo):
        df_sub = pd.read_csv(arquivo, sep=';')
        df_sub['Categoria'] = categoria
        lista_df.append(df_sub)

df_completo = pd.concat(lista_df, ignore_index=True)

df_completo['Tamanho_Texto'] = df_completo['text'].astype(str).apply(len)
df_completo['Tamanho_Titulo'] = df_completo['title'].astype(str).apply(len)
df_completo['Palavras_No_Titulo'] = df_completo['title'].astype(str).apply(lambda x: len(x.split()))


# GRÁFICO 1: Volume de Posts por Transtorno Mental

plt.figure(figsize=(11, 5.5))
ax = plt.subplot()
ax.set_facecolor(COR_CARD_FUNDO)

df_vol = df_completo['Categoria'].value_counts().reset_index()
bars = ax.barh(df_vol['Categoria'], df_vol['count'], color=PALETA_CUSTOM[:len(df_vol)], alpha=0.85)

plt.title('VOLUME TOTAL DE POSTS POR TRANSTORNO MENTAL', fontsize=12, pad=20, fontweight='bold', color='#E2E8F0')
plt.xlabel('CONTAGEM ABSOLUTA', fontsize=9, labelpad=10)

ax.bar_label(bars, padding=8, color='#94A3B8', fontweight='bold', fontsize=10)

plt.gca().invert_yaxis() 
plt.grid(axis='x')
plt.tight_layout()
plt.savefig('grafico1_volume_posts.png', dpi=300, bbox_inches='tight')
plt.show()


# GRÁFICO 2: Comprimento Médio dos Títulos

plt.figure(figsize=(11, 5.5))
ax = plt.subplot()
ax.set_facecolor(COR_CARD_FUNDO)

df_titulos = df_completo.groupby('Categoria')['Tamanho_Titulo'].mean().reset_index().sort_values(by='Tamanho_Titulo')
bars = ax.bar(df_titulos['Categoria'], df_titulos['Tamanho_Titulo'], color=PALETA_CUSTOM[:len(df_titulos)], alpha=0.85)

plt.title('COMPRIMENTO MÉDIO DOS TÍTULOS (CARACTERES)', fontsize=12, pad=20, fontweight='bold', color='#E2E8F0')
plt.ylabel('MÉDIA DE CARACTERES', fontsize=9, labelpad=10)
plt.xticks(fontsize=10, rotation=10)

ax.bar_label(bars, fmt='%.1f', padding=5, color='#94A3B8', fontweight='bold')

plt.grid(axis='y')
plt.tight_layout()
plt.savefig('grafico2_comprimento_titulos.png', dpi=300, bbox_inches='tight')
plt.show()


# GRÁFICO 3: Distribuição do Comprimento dos Textos (Boxplot)

plt.figure(figsize=(11, 5.5))
ax = plt.subplot()
ax.set_facecolor(COR_CARD_FUNDO)

df_boxplot_filtrado = df_completo[df_completo['Tamanho_Texto'] < 2500]
boxplot = df_boxplot_filtrado.boxplot(column='Tamanho_Texto', by='Categoria', ax=ax, grid=False, patch_artist=True, showfliers=False)

plt.title('DISPERSÃO DO COMPRIMENTO DOS TEXTOS', fontsize=12, pad=20, fontweight='bold', color='#E2E8F0')
plt.suptitle('') 
plt.xlabel('')
plt.ylabel('NÚMERO DE CARACTERES', fontsize=9, labelpad=10)
plt.xticks(fontsize=10, rotation=10)

for patch, color in zip(ax.patches, PALETA_CUSTOM):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)
    patch.set_edgecolor('#475569')

plt.grid(axis='y')
plt.tight_layout()
plt.savefig('grafico3_boxplot_textos.png', dpi=300, bbox_inches='tight')
plt.show()


# GRÁFICO 4: Top 12 Termos mais Recorrentes nos Títulos 

plt.figure(figsize=(11, 5.5))
ax = plt.subplot()
ax.set_facecolor(COR_CARD_FUNDO)

stopwords_en = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'you', 'your', 'he', 'him', 'his', 'she', 'her', 'it', 'its', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'of', 'at', 'by', 'for', 'with', 'about', 'to', 'in', 'on', 'dont', 'feel', 'like', 'want'}
palavras_totais = []
for t in df_completo['title'].dropna().astype(str):
    tokens = [w.lower().strip("?!.,:;()\"'") for w in t.split()]
    for w in tokens:
        if w and w not in stopwords_en and len(w) > 2:
            palavras_totais.append(w)

contagem = Counter(palavras_totais)
df_top_words = pd.DataFrame(contagem.most_common(12), columns=['Palavra', 'Frequência'])

bars = ax.barh(df_top_words['Palavra'], df_top_words['Frequência'], color='#4A6FA5', alpha=0.8)

plt.title('TOP 12 TERMOS MAIS RECORRENTES NOS TÍTULOS', fontsize=12, pad=20, fontweight='bold', color='#E2E8F0')
plt.xlabel('FREQUÊNCIA ABSOLUTA', fontsize=9, labelpad=10)

ax.bar_label(bars, padding=6, color='#94A3B8', fontweight='bold')

plt.gca().invert_yaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.savefig('grafico4_top_palavras_titulos.png', dpi=300, bbox_inches='tight')
plt.show()


# GRÁFICO 5: Média de Palavras Digitadas por Título

plt.figure(figsize=(11, 5.5))
ax = plt.subplot()
ax.set_facecolor(COR_CARD_FUNDO)

df_palavras_titulo = df_completo.groupby('Categoria')['Palavras_No_Titulo'].mean().reset_index().sort_values(by='Palavras_No_Titulo')
bars = ax.bar(df_palavras_titulo['Categoria'], df_palavras_titulo['Palavras_No_Titulo'], color=PALETA_CUSTOM[:len(df_palavras_titulo)], alpha=0.85)

plt.title('MÉDIA DE PALAVRAS DIGITADAS POR TÍTULO', fontsize=12, pad=20, fontweight='bold', color='#E2E8F0')
plt.xlabel('')
plt.ylabel('MÉDIA DE PALAVRAS', fontsize=9, labelpad=10)
plt.xticks(fontsize=10, rotation=10)

ax.bar_label(bars, fmt='%.1f', padding=5, color='#94A3B8', fontweight='bold')

plt.grid(axis='y')
plt.tight_layout()
plt.savefig('grafico5_media_palavras_titulo.png', dpi=300, bbox_inches='tight')
plt.show()


# GRÁFICO 6: Extensão Média do Post por Transtorno

plt.figure(figsize=(11, 5.5))
ax = plt.subplot()
ax.set_facecolor(COR_CARD_FUNDO)

df_tamanho_post = df_completo.groupby('Categoria')['Tamanho_Texto'].mean().reset_index().sort_values(by='Tamanho_Texto', ascending=False)
bars = ax.barh(df_tamanho_post['Categoria'], df_tamanho_post['Tamanho_Texto'], color=PALETA_CUSTOM[:len(df_tamanho_post)], alpha=0.85)

plt.title('EXTENSÃO MÉDIA DO POST (CARACTERES) POR TRANSTORNO', fontsize=12, pad=20, fontweight='bold', color='#E2E8F0')
plt.xlabel('COMPRIMENTO MÉDIO DO TEXTO', fontsize=9, labelpad=10)
plt.ylabel('')

ax.bar_label(bars, fmt='%.0f', padding=8, color='#94A3B8', fontweight='bold', fontsize=10)

plt.grid(axis='x')
plt.tight_layout()
plt.savefig('grafico6_extensao_media_posts.png', dpi=300, bbox_inches='tight')
plt.show()

