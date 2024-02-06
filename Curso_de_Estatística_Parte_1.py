#!/usr/bin/env python
# coding: utf-8

# ***
# # <font color=green size=10>CURSO DE ESTATÍSTICA - PARTE 1</font>
# ***

# # <font color=green>1 CONHECENDO OS DADOS</font>
# ***

# ## <font color=green>1.1 Dataset do projeto</font>
# ***

# ### Pesquisa Nacional por Amostra de Domicílios - 2015
# 
# A <b>Pesquisa Nacional por Amostra de Domicílios - PNAD</b> investiga anualmente, de forma permanente, características gerais da população, de educação, trabalho, rendimento e habitação e outras, com periodicidade variável, de acordo com as necessidades de informação para o país, como as características sobre migração, fecundidade, nupcialidade, saúde, segurança alimentar, entre outros temas. O levantamento dessas estatísticas constitui, ao longo dos 49 anos de realização da pesquisa, um importante instrumento para formulação, validação e avaliação de políticas orientadas para o desenvolvimento socioeconômico e a melhoria das condições de vida no Brasil.

# ### Fonte dos Dados
# 
# https://ww2.ibge.gov.br/home/estatistica/populacao/trabalhoerendimento/pnad2015/microdados.shtm

# ### Variáveis utilizadas
# 
# > ### Renda
# > ***
# 
# Rendimento mensal do trabalho principal para pessoas de 10 anos ou mais de idade.
# 
# > ### Idade
# > ***
# 
# Idade do morador na data de referência em anos.
# 
# > ### Altura (elaboração própria)
# > ***
# 
# Altura do morador em metros.
# 
# > ### UF
# > ***
# 
# |Código|Descrição|
# |---|---|
# |11|Rondônia|
# |12|Acre|
# |13|Amazonas|
# |14|Roraima|
# |15|Pará|
# |16|Amapá|
# |17|Tocantins|
# |21|Maranhão|
# |22|Piauí|
# |23|Ceará|
# |24|Rio Grande do Norte|
# |25|Paraíba|
# |26|Pernambuco|
# |27|Alagoas|
# |28|Sergipe|
# |29|Bahia|
# |31|Minas Gerais|
# |32|Espírito Santo|
# |33|Rio de Janeiro|
# |35|São Paulo|
# |41|Paraná|
# |42|Santa Catarina|
# |43|Rio Grande do Sul|
# |50|Mato Grosso do Sul|
# |51|Mato Grosso|
# |52|Goiás|
# |53|Distrito Federal|
# 
# > ### Sexo	
# > ***
# 
# |Código|Descrição|
# |---|---|
# |0|Masculino|
# |1|Feminino|
# 
# > ### Anos de Estudo
# > ***
# 
# |Código|Descrição|
# |---|---|
# |1|Sem instrução e menos de 1 ano|
# |2|1 ano|
# |3|2 anos|
# |4|3 anos|
# |5|4 anos|
# |6|5 anos|
# |7|6 anos|
# |8|7 anos|
# |9|8 anos|
# |10|9 anos|
# |11|10 anos|
# |12|11 anos|
# |13|12 anos|
# |14|13 anos|
# |15|14 anos|
# |16|15 anos ou mais|
# |17|Não determinados| 
# ||Não aplicável|
# 
# > ### Cor
# > ***
# 
# |Código|Descrição|
# |---|---|
# |0|Indígena|
# |2|Branca|
# |4|Preta|
# |6|Amarela|
# |8|Parda|
# |9|Sem declaração|

# #### <font color='red'>Observação</font>
# ***
# > Os seguintes tratamentos foram realizados nos dados originais:
# > 1. Foram eliminados os registros onde a <b>Renda</b> era inválida (999 999 999 999);
# > 2. Foram eliminados os registros onde a <b>Renda</b> era missing;
# > 3. Foram considerados somente os registros das <b>Pessoas de Referência</b> de cada domicílio (responsável pelo domicílio).

# ### Importando pandas e lendo o dataset do projeto
# 
# https://pandas.pydata.org/

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv("dados.csv")


# In[3]:


dados.head()


