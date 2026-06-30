 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Nayara Lage Silva 
MAPEAMENTO E ANÁLISE 
MULTITEMPORAL DA 
COBERTURA DO SOLO DO 
MUNICÍPIO DE SÃO THOMÉ 
DAS LETRAS 
UFMG 
Instituto de Geociências 
Departamento de Cartografia 
Av. Antônio Carlos, 6627 – Pampulha 
Belo Horizonte 
cartografia@igc.ufmg.br 
XIV Curso de Especialização em 
Geoprocessamento 

 
 
 
NAYARA LAGE SILVA 
 
 
 
 
MAPEAMENTO E ANÁLISE MULTITEMPORAL DA COBERTURA DO 
SOLO DO MUNICÍPIO DE SÃO THOMÉ DAS LETRAS 
 
 
 
 
 
 
 
 
Monografia apresentada como requisito parcial à 
obtenção 
do 
grau 
de 
Especialista 
em 
Geoprocessamento. Curso de Especialização em 
Geoprocessamento. Departamento de Cartografia. 
Instituto de Geociências. Universidade Federal de 
Minas Gerais. 
 
Orientador: Professor Bráulio Magalhães Fonseca 
 
 
 
 
 
 
Belo Horizonte 
Dezembro de 2014

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

3 
 
 
 
 
 
 
 CursodeEspeciali
Curso de Especialização em GeoprocessamentoUNIVERSIDADE FE
UNIVERSIDADE FEDERAL DE MINAS GERAIS
DE MINAS GERAIS 
Av. Antonio Carlos 6627,  
Belo Horizonte, MG, 31.270-901 
Tel: 55 31 3409-5416 
www.csr.ufmg.br/geoprocessamento 
FOLHA DE APROVAÇÃO 
MAPEAMENTO E ANÁLISE MULTITEMPORAL DA 
COBERTURA DO SOLO DO MUNICÍPIO DE SÃO THOMÉ 
DAS LETRAS 
 
 
Monografia defendida em cumprimento ao requisito exigido para obtenção do titulo de 
Especialista em Geoprocessamento. 
Aprovada em 09 de dezembro de 2014, pela Banca Examinadora constituída pelos 
seguintes membros: 
 
 
 
 
 
 
 
 
Prof. Rodrigo Affonso de Albuquerque Nóbrega 
UFMG 
Prof. Bráulio Magalhães Fonseca – Orientador 
UFMG 
Nayara Lage Silva 

4 
 
 
RESUMO 
O mapeamento da cobertura do solo por meio da utilização de dados de sensoriamento 
remoto e técnicas de processamento digital de imagens tem se difundindo globalmente 
por permitir uma análise espacial e dinâmica das tipologias de cobertura. A mineração é 
uma das atividades transformadoras do meio que mais causa impactos adversos, mesmo 
que de maneira concentrada, devido ao fator de rigidez locacional da atividade. É uma 
atividade que demanda controle ambiental em todo processo para reduzir os impactos 
negativos e garantir um meio ambiente equilibrado. Neste contexto o trabalho objetivou 
realizar uma análise multitemporal da cobertura do solo do município de São Thomé 
das Letras, no estado de Minas Gerais, quantificar e espacializar as alterações no 
período determinado entre 1984 a 2011.  Buscou-se visualizar o comportamento da 
atividade de mineração desde seu início até os dias atuais, e consequentemente, observar 
a dinamicidade das mudanças ocorridas na cobertura do solo das outras classes 
estabelecidas. Para o mapeamento do uso e cobertura do solo foi utilizado o programa 
SPRING/INPE e para a análise temporal/espacial de mudanças utilizou-se a plataforma 
Land Change Modeler acoplada ao programa IDRISI. A partir da análise dos resultados 
foi possível quantificar e espacializar o avanço da mineração sob o campo 
rupestre/afloramento rochoso; a perda substancial da vegetação densa no intervalo do 
período analisado; o crescimento exponencial da ocupação urbana; e o surgimento da 
atividade reflorestamento. 
Palavras-chave: Análise multitemporal; cobertura do solo; mineração; sensoriamento 
remoto. 
 
 
 
 
 
 

5 
 
 
SUMÁRIO 
1. 
INTRODUÇÃO ....................................................................................................... 9 
2. 
OBJETIVOS .......................................................................................................... 10 
3. 
CARACTERIZAÇÃO DA ÁREA DE ESTUDO ............................................... 10 
3.1 
MEIO SOCIOECONÔMICO ................................................................................... 10 
3.2 
MEIO FÍSICO ...................................................................................................... 13 
3.3 
MEIO BIÓTICO ................................................................................................... 17 
4. 
REVISÃO BIBLIOGRÁFICA ............................................................................. 19 
5. 
MATERIAIS E MÉTODOS ................................................................................. 23 
5.1 
ETAPA 1 – OBTENÇÃO DAS IMAGENS LANDSAT 5 TM ....................................... 24 
5.2 
ETAPA 2 - ANÁLISE E TRATAMENTO DAS IMAGENS ........................................... 24 
5.3 
ETAPA 3 - DEFINIÇÃO DAS CLASSES DE COBERTURA DO SOLO (CHAVES DE 
INTERPRETAÇÃO) ......................................................................................................... 25 
5.4 
ETAPA 4 - COLETA DE AMOSTRAS ..................................................................... 27 
5.5 
ETAPA 5 - CLASSIFICAÇÃO DAS IMAGENS ......................................................... 27 
5.6 
ETAPA 6 - QUANTIFICAÇÃO E ANÁLISE DAS ALTERAÇÕES ................................. 28 
6. 
RESULTADOS E DISCUSSÕES ........................................................................ 28 
7. 
CONCLUSÕES ..................................................................................................... 39 
8. 
BIBLIOGRAFIA ................................................................................................... 40 
9. 
APÊNDICE ............................................................................................................ 41 
 
 
 
 
 
 
 
 
 