# ## <font color=green>1.2 Tipos de dados</font>
# ***

# ### Variáveis qualitativas ordinais
# 
# ► Variáveis que podem ser ordenadas ou hierarquizardas

# In[4]:


sorted(dados['Anos de Estudo'].unique())


# ### Variáveis qualitativas nominais
# 
# ► Variáveis que não podem ser ordenadas ou hierarquizardas

# In[5]:


sorted(dados['UF'].unique())


# In[6]:


sorted(dados['Sexo'].unique())


# In[7]:


sorted(dados['Cor'].unique())


# ### Variáveis quantitativas discretas
# 
# ► Variáveis que representam uma contagem onde os valores possíveis formam um conjunto finito ou enumerável.

# In[8]:


print('De %s até %s anos' % (dados.Idade.min(), dados.Idade.max()))


# #### <font color='red'>Observação</font>
# ***
# > A variável idade pode ser classificada de três formas distintas:
# > 1. <b>QUANTITATIVA DISCRETA</b> - quando representa anos completos (números inteiros);
# > 2. <b>QUANTITATIVA CONTÍNUA</b> - quando representa a idade exata, sendo representado por frações de anos; e
# > 3. <b>QUALITATIVA ORDINAL</b> - quando representa faixas de idade.

# ### Variáveis quantitativas contínuas
# 
# ► Variáveis que representam uma contagem ou mensuração que assumem valores em uma escala contínua (números reais).

# In[9]:


print('De %s até %s metros' % (dados['Altura'].min(), dados.Altura.max()))


# ### Classificação de uma variável
# <img src='https://caelum-online-public.s3.amazonaws.com/1177-estatistica-parte1/01/img001.png' width='70%'>

# # <font color=green>2 DISTRIBUIÇÃO DE FREQUÊNCIAS</font>
# ***
# 
# O primeiro passo em um trabalho de análise é o conhecimento do comportamento das variáveis envolvidas no estudo. Utilizando técnicas estatísticas como as análises das <b>DISTRIBUIÇÕES DE FREQUÊNCIAS</b> e <b>HISTOGRAMAS</b> podemos avaliar melhor a forma como os fenômenos em estudo se distribuem.

# ## <font color=green>2.1 Distribuição de frequências para variáveis qualitativas</font>
# ***

# ### Método 1

# https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.Series.value_counts.html

# In[10]:


dados['Sexo'].value_counts()


# In[11]:


dados['Sexo'].value_counts(normalize = True) * 100


# In[12]:


frequencia = dados['Sexo'].value_counts()


# In[13]:


percentual = dados['Sexo'].value_counts(normalize = True) * 100


# In[14]:


dist_freq_qualitativas = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})


# In[15]:


dist_freq_qualitativas


# In[16]:


dist_freq_qualitativas.rename(index = {0: 'Masculino', 1: 'Feminino'}, inplace = True)
dist_freq_qualitativas.rename_axis('Sexo', axis= 'columns', inplace = True)


# In[17]:


dist_freq_qualitativas


# ### Método 2

# https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.crosstab.html

# In[18]:


sexo = {0: 'Masculino', 
        1: 'Feminino'}

cor = {0: 'Indígena', 
       2: 'Branca', 
       4: 'Preta', 
       6: 'Amarela', 
       8: 'Parda', 
       9: 'Sem declaração'}


# In[19]:


frequencia = pd.crosstab(dados.Sexo,
                         dados.Cor)
frequencia.rename(index = sexo, inplace = True)
frequencia.rename(columns = cor, inplace = True)
frequencia


# In[20]:


percentual = pd.crosstab(dados.Sexo,
                         dados.Cor,
                         normalize = True) * 100
percentual.rename(index = sexo, inplace = True)
percentual.rename(columns = cor, inplace = True)
percentual


# In[21]:


percentual = pd.crosstab(dados.Sexo,
                         dados.Cor,
                         aggfunc = 'mean',
                         values = dados.Renda)
percentual.rename(index = sexo, inplace = True)
percentual.rename(columns = cor, inplace = True)
percentual


# ## <font color=green>2.2 Distribuição de frequências para variáveis quantitativas (classes personalizadas)</font>
# ***

# ### Passo 1 - Especificar os limites de cada classe
# 
# Utilizar a seguinte classificação:
# 
# <b>A</b> ► Acima de 20 SM
# 
# <b>B</b> ► De 10 a 20 SM
# 
# <b>C</b> ► De 4 a 10 SM
# 
# <b>D</b> ► De 2 a 4 SM
# 
# <b>E</b> ► Até 2 SM
# 
# onde <b>SM</b> é o valor do salário mínimo na época. Em nosso caso <b>R$ 788,00</b> (2015):
# 
# <b>A</b> ► Acima de 15.760
# 
# <b>B</b> ► De 7.880 a 15.760
# 
# <b>C</b> ► De 3.152 a 7.880
# 
# <b>D</b> ► De 1.576 a 3.152
# 
# <b>E</b> ► Até 1.576
# 

# In[22]:


dados.Renda.min()


# In[23]:


dados.Renda.max()


# In[24]:


classes = [0, 1576, 3152, 7880, 15760, 200000]


# In[25]:


labels = ['E', 'D', 'C', 'B', 'A']


# ### Passo 2 - Criar a tabela de frequências

# https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.cut.html

# In[26]:


frequencia = pd.value_counts(
  pd.cut(x = dados.Renda,
         bins = classes,
         labels = labels,
         include_lowest = True)
)
frequencia


# In[27]:


percentual = pd.value_counts(
  pd.cut(x = dados.Renda,
         bins = classes,
         labels = labels,
         include_lowest = True),
  normalize = True
)
percentual


# In[28]:


dist_freq_quantitativas_personalizadas = pd.DataFrame(
    {'Frequência': frequencia, 'Porcentagem (%)': percentual}
)
dist_freq_quantitativas_personalizadas


# In[29]:


dist_freq_quantitativas_personalizadas.sort_index(ascending = False)


# ## <font color=green>2.3 Distribuição de frequências para variáveis quantitativas (classes de amplitude fixa)</font>
# ***

# ### Importando bibliotecas
# 
# http://www.numpy.org/

# In[30]:


import numpy as np


# ### Passo 1 - Difinindo o número de classes

# #### Regra de Sturges
# 
# # $$k = 1 + \frac {10}{3}\log_{10}n$$

# In[31]:


n = dados.shape[0]
n


# In[32]:


k = 1 + (10 /3) * np.log10(n)


# In[33]:


k


# In[34]:


k = int(k.round(0))
k


# ### Passo 2 - Criar a tabela de frequências

# In[35]:


frequencia = pd.value_counts(
  pd.cut(
    x = dados.Renda,
    bins = 17,
    include_lowest = True
  ),
  sort = False
)


# In[36]:


percentual = pd.value_counts(
  pd.cut(
    x = dados.Renda,
    bins = 17,
    include_lowest = True
  ),
  sort = False,
  normalize = True
)
percentual


# In[37]:


dist_freq_quantitativas_amplitude_fixa = pd.DataFrame(
    {'Frequência': frequencia, 'Porcentagem (%)': percentual}
)
dist_freq_quantitativas_amplitude_fixa


# ## <font color=green>2.4 Histograma</font>
# ***
# 
# O <b>HISTOGRAMA</b> é a representação gráfica de uma distribuição de frequências. É um gráfico formado por um conjunto de retângulos colocados lado a lado, onde a área de cada retângulo é proporcional à frequência da classe que ele representa.

# ### Importando a biblioteca
# 
# https://seaborn.pydata.org/

# In[38]:


import seaborn as sns


# In[39]:


ax = sns.distplot(dados.Altura, kde = False)

ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax


# In[40]:


ax = sns.distplot(dados.Altura)


ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura - KDE', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax


# In[41]:


dados.Altura.hist(bins = 50, figsize=(12, 6))


# In[42]:


dist_freq_quantitativas_personalizadas


# In[43]:


dist_freq_quantitativas_personalizadas['Frequência'].plot.bar(width= 1, color = 'blue', alpha = 0.2, figsize=(12, 6))


# # <font color=green>3 MEDIDAS DE TENDÊNCIA CENTRAL</font>
# ***