6 
 
 
LISTA DE FIGURAS 
Figura 1 - Mapa de localização do município de São Thomé das Letras ....................... 11 
Figura 2 - Ortofoto de São Thomé das Letras, incluindo a sede do município, ao centro, 
e seu entorno com a Serra de São Tomé a nordeste (1968). ................................... 12 
Figura 3 - Mapa hipsométrico ........................................................................................ 15 
Figura 4 - Mapa de declividade ...................................................................................... 16 
Figura 5 - Mapa hidrográfico.......................................................................................... 17 
Figura 6 - Mapa da área de aplicação da Lei 11.428/2006 (Lei do bioma Mata Atlântica)
 ................................................................................................................................. 18 
Figura 7 - Tranformação dos níveis de cinza de uma cena ............................................ 20 
Figura 8 - Curva espectral da vegetação, da água e do solo ........................................... 20 
Figura 9 - Etapas do trabalho .......................................................................................... 24 
Figura 10 - Mapa de cobertura do solo do ano de 1984 no município de São Thomé das 
Letras ....................................................................................................................... 29 
Figura 11 - Mapa de cobertura do solo do ano de 2011 no município de São Thomé das 
Letras ....................................................................................................................... 30 
Figura 12 - Gráfico do quantitativo de perdas e ganhos das classes de cobertura do solo 
(%) ........................................................................................................................... 32 
Figura 13 – Gráfico da variação qualiquantitativa das classes de cobertura do solo (%)
 ................................................................................................................................. 32 
Figura 14 – Gráfico representando a contribuição da classe vegetação densa nas 
variações das classes (%) ........................................................................................ 33 
Figura 15 – Gráfico representando a contribuição da classe afloramento rochoso nas 
variações das classes (%) ........................................................................................ 33 
Figura 16 – Gráfico representando a contribuição da classe atividade agropastoril nas 
variações das classes (%) ........................................................................................ 33 
Figura 17 – Gráfico representando a contribuição da classe área urbana nas variações 
das classes (%) ........................................................................................................ 34 
Figura 18 – Gráfico representando a contribuição da classe mineração nas variações das 
classes (%) ............................................................................................................... 34 
Figura 19 – Gráfico representando a contribuição da classe reflorestamento nas 
variações das classes (%) ........................................................................................ 34 
Figura 20 - Mapa de mudanças das classes de cobertura do solo entre os anos de 1984 e 
2011 no município de São Thomé das Letras ......................................................... 37 
Figura 21 – Mapa de persistência das classes de cobertura do solo no município de São 
Thomé das Letras .................................................................................................... 38 
 
 
 

7 
 
 
LISTA DE QUADROS E TABELA 
Quadro 1 - Bandas do Sensor Thematic Mapper do satélite Landsat 5 e suas aplicações
 ................................................................................................................................. 22 
Quadro 2 - Chave de interpretação para mapeamento da cobertura do solo .................. 26 
Tabela 1 - Áreas das classes de cobertura do solo para o ano de 1984 e 2011 do 
município de São Thomé das Letras ....................................................................... 31 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

8 
 
 
LISTA DE ABREVIATURAS E SIGLAS 
IBGE – Instituto Brasileiro de Geografia e Estatística 
INPE - Instituto Nacional de Pesquisas Espaciais  
LCM - Land Change Modeler 
MAXVER - Máxima Verossimilhança 
PIB – Produto Interno Bruto 
SIG - Sistema de Informações Geográficas  
TM - Thematic Mapper 
 
 

9 
 
 
1. 
INTRODUÇÃO 
 
São Thomé das Letras é um município localizado ao sul do estado de Minas Gerais, 
distante 336 km da capital Belo Horizonte. Apresenta uma área de 369,52 km² e 
aproximadamente 6.655 habitantes distribuídos nas localidades de Sobradinho, 
Cantagalo, Pinhal, Caí, Correias e da sede urbana propriamente dita. 
O histórico do município está intimamente ligado à atividade de mineração. Os 
monumentos tombados no município foram construídos a partir da extração de 
quartzitos, denominado de pedra São Tomé, predominantes na região. A exploração do 
minério na região teve início no século XIX e em 1940 houve um crescimento acelerado 
por meio da utilização de explosivos para a exploração mineral, se consolidando como a 
principal fonte de renda da população local (RESENDE et al., 2009). 
O crescimento da atividade de extração mineral sem planejamento causou impactos 
adversos aos compartimentos ambientais e que, atualmente, se caracterizam como 
grandes passivos ambientais da região. Isso ocorre também porque a região tem grande 
potencial turístico visto o histórico de sua ocupação, seus monumentos, e as 
características dos aspectos ambientais em que está inserida (geológico, geomorfológico 
e paisagístico) acarretando em conflitos de interesse e uso do solo. 
O mapeamento da cobertura do solo é uma importante forma de conhecer os aspectos e 
impactos das atividades antrópicas sob o meio ambiente. Segundo Rosa (1990), este 
mapeamento é de fundamental importância para a compreensão dos padrões de 
organização do espaço. Dessa forma, o mapeamento da cobertura do solo permite 
avaliar, planejar e controlar espacialmente o uso sustentável e ocupação ordenada do 
meio ambiente. 
O Sistema de Informações Geográficas (SIG), a partir das geotecnologias disponíveis, 
pode auxiliar quanto à possibilidade de análise espacial de um determinado local, bem 
como uma análise multitemporal, para conhecer o padrão de expansão das atividades 
antrópicas e permitir um planejamento territorial de forma a orientar o desenvolvimento 
ordenado e controlado destas atividades. 

10 
 
 
O presente trabalho objetiva analisar, por meio de ferramentas de geoprocessamento, o 
desenvolvimento da cobertura do solo no município de São Thomé das Letras e 
contribuir com o trabalho de dissertação desenvolvido pela mestranda Camila Ragonezi 
Gomes Lopes sobre a modelagem do uso e conservação da geodiversidade no município 
de São Thomé das Letras. 
2. 
OBJETIVOS 
 
Objetivo geral:  
 Mapear e analisar a cobertura do solo do município de São Thomé das Letras 
nos anos de 1984 e 2011. 
Objetivos específicos: 
 Elaboração de dois mapas da cobertura do solo correspondente a cada época, por 
meio da utilização de imagens de satélite; 
 Estabelecimento de uma análise comparativa entre duas épocas distintas sobre a 
cobertura do solo; 
 Quantificação e análise das alterações de cada classe mapeada. 
3. 
CARACTERIZAÇÃO DA ÁREA DE ESTUDO 
 
3.1 Meio socioeconômico 
O município de São Thomé das Letras está localizado na região sul do estado de Minas 
Gerais, distando 336 km da capital mineira (Figura 1). Apresenta uma área de 369,52 
km² e possui 6.655 habitantes (IBGE, 2010) distribuídos nas localidades de Sobradinho, 
Cantagalo, Pinhal, Caí, Correias e da sede urbana. 

11 
 
 
 
Figura 1 - Mapa de localização do município de São Thomé das Letras 
O município surgiu aproximadamente em 1770, a partir da construção da Igreja Matriz 
próximo a uma gruta que influenciou a construção de residências em seu entorno. Sua 
localização era estratégica devido à proximidade e necessidade de abastecimento da 
Corte no Rio de Janeiro (RESENDE et al., 2009).  Ao se observar a arquitetura 
vernacular do município nota-se que desde a sua criação os habitantes têm explorado as 
pedras de quartzito presentes na região. 
A exploração comercial do minério na região teve início no final do século XIX até 
1940 e posteriormente houve um crescimento acelerado da mineração, por meio da 
utilização de explosivos para a exploração mineral, se consolidando ao longo do tempo 
como a principal fonte de renda da população local. 
É mostrada na Figura 2 uma ortofoto de 1968 que evidencia a ocupação predominante 
da atividade de mineração no município e a mancha urbana contida/inserida neste 
contexto. 
Embora o contexto histórico do município esteja relacionado à atividade de mineração, 
o turismo histórico, esotérico e ecológico vem se consolidando ao longo de décadas na 
região. São Thomé das Letras possui atrativos naturais, tais como cachoeiras, grutas e 

12 
 
 
mirantes, além de histórias/lendas esotéricas e misticismo quanto a manifestações de 
seres extraterrestres e objetos voadores não identificados, que atraem cada vez mais 
turistas para a região. 
 
Figura 2 - Ortofoto de São Thomé das Letras, incluindo a sede do município, ao centro, e seu 
entorno com a Serra de São Tomé a nordeste (1968). 
Fonte: Resende et al., 2009 
 
A pedra São Tomé, nome dado ao mineral quartzito explorado na região, tornou-se a 
principal fonte de renda e de desenvolvimento econômico da região. De acordo com 
Deschamps et. al. (2002), a economia do município está fundamentada em três 
atividades principais: o extrativismo mineral, que ocupa até 70% da população ativa, a 
agropecuária e o turismo.  

13 
 
 
A exploração da pedra São Tomé representa 90% do total das exportações minerais de 
quartzitos foliados, o que demonstra sua importância para a economia do município e 
do Estado. Entretanto, muitos anos de exploração intensiva, sem as devidas prevenções 
e controle resultou em uma grande quantidade de passivos ambientais e efeitos adversos 
ao meio ambiente. Pode ser observado na região a disposição desordenada do material 
estéril e rejeitos da lavra em talvegues e drenagens naturais, que foram assoreadas.  
Além dos fatores de ordem física e biótica causados pela extração de pedras (poluição 
atmosférica, sonora, assoreamento dos cursos d’água, impacto visual, supressão de 
vegetação e desestabilização do solo) o município encontra-se marcado pelo 
comprometimento das atividades turísticas e da identidade com o lugar.  
3.2 Meio físico 
O município apresenta o tipo climático tropical, mesotérmico brando, semiúmido 
(classificação adotada por Nimer). É caracterizado por grande influência orográfica, 
predomínio de temperaturas amenas durante quase todo o ano, com média anual 
variando entre 18°C e 19°C. De maneira geral, o verão é ameno e não apresenta 
temperatura média superior a 22º C, apesar da ocorrência de invernos com temperaturas 
variando entre 10º e 15º C. 
No que tange aos aspectos geológicos a região está inserida na Província da 
Mantiqueira, destacando o embasamento do Grupo Carrancas e Andrelândia (HASUI & 
OLIVEIRA, 1984 apud DESCHAMPS et al., 2002). 
De acordo com Ribeiro & Heilbron (1982) apud Deschamps et al. (2002), o Grupo 
Andrelândia é formado por quartzitos, filitos, xistos grafitosos, localmente com biotita, 
que muito se assemelha ao Grupo Carrancas, e biotita xistos, semelhantes à rocha do 
Grupo São João Del Rei.  
O Grupo Carrancas é dividido em Formação São Tomé das Letras e Formação 
Campestre. Este último é marcado pela alternância de quartzitos e filitos ou xisto 
grafitosos, já a Formação São Tomé das Letras tem como principal tipo litológico um 
quartzito micáceo formado, em sua essência, por quartzo, mica esverdeada, turmalina 
preta, magnetita, ilmeno-magnetita, e hematita (RIBEIRO & HEILBRON, 1982 apud 
DESCHAMPS et al., 2002).  

14 
 
 
Os tipos de solo predominantes na região são afloramentos de rochas + solos litólicos 
distróficos ou álicos de textura indiscriminada, associados com cambissolos álicos de 
textura argilosa, ambos A fraco substrato quartzito fase floresta subperenifólia relevo 
forte ondulado e montanhoso. Considerando que os solos são provenientes das rochas 
sedimentares quartzíticas, são rasos, arenosos, cascalhentos, com alto grau de 
rochosidade e com fertilidade natural geralmente baixa. 
O relevo da região é forte ondulado a montanhoso, caracterizado por um padrão 
montanhoso intercalado com terrenos arrasados (Figura 3). Segundo Souza et. al. 
(1999) os terrenos montanhosos são compostos por pacotes quartzíticos proterozóicos, 
representados pelas serras São Tomé das Letras e do Grotão, ou Cantagalo.  

15 
 
 
 
Figura 3 - Mapa hipsométrico 
Em relação à declividade, a Figura 4 mostra que as áreas junto às serras apresentam 
declividade maior que 20°. São áreas de preservação permanente as quais não devem 
ser ocupadas por atividades antrópicas. As declividades médias, de 10° a 20°, se 
concentram no sudeste do município e as declividades inferiores a 10° condizem com as 
planícies dos rios e com as áreas destinadas às atividades agropastoris. 

16 
 
 
 
Figura 4 - Mapa de declividade 
O município está inserido na bacia hidrográfica federal do rio Paraná e na bacia 
hidrográfica estadual do rio Grande.  

17 
 
 
 
Figura 5 - Mapa hidrográfico 
Conforme observado na Figura 5, o extremo nordeste do município pertence à sub-bacia 
do Alto Rio Grande, cuja principal drenagem é o ribeirão Lavarejo. A outra sub-bacia a 
qual pertence o município é a do Rio Verde, cujos principais corpos d’água são os 
ribeirões Vermelho e Cantagalo e os rios Caí e do Peixe, que drenam para oeste. 
3.3 Meio biótico 
O bioma presente na área de estudo é a Mata Atlântica, por meio da fitofisionomia 
Floresta Estacional Semidecidual e Floresta Ombrófila Mista. Há ocorrência do bioma 
Cerrado por meio da fitofisionomia Savana (Figura 6). Contudo, de acordo com 
Deschamps et. al. (2002) a formação vegetal original se encontra bastante 
descaracterizada, restando fragmentos florestais. 

18 
 
 
 
Figura 6 - Mapa da área de aplicação da Lei 11.428/2006 (Lei do bioma Mata Atlântica) 
De acordo com Lopes (2013), compõem a cobertura da área de estudo manchas de 
Campo Cerrado, ou Savana Gramíneo-Lenhosa, pastagens associadas com culturas 
permanentes, como o café, culturas anuais, como o milho e o feijão, e afloramentos 
rochosos associado ao Campo Rupestre. 
Há no município também a Área de Proteção Ambiental municipal de São Tomé, 
conforme Decreto Estadual nº 003 de 29 janeiro de 2003, que ainda não possui um 
plano de manejo, bem como está em processo de valorização através de sua validação 
no Plano Diretor do município, que por sua vez está sendo elaborado.  

19 
 
 
4. 
REVISÃO BIBLIOGRÁFICA 
Segundo Jensen (2009) o termo uso da terra refere-se ao modo como a terra é usada 
pelos seres humanos, já a cobertura do solo, por sua vez, é definida como os materiais 
biofísicos encontrados sob a superfície terrestre. 
O mapeamento da cobertura do solo torna-se uma atividade de grande valia quando se 
quer ter uma visão geral dos aspectos que ocorrem em uma determinada região e quais 
os impactos associados à eles. As ferramentas disponibilizadas pelas geotecnologias 
permitem a realização de análises mais complexas, que associam diversas variáveis do 
ambiente, possibilitando ao homem o estabelecimento de medidas para o planejamento 
do uso da terra. Todavia, como ressaltado por Rosa (1990), cada classificação é 
realizada para atender a determinadas necessidades do usuário e adaptadas à região, não 
existindo, portanto, um modelo único e ideal. 
A modificação da paisagem pela atividade antrópica pode ser acompanhada e 
quantificada pela análise e processamento digital de imagens. A partir da interpretação 
de imagens de satélite, a cobertura do solo, como, por exemplo, pelas atividades de 
mineração, referente a duas datas distintas, pode ser delimitada e calculada (área), e 
definida ainda a taxa de expansão das atividades (FLORENZANO, 2002). 
O processamento digital de imagens consiste na combinação de bandas espectrais, 
combinações de imagens de uma mesma banda em diferentes datas, ou imagens de 
diferentes sensores, gerando composições coloridas que permitem a extração de 
informações (NOVO, 2008). 
As atividades de processamento digital podem ser estruturadas em três etapas 
independentes: pré-processamento, que consiste no tratamento inicial dos dados brutos, 
tais como calibração radiométrica, correção de distorções geométricas e remoção de 
ruídos; realce, que consiste na manipulação do contraste; e classificação, que consiste na 
técnica de atribuição de informação a um conjunto de pixels (NOVO, 2008). 
No que tange à etapa determinada como realce, de acordo com Novo (1992), as 
manipulações de contraste visam facilitar a discriminação visual de características da 
cena com baixo contraste e enfatizar alguma característica de interesse para uma 
aplicação específica. Esta manipulação é realizada por meio da análise do histograma 

20 
 
 
com a frequência dos níveis de cinza de cada canal espectral, conforme indicado na 
Figura 7. 
 
Figura 7 - Tranformação dos níveis de cinza de uma cena 
Fonte: Schowengerdt, 1983 apud Novo, 1992. 
Na etapa de classificação, a base para a determinação e classificação da cobertura do 
solo no processamento digital de imagens, conforme Florenzano (2002), é a energia 
refletida pelos objetos/elementos em proporções que variam de acordo com o 
comprimento de onda (Figura 8). 
 
Figura 8 - Curva espectral da vegetação, da água e do solo 
Fonte: Florenzano, 2002. 

21 
 
 
Portanto, para classificação da cobertura do solo de uma determinada região faz-se 
necessário o conhecimento prévio do comportamento espectral dos objetos/elementos a 
que se deseja mapear. 
Segundo Filho (2000) a interpretação visual dos dados digitais visa identificar feições e 
os seus significados de forma a produzir mapas temáticos. Este processo pode ser 
aplicado às diversas áreas do conhecimento, como na determinação/conhecimento da 
cobertura do solo de uma região, possibilitando uma análise ampla e a detecção de 
objetos e fenômenos não perceptíveis pela visão humana. 
Para este processo de interpretação é de extrema importância possuir conhecimento 
sobre a tecnologia utilizada, compreender o comportamento espectral dos objetos 
analisados e conhecer a área mapeada (FILHO, 2000). 
De acordo com Florenzano (2002), o processo de interpretação de imagens consiste na 
identificação de objetos e atribuição de significados a esses objetos. Os elementos 
básicos para este processo, tais como tonalidade/cor, textura, tamanho, forma, sombra, 
altura, padrão e localização, permitem a análise e extração das informações na imagem. 
Outro fator de destaque no processo de interpretação visual dos dados se refere a 
seleção das bandas. Segundo Filho (2000) a seleção das bandas espectrais que comporá 
os estudos dependerá diretamente dos objetivos do estudo/análise. De forma a 
exemplificar, é apresentado no Quadro 1 as principais aplicações das bandas espectrais 
do sensor Thematic Mapper a bordo do satélite Landsat 5. 

22 
 
 
 
Quadro 1 - Bandas do Sensor Thematic Mapper do satélite Landsat 5 e suas aplicações 
Fonte: Filho, 2000 
As técnicas de classificação digital de imagens, segundo Novo (1992), se configuram 
como um processo de decisão para que o computador possa atribuir certo conjunto de 
pontos da imagem (pixels) a uma determinada classe. O processo de classificação 
digital de imagens pode ser subdividido em duas categorias: Classificação 
unidimensional e Classificação multiespectral. A primeira técnica, mais simples, 
consiste na divisão do intervalo total de níveis de cinza, de uma dada faixa espectral, em 
um certo número de classes. Já a segunda técnica é dividida em três conjuntos: 
classificação 
supervisionada, 
classificação 
não-supervisionada 
e 
técnicas 
de 
classificação híbrida. 
A classificação supervisionada é caracterizada por um processo onde o analista está em 
constante interação com o sistema. O analista define a amostragem de classes de 
interesse as quais são selecionadas por meio de um conhecimento prático ou teórico. 
Um ponto que merece destaque, de acordo com diversos autores, é a seleção de 
amostras. Este processo necessita de bastante atenção tendo em vista o comportamento 
espectral dos objetos que podem, às vezes, ser a mesma para classes distintas (NOVO, 
1992). 
Para as classificações não-supervisionadas o analista tem pouco controle sobre a 
separação das classes, nas quais os pixels são agrupados naturalmente considerando sua 
distribuição num espaço de atributos de N dimensões. 

23 
 
 
A partir dos resultados da classificação, uma infinidade de análises pode ser realizada. 
Umas das mais difundidas atualmente é a quantificação das classes e modelos de 
predição por meio da utilização do software Land Change Modeler – LCM. Este 
software que pode ser acoplado a plataforma do ArcGis ou Idrisi, foi desenvolvido por 
uma equipe do laboratório de processamento Clark Labs da Universidade Clark, no 
estado de Massachusetts (EUA) objetivando permitir análises qualiquantitativas em 
torno das alterações da cobertura do solo. Segundo Luiz (2014) o software dispõe de 
ferramentas para mensurar as áreas de mudança, persistência e de construir cenários 
futuros a partir da análise das informações de uso e ocupação do solo de diferentes 
datas. 
Para compreensão da dinâmica da mudança na cobertura da terra o software LCM 
permite a elaboração de mapas e gráficos que mostram as perdas, os ganhos, as 
mudanças e persistência das classes definidas. Permite também a construção de 
variáveis explanatórias a partir da análise das mudanças que, por sua vez, subsidiam a 
construção de cenários futuros. 
5. 
MATERIAIS E MÉTODOS 
 
Para realização da análise multitemporal da cobertura do solo do município de São 
Thomé das Letras foram selecionadas duas imagens do satélite Landsat 5 (TM) nos anos 
de 1984 e 2011. Os anos foram selecionados considerando-se o histórico de ocupação 
do município, e principalmente a viabilidade de tratamento das imagens para a 
realização do trabalho. Ambas as imagens selecionadas foram do mês julho objetivando 
imagens mais limpas e com menos interferência climática. 
O fluxograma da Figura 9 mostra as etapas adotadas para a execução do trabalho. 

24 
 
 
 
Figura 9 - Etapas do trabalho 
 
5.1 Etapa 1 – Obtenção das imagens Landsat 5 TM 
As imagens são disponibilizadas gratuitamente pelo Instituto Nacional de Pesquisas 
Espaciais - INPE, em resolução espacial de 30 metros (exceto a banda 6 com 120 
metros). O sensor Thematic Mapper (TM) do satélite Landsat 5 possui sete bandas 
espectrais, onde cada uma representa uma faixa do espectro eletromagnético captado 
pelo sensor do satélite. O satélite, lançado em 01 de março de 1984, foi programado 
para fazer o imageamento da superfície terrestre produzindo imagens com 185 km de 
largura do terreno e revisitando uma mesma área num intervalo de 16 dias. 
Considerando as aplicações possíveis das bandas disponibilizadas pelo satélite Landsat 
5, conforme item 4, foram selecionadas as bandas 3, 4 e 5, devido a estas cobrirem o 
comportamento espectral da vegetação e do uso do solo. 
5.2 Etapa 2 - Análise e tratamento das imagens 
Para o tratamento e classificação das imagens foi utilizado o software livre denominado 
Spring 5.2.6. Este software foi desenvolvido pelo INPE e outros parceiros com o 
objetivo de construir um sistema de informações geográficas gratuito, acessível e 
unificado para diversas aplicações. O Spring é um sistema de informações geográficas 
Etapa 1: Obtenção 
das imagens 
Landsat 5 TM 
Etapa 2: Análise e 
tratamento das 
imagens 
Etapa 3: Definição 
das classes de 
cobertura do solo - 
Chaves de 
interpretação 
Etapa 4: Coleta de 
amostras 
Etapa 5: 
Classificação das 
imagens  
Etapa 6: 
Quantificação e 
análise das 
alterações  

25 
 
 
com funções de processamento de imagens, análise espacial, modelagem numérica de 
terreno e consulta a banco de dados espaciais (INPE, 2012). 
5.3 Etapa 3 - Definição das classes de cobertura do solo (Chaves de interpretação) 
Após a obtenção das imagens selecionou-se as bandas de interesse: bandas 3, 4 e 5, 
onde as bandas 3 (faixa da luz vermelha), 4 (infravermelho próximo) e 5 (infravermelho 
médio) foram associadas às cores azul, verde e vermelha respectivamente. Por meio de 
análise visual das imagens, definiu-se as chaves de interpretação, ou seja, as classes de 
cobertura do solo a serem mapeadas. 
As chaves de interpretação, que consistem nas feições identificadas e determinação dos 
seus significados por meio da fotoleitura, fotoanálise e fotointerpretação, foram 
definidas conforme mostrado no Quadro 2. 
Cobertura do solo 
Tonalidade/ Cor 
Textura 
Forma 
Atividades agropastoris 
Roxo claro/escuro 
 
Lisa 
Regular 
Área Urbana 
Lilás esbranquiçado 
 
Rugosa 
Regular 
Mineração 
Branco 
 
Lisa 
Irregular 
Água 
Preto 
 
Lisa 
Irregular 
Afloramento rochoso e 
campo rupestre 
Roxo escuro 
 
Lisa 
Irregular 

26 
 
 
Cobertura do solo 
Tonalidade/ Cor 
Textura 
Forma 
Reflorestamento 
Verde claro 
 
Lisa 
Regular 
Vegetação densa 
Verde escuro 
 
Rugosa 
Irregular 
Quadro 2 - Chave de interpretação para mapeamento da cobertura do solo 
Cabe ressaltar que para a imagem do ano de 1984, a partir de análise prévia, foram 
definidas/utilizadas todas as classes supramencionadas, exceto “Reflorestamento”, 
tendo em vista a não existência desse tipo de atividade no município à época. 
A composição de cor falsa RBG 543 permitiu uma melhor visualização das chaves de 
interpretação definidas, tendo em vista a possibilidade de destacar diferentes elementos 
na imagem, já que os elementos refletem os espectros com intensidades diferentes.  
Aplicou-se o contraste, que consiste na distribuição dos níveis de cinza em todo 
intervalo possível do histograma, obtendo-se assim uma imagem mais clara e viável 
para visualização humana e consequentemente para a obtenção das amostras das classes 
na etapa de classificação da imagem.  
Além dos procedimentos de preparação para a classificação, para a imagem do ano de 
1984 foi necessária aplicar a correção geométrica. Segundo Melo et. al. (2004) as 
imagens produzidas por sensores remotos apresentam uma série de distorções espaciais, 
portanto, sem precisão cartográfica quanto ao posicionamento dos objetos, superfícies 
ou fenômenos nelas representados. As principais fontes de erros geométricos, conforme 
Novo (2008), são: a) o movimento de rotação da terra durante o processo de aquisição 
de imagens; b) a velocidade de “varredura” finita; c) o amplo campo de visada de 
alguns sensores; d) a curvatura da terra; e) variações na posição da plataforma de 
aquisição; e) efeitos panorâmicos relacionados à geometria da imagem. 

27 
 
 
A correção geométrica, de acordo com Mather (1987), tem como objetivo recuperar a 
qualidade geométrica da cena, de tal modo que os dados possuam características de 
escala e projeção próprias de mapas. 
A correção foi realizada, utilizando-se o comando Auto Ajust disponível na ferramenta 
Georreferencing 
do 
software 
ArcGis 
10.2. 
Esta 
ferramenta 
realiza 
o 
georreferenciamento do raster da seguinte forma: por meio das assinaturas espectrais de 
um raster de referência, o sistema cria links de seu conjunto de dados raster não 
referenciado para o conjunto referenciado. 
5.4 Etapa 4 - Coleta de amostras 
Posteriormente, foi realizada a coleta de amostras da imagem, visando associar 
determinados pixels a uma classe previamente definida. Coletada as amostras, realizou-
se sua análise para verificação do atendimento ao valor mínimo de aceitação e 
desempenho geral estipulado de 95%. Este processo é parte integrante do método 
utilizado: Classificação Supervisionada por Pixel por meio da utilização da técnica 
denominada de Máxima Verossimilhança (MAXVER). 
5.5 Etapa 5 - Classificação das imagens 
De acordo com Rosa (1990) o algoritmo de classificação MAXVER consiste em 
classificar a imagem, ponto a ponto, usando o critério de máxima verossimilhança a 
partir de classes fornecidas pelo usuário. Este tipo de método reconhece padrões e 
objetos homogêneos o qual, por meio da classificação “pixel a pixel”, utiliza a 
informação espectral isolada definindo regiões homogêneas e resultando em uma 
imagem constituída de pixels classificados por cores. A técnica MAXVER utilizada 
para o processamento da imagem considera a ponderação das distâncias entre médias 
dos níveis digitais das classes, utilizando parâmetros estatísticos (INPE, 2010). 
Esse método foi utilizado por ser considerado um dos mais eficientes classificadores e, 
consequentemente, o mais utilizado.  
Após a classificação da imagem, foi realizado o procedimento de pós-classificação que 
consiste na eliminação de ruídos da classificação realizada, onde possíveis pixels que 

28 
 
 
foram classificados erroneamente sejam corrigidos por meio da edição matricial 
disponível no software. 
A partir da conclusão dos procedimentos metodológicos de classificação, foi realizada a 
conversão do arquivo em formato matricial para vetor (shapefile) visando finalizar a 
elaboração do mapa no software ArcGis 9.3. 
Com a shape criada realizou-se seu recorte a partir do limite municipal de São Thomé 
das Letras e o cálculo das áreas das classes de cobertura (percentagem) de forma a 
verificar a representatividade de cada uma em relação à área de estudo. 
5.6 Etapa 6 - Quantificação e análise das alterações 
A partir do mapeamento das classes foi realizada análise quantitativa das alterações 
observadas no solo a partir do software Land Change Modeler - LCM.  
Para que isto fosse possível, necessitou-se converter a shape resultante do 
processamento de cobertura do solo para uma extensão conhecida do Idrisi, que neste 
caso foi o ASCII. Convertido, os arquivos de cada ano foram inseridos no Idrisi para 
que pudessem ser tratados e posteriormente processados na ferramenta LCM. 
Uma vez os dados inseridos no LCM, foram gerados gráficos e mapas que permitiram 
diversos cruzamentos de dados e consequentemente uma análise mais aprofundada e 
assertiva da dinâmica das mudanças ocorridas entre os anos estudados. 
6. 
RESULTADOS E DISCUSSÕES 
Processado os dados foi possível elaborar o mapa de cobertura do solo nos anos de 1984 
e 2011 e quantificar cada classe definida. Os resultados são mostrados na Figura 10 e 
Figura 11. 
Para o ano de 1984 o desempenho geral de classificação a partir das amostras de 
aquisição foi de 96,58% e a confusão média foi de 3,42%. Para o ano de 2011 o 
desempenho geral de classificação a partir das amostras de aquisição foi de 95,75% e a 
confusão média foi de 4,25%. Ambas as matrizes de confusão são apresentadas no 
Apêndice A. 

29 
 
 
 
 
Figura 10 - Mapa de cobertura do solo do ano de 1984 no município de São Thomé das Letras 

30 
 
 
 
Figura 11 - Mapa de cobertura do solo do ano de 2011 no município de São Thomé das Letras 
 

31 
 
 
As quantificações de cada classe de cobertura do solo em quilômetros quadrados bem 
como sua representatividade em porcentagem são mostradas na Tabela 1. 
Tabela 1 - Áreas das classes de cobertura do solo para o ano de 1984 e 2011 do município de 
São Thomé das Letras 
Classe de cobertura do solo 
Área 
1984 
2011 
km² 
% 
km² 
% 
Água 
0,301 
0,082% 
0,008 
0,002% 
Área Urbana 
0,113 
0,031% 
0,488 
0,133% 
Campo rupestre/Afloramento rochoso 
87,011 
23,665% 
21,520 
5,853% 
Mineração 
0,608 
0,165% 
3,737 
1,016% 
Atividade agropastoril 
150,113 
40,827% 
273,807 
74,468% 
Reflorestamento 
0,000 
0,000% 
4,113 
1,119% 
Vegetação densa 
129,538 
35,231% 
64,010 
17,409% 
Total Geral 
367,6829 
100% 
367,6829 
100% 
 
Analisando os dados apresentados, observa-se que no ano de 1984 há um grande 
predomínio das atividades agropastoris (40,82%), porém a área de vegetação densa 
juntamente com o afloramento rochoso (58,89%) mostra uma preservação do meio 
ambiente, superior ao percentual de ocupação por atividades antrópicas.  
A mineração não apresenta percentual de ocupação significativo em uma análise global, 
porém é possível observar sua distribuição geográfica na Serra São Tomé, o que 
demonstra popularidade e aumento da atividade à época.  
Para o ano de 2011 observa-se o surgimento da classe reflorestamento ao sul do 
município, representando a instalação de outras fontes de renda. Há um crescimento 
exponencial da atividade de mineração e um predomínio das atividades agropastoris, 
que substituem principalmente as áreas de vegetação densa. 
A mineração cresce, substituindo áreas de afloramento rochoso/campo rupestre 
conforme esperado, visto que são os locais de presença do mineral quartzito. Observa-se 
um conflito entre as áreas de expansão da atividade minerária e da área urbana. A área 
urbana cresce em meio à mineração, caracterizando um conflito deste tipo de ocupação. 

32 
 
 
Com a utilização do software Land Change Modeler foi possível visualizar 
quantitativamente e de que forma ocorreram as alterações da cobertura, sendo possível 
determinar sobre o padrão de expansão de cada classe. 
Na Figura 12 o gráfico mostra que a classe atividade agropastoril foi a atividade que 
mais se expandiu no município, representando um crescimento favorável ao Produto 
Interno Bruto – PIB e se estabelecendo como uma das atividades de maior rentabilidade, 
atrás somente do setor de serviços. 
As classes de vegetação densa e campo rupestre/afloramento rochoso sofreram com 
uma maior perda de área. 
 
Figura 12 - Gráfico do quantitativo de perdas e ganhos das classes de cobertura do solo (%) 
 
Analisando o gráfico da variação qualiquantitativa das classes mostrado na Figura 13, 
observa-se que, de forma geral, as classes de vegetação densa e campo 
rupestre/afloramento rochoso foram as que apresentaram maior perda de área. Já as 
atividades agropastoris, mineração e reflorestamento apresentaram um ganho na 
representatividade de ocupação de área. 
 
Figura 13 – Gráfico da variação qualiquantitativa das classes de cobertura do solo (%) 
 

33 
 
 
Em uma análise mais detalhada, são apresentados os gráficos da contribuição de cada 
classe na variação total das classes. Estes gráficos permitem verificar padrões de 
comportamento, a dinâmica de alteração, e possibilitam visualizar sob qual classe as 
alterações ocorrem e de quais ocorrem.  
 
Figura 14 – Gráfico representando a contribuição da classe vegetação densa nas variações das 
classes (%) 
 
 
Figura 15 – Gráfico representando a contribuição da classe afloramento rochoso nas variações 
das classes (%) 
 
 
Figura 16 – Gráfico representando a contribuição da classe atividade agropastoril nas variações 
das classes (%) 
 

34 
 
 
 
Figura 17 – Gráfico representando a contribuição da classe área urbana nas variações das classes 
(%) 
 
 
Figura 18 – Gráfico representando a contribuição da classe mineração nas variações das classes 
(%) 
 
 
Figura 19 – Gráfico representando a contribuição da classe reflorestamento nas variações das 
classes (%) 
 
Observa-se nos dados apresentados (Figura 14 e Figura 15) que a vegetação densa e 
campo rupestre/afloramento rochoso são ocupadas, principalmente, pela atividade 
agropastoril. Para a classe campo rupestre/afloramento rochoso ainda há a perda de área 
para a ocupação da mineração e da área urbana. 

35 
 
 
A atividade agropastoril é a atividade de maior impacto no município e mais invasora 
no que tange à ocupação das áreas de cobertura do solo (Figura 16). Porém, apesar de 
apresentar um predomínio na ocupação, a atividade de mineração é a que maior 
representa impactos adversos e irreversíveis ao meio ambiente na área do município. 
O aglomerado urbano cresce sob as áreas de campo rupestre/afloramento rochoso, 
mineração e atividade agropastoril (Figura 17). Nota-se que sua expansão ocorre em 
proximidade as atividades de mineração, caracterizando o evidente conflito do uso do 
solo, mineração versus turismo ecológico. 
Na Figura 18 é mostrado que a mineração ocupa as áreas de afloramento rochoso/campo 
rupestre e área de atividade agropastoril, perdendo área somente para a ocupação 
urbana. 
Fato novo identifica-se no gráfico mostrado na Figura 19 com a introdução de nova 
classe: o reflorestamento. Esta atividade surge ocupando as áreas de atividades 
agropastoris, afloramento rochoso/campo rupestre e vegetação densa. 
Com o objetivo de visualizar as mudanças supracitadas, elaborou-se o mapa de 
mudanças mostrado na Figura 20.  Apesar de trazer muitas informações, o que pode 
causar dificuldade em sua análise, o mapa permite visualizar espacialmente as 
alterações da cobertura do solo. 
No mapa se destaca a perda da vegetação densa para a ocupação de outras atividades 
como a agropastoril, área urbana, mineração e reflorestamento, devido a sua maior 
distribuição geográfica. É possível identificar também a expansão urbana sob a 
mineração e afloramento rochoso/campo rupestre. 
Nota-se também as áreas de reflorestamento que se destacam no meio devido à sua 
dimensão e forma. 
Já na Figura 21 é mostrado o mapa de persistência, onde é possível visualizar 
espacialmente as áreas que não sofreram alterações, ou seja, permaneceram desde o ano 
de 1984. 

36 
 
 
Nota-se que ainda há áreas de campo rupestre/afloramento rochoso e vegetação densa 
intactas, e que preservam os recursos naturais da região e aumentam o potencial 
turístico ecológico. 
Observa-se que as mudanças que ocorreram ao longo do tempo se concentram na região 
central do município, exatamente onde se localizam predominantemente as atividades 
de mineração e o aglomerado urbano. 
 

37 
 
 
 
Figura 20 - Mapa de mudanças das classes de cobertura do solo entre os anos de 1984 e 2011 no município de São Thomé das Letras 

38 
 
 
 
Figura 21 – Mapa de persistência das classes de cobertura do solo no município de São Thomé 
das Letras 
  
 

39 
 
 
7. 
CONCLUSÕES 
 
Analisando os resultados obtidos a partir do processamento das imagens e elaboração 
dos mapas de cobertura do solo do município São Thomé das Letras para os anos de 
1984 e 2011 foi possível observar mudanças significativas para as classes de cobertura 
estabelecidas, principalmente mineração, área urbana e vegetação densa. 
Os resultados obtidos pós-processamento no LCM permitiram verificar que a classe de 
cobertura mineração expandiu predominantemente sobre campo rupestre/afloramento 
rochoso e que a classe atividade agropastoril e área urbana aumentou sua taxa de 
cobertura, sendo esta última sob a mineração. 
A atividade agropastoril ocupa grande extensão do município e se caracteriza como a 
fonte de renda principal no que tange ao PIB, entretanto, a atividade de mineração, 
apesar de ocupar uma área muito inferior, apresenta maior contribuição de arrecadação 
municipal e estadual e de impactos adversos significativos ao meio ambiente. 
Conclui-se que há necessidade de regulamentar e fiscalizar as atividades de mineração e 
agropastoril. Essas atividades de grande impacto negativo ambiental estão se expandido 
no município sem o devido planejamento e controle. A região possui alto potencial para 
o turismo ecológico e há ainda um percentual significativo de vegetação preservada. O 
relevo fortemente ondulado na região central do município auxilia na preservação dos 
recursos naturais. Portanto, considerando a riqueza econômica e ambiental, faz-se 
urgente a conclusão do Plano Diretor e regularização ambiental das atividades 
econômicas. 
Ressalta-se que para um refinamento dos resultados e de sua confiabilidade recomenda-
se a realização de visita a campo objetivando a validação do mapeamento.  
O presente trabalho poderá ser expandido aplicando técnicas de modelagem dinâmica 
do uso e cobertura do solo, através de outros recursos disponíveis na plataforma LCM. 
 
 
 
 

40 
 
 
8. 
BIBLIOGRAFIA 
 
DESCHAMPS, D. et al. (2002). Controle Ambiental na Mineração de Quartzito – 
Pedra São Tomé. Belo Horizonte: Projeto Minas Ambiente: 204 p. 
FILHO, B. S. S. (2000). Interpretação das imagens da terra. Belo Horizonte: 
Universidade Federal de Mines Gerias: 17 p. 
FLORENZANO, T, G. (2002). Imagens de satélite para estudos ambientais. São 
Paulo: Oficina de Textos: 97 p. 
JENSEN, R. J. Sensoriamento remoto do ambiente: uma perspectiva em recursos 
terrestres. São José dos Campos: Parêntese: 598 p. 
LOPES, C. R. G. (2014). Modelagem do uso e conservação dos recursos da 
geodiversidade no município de São Thomé das Letras - MG, Universidade Federal 
de Minas Gerais. Qualificação para Mestrado: 76p. 
LUIZ, C. H. P. Modelagem da cobertura da terra e análise da influência do 
reflorestamento na transformação da paisagem: Bacia do Rio Piracicapa e Região 
Metropolitana do Vale do Aço. Universidade Federal de Minas Gerais. Dissertação de 
Mestrado: 140 p. 
MATHER, P.M. (1987). Computer processing of remotely-sensed images, John 
Wiley & Sons. 
MELO, I. D. F. (2004). Aspectos da correção geométrica de imagens orbitais,  
Universidade Federal de Pernambuco: Recife 1-9p. 
NOVO, E. M. L. M. (1992). Sensoriamento Remoto: princípios e aplicações. São 
Paulo: Edgard Blücher. 2ª Edição: 308 p. 
NOVO, E. M. L. M. (2008). Sensoriamento Remoto: princípios e aplicações. São 
Paulo: Edgard Blücher. 3ª Edição: 363 p. 
RESENDE, M. A. P. et al. (2009). Pedra São Tomé: Valoração regional por meio da 
revitalização da paisagem e da identidade cultural em São Thomé das Letras, 
Universidade Federal de Minas Gerais. Projeto FAPEMIG: 776p. 
ROSA, R. (1990). Introdução ao Sensoriamento Remoto. Ed. da Universidade 
Federal de Uberlândia. Uberlândia: 136p. 
SOUZA, G. G.; SANTOS, M. R. C. dos; COSTA, A. G. (1999). Quartzitos de São Tomé das 
Letras: enquadramento geológico, caracterização tecnológica e análise ambiental. 
Universidade Federal de Minas Gerais: 129 p. 
 
 
 

41 
 
 
9. 
APÊNDICE 
 
APÊNCIDE A – Matriz de confusão 
ANO 1984 
 
 
 
 
 
 
 
 
 
 
 
 

42 
 
 
ANO 2011 
 
 