# ## DataFrame de exemplo

# In[44]:


df = pd.DataFrame(data = {'Fulano': [8, 10, 4, 8, 6, 10, 8],
                          'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
                          'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]}, 
                  index = ['Matemática', 
                           'Português', 
                           'Inglês', 
                           'Geografia', 
                           'História', 
                           'Física', 
                           'Química'])
df.rename_axis('Matérias', axis = 'columns', inplace = True)
df


# ## <font color=green>3.1 Média aritmética</font>
# ***
# 
# É representada por $\mu$ quando se refere à população e por $\bar{X}$ quando se refere à amostra
# 
# # $$\mu = \frac 1n\sum_{i=1}^{n}X_i$$
# 
# onde 
# 
# $n$ = número de observações (registros)
# 
# $X_i$ = valor da i-ésima observação (registro)

# In[45]:


(8 + 10 + 4 + 8 + 6 + 10 + 8) / 7


# In[46]:


df['Fulano'].mean()


# In[47]:


dados.Renda.mean()


# In[48]:


dados.groupby(['Sexo'])['Renda'].mean()


# ## <font color=green>3.2 Mediana</font>
# ***
# 
# Para obtermos a mediana de uma conjunto de dados devemos proceder da seguinte maneira:
# 1. Ordenar o conjunto de dados;
# 2. Identificar o número de observações (registros) do conjunto de dados ($n$);
# 3. Identicar o elemento mediano:
# 
# > Quando $n$ for ímpar, a posição do elemento mediano será obtida da seguinte forma:
# 
# 
# # $$Elemento_{Md} = \frac{n+1}2$$
# 
# > Quando $n$ for par, a posição do elemento mediano será obtida da seguinte forma:
# 
# 
# # $$Elemento_{Md} = \frac{n}2$$
# 
# 4. Obter a mediana:
# 
# > Quando $n$ for ímpar:
# 
# 
# # $$Md = X_{Elemento_{Md}}$$
# 
# > Quando $n$ for par:
# 
# 
# # $$Md = \frac{X_{Elemento_{Md}} + X_{Elemento_{Md}+1}}2$$
# ***

# ### Exemplo 1 - n ímpar
# 
# <img src='https://caelum-online-public.s3.amazonaws.com/1177-estatistica-parte1/01/img002.png' width='40%' style="float:left">

# In[49]:


notas_fulano = df.Fulano
notas_fulano


# In[50]:


notas_fulano = notas_fulano.sort_values()
notas_fulano


# In[51]:


notas_fulano = notas_fulano.reset_index()
notas_fulano


# In[52]:


n = notas_fulano.shape[0]
n


# In[53]:


elemento_md = (n + 1) / 2
elemento_md


# In[54]:


notas_fulano.loc[elemento_md - 1]


# In[55]:


notas_fulano.median()


# ### Exemplo 2 - n par
# 
# <img src='https://caelum-online-public.s3.amazonaws.com/1177-estatistica-parte1/01/img003.png' width='50%' style="float:left">

# In[56]:


notas_beltrano = df.Beltrano.sample(6, random_state = 101)
notas_beltrano


# In[57]:


notas_beltrano = notas_beltrano.sort_values()
notas_beltrano


# In[58]:


notas_beltrano = notas_beltrano.reset_index()
notas_beltrano


# In[59]:


n = notas_beltrano.shape[0]
n


# In[60]:


elemento_md = n / 2
elemento_md


# In[61]:


(notas_beltrano.Beltrano[elemento_md - 1] + notas_beltrano.Beltrano[elemento_md]) / 2


# In[62]:


notas_beltrano.median()


# ### Obtendo a mediana em nosso dataset

# In[63]:


dados.Renda.median()


# In[64]:


dados.Renda.quantile()


# ## <font color=green>3.3 Moda</font>
# ***
# 
# Pode-se definir a moda como sendo o valor mais frequente de um conjunto de dados. A moda é bastante utilizada para dados qualitativos.

# In[65]:


df


# In[66]:


df.mode()


# In[67]:


exemplo = pd.Series([1, 2, 2, 3, 4, 4, 5, 6, 7])
exemplo


# In[68]:


exemplo.mode()


# ### Obtendo a moda em nosso dataset

# In[69]:


dados.Renda.mode()


# In[70]:


dados.Altura.mode()


# ## <font color=green>3.4 Relação entre média, mediana e moda</font>
# ***

# <img src='https://caelum-online-public.s3.amazonaws.com/1177-estatistica-parte1/01/img004.png' width='80%'>

# ### Avaliando a variável RENDA

# In[71]:


ax = sns.distplot(dados.query('Renda < 20000').Renda)
ax.figure.set_size_inches(12, 6)
ax


# In[72]:


Moda = dados.Renda.mode()[0]
Moda


# In[73]:


Mediana = dados.Renda.median()
Mediana


# In[74]:


Media = dados.Renda.mean()
Media


# In[75]:


Moda < Mediana < Media


# ***

# ### Avaliando a variável ALTURA

# In[76]:


ax = sns.distplot(dados.Altura)
ax.figure.set_size_inches(12, 6)
ax


# In[77]:


Moda = dados.Altura.mode()
Moda


# In[78]:


Mediana = dados.Altura.median()
Mediana


# In[79]:


Media = dados.Altura.mean()
Media


# ***

# ### Avaliando a variável ANOS DE ESTUDO

# In[80]:


ax = sns.distplot(dados['Anos de Estudo'], bins = 17)
ax.figure.set_size_inches(12, 6)
ax


# In[81]:


Moda = dados['Anos de Estudo'].mode()[0]
Moda


# In[82]:


Mediana = dados['Anos de Estudo'].median()
Mediana


# In[83]:


Media = dados['Anos de Estudo'].mean()
Media


# In[84]:


Moda > Mediana > Media


# # <font color=green>4 MEDIDAS SEPARATRIZES</font>
# ***

# ## <font color=green>4.1 Quartis, decis e percentis</font>
# ***
# 
# Há uma série de medidas de posição semelhantes na sua concepção à mediana, embora não sejam medidas de tendência central. Como se sabe, a mediana divide a distribuição em duas partes iguais quanto ao número de elementos de cada parte. Já os quartis permitem dividir a distribuição em quatro partes iguais quanto ao número de elementos de cada uma; os decis em dez partes e os centis em cem partes iguais.

# In[85]:


dados.Renda.quantile([0.25, 0.5, 0.75])


# In[86]:


[i / 10 for i in range(1, 10)]


# In[87]:


dados.Renda.quantile([i / 10 for i in range(1, 10)])


# In[88]:


dados.Renda.quantile([i / 100 for i in range(1, 100)])


# In[89]:


ax = sns.distplot(dados.Idade, 
                  hist_kws = {'cumulative': True},
                  kde_kws = {'cumulative': True},
                  bins = 10)
ax.figure.set_size_inches(14, 6)
ax.set_title('Distribuição de Frequências Acumulada', fontsize=18)
ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Anos', fontsize=14)
ax


# In[90]:


dados.Idade.quantile([i / 10 for i in range(1, 10)])


# ## <font color=green>4.2 Box-plot</font>
# ***
# 
# O box plot dá uma idéia da posição, dispersão, assimetria, caudas e dados discrepantes (outliers). A posição central é dada pela mediana e a dispersão por $IIQ$. As posições relativas de $Q1$, $Mediana$ e $Q3$ dão uma noção da simetria da distribuição. Os comprimentos das cauda são dados pelas linhas que vão do retângulo aos valores remotos e pelos valores atípicos.

# <img src='https://caelum-online-public.s3.amazonaws.com/1177-estatistica-parte1/01/img005.png' width='65%'>

# In[91]:


ax = sns.boxplot(x = 'Altura', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax


# In[92]:


ax = sns.boxplot(x = 'Altura', y = 'Sexo', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax


# In[93]:


ax = sns.boxplot(x = 'Renda', data = dados.query('Renda < 10000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax


# In[94]:


ax = sns.boxplot(x = 'Renda', y = 'Sexo', data = dados.query('Renda < 10000'), orient = 'h')

ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax


# In[95]:


ax = sns.boxplot(x = 'Anos de Estudo', data = dados, orient = 'h')

ax.figure.set_size_inches(12, 4)
ax.set_title('Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax


# In[96]:


ax = sns.boxplot(x = 'Anos de Estudo', y = 'Sexo', data = dados, orient = 'h')

ax.figure.set_size_inches(12, 4)
ax.set_title('Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax


# <img src='https://caelum-online-public.s3.amazonaws.com/1177-estatistica-parte1/01/img006.png' width='80%'>

# # <font color=green>5 MEDIDAS DE DISPERSÃO</font>
# ***
# 
# Embora as medidas de posição forneçam uma sumarização bastante importante dos dados, elas podem não ser suficientes para caracterizar conjuntos distintos, especialmente quando as observações de determinada distribuição apresentarem dados muito dispersos.

# ## <font color=green>5.1 Desvio médio absoluto</font>
# ***
# 
# 
# # $$DM = \frac 1n\sum_{i=1}^{n}|X_i-\bar{X}|$$
# 

# In[97]:


df


# In[98]:


notas_fulano = df[['Fulano']]
notas_fulano


# In[99]:


nota_media_fulano = notas_fulano.mean()[0]
nota_media_fulano


# In[100]:


notas_fulano['Desvio'] = notas_fulano['Fulano'] - nota_media_fulano
notas_fulano


# In[101]:


notas_fulano['Desvio'].sum()


# In[102]:


notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()
notas_fulano


# In[103]:


ax = notas_fulano['Fulano'].plot(style = 'o')
ax.figure.set_size_inches(14, 6)
ax.hlines(y = nota_media_fulano, xmin = 0, xmax = notas_fulano.shape[0] - 1, colors='red')
for i in range(notas_fulano.shape[0]):
    ax.vlines(x = i, ymin = nota_media_fulano, ymax = notas_fulano['Fulano'][i], linestyles='dashed')
ax


# In[104]:


notas_fulano['|Desvio|'].mean()


# In[105]:


desvio_medio_absoluto = notas_fulano['Fulano'].mad()
desvio_medio_absoluto


# ## <font color=green>5.2 Variância</font>
# ***

# ### Variância
# 
# A variância é construída a partir das diferenças entre cada observação e a média dos dados, ou seja, o desvio em torno da média. No cálculo da variância, os desvios em torno da média são elevados ao quadrado.

# ### Variância populacional
# 
# # $$\sigma^2 = \frac 1n\sum_{i=1}^{n}(X_i-\mu)^2$$

# ### Variância amostral
# 
# # $$S^2 = \frac 1{n-1}\sum_{i=1}^{n}(X_i-\bar{X})^2$$

# In[106]:


notas_fulano['(Desvio)^2'] = notas_fulano['Desvio'].pow(2)
notas_fulano


# In[107]:


notas_fulano['(Desvio)^2'].sum() / (len(notas_fulano) - 1)


# In[108]:


variancia = notas_fulano['Fulano'].var()
variancia


# ## <font color=green>5.3 Desvio padrão</font>
# ***
# 
# Uma das restrições da variância é o fato de fornecer medidas em quadrados das unidades originais - a variância de medidas de comprimento, por exemplo, é em unidades de área. Logo, o fato de as unidades serem diferentes dificulta a comparação da dispersão com as variáveis que a definem. Um modo de eliminar essa dificuldade é considerar sua raiz quadrada.

# ### Desvio padrão populacional
# 
# # $$\sigma = \sqrt{\frac 1n\sum_{i=1}^{n}(X_i-\mu)^2} \Longrightarrow \sigma = \sqrt{\sigma^2}$$

# ### Desvio padrão amostral
# 
# # $$S = \sqrt{\frac 1{n-1}\sum_{i=1}^{n}(X_i-\bar{X})^2} \Longrightarrow S = \sqrt{S^2}$$

# In[109]:


np.sqrt(variancia)


# In[110]:


desvio_padrao = notas_fulano['Fulano'].std()
desvio_padrao


# In[111]:


df


# In[112]:


df.mean()


# In[113]:


df.median()


# In[114]:


df.mode()


# In[115]:


df.std()


# In[ ]:




