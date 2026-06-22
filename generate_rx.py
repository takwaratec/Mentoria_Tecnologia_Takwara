import re
import json
import datetime

# Administrators list
admins = ["Maré Educação", "Vanessa Fleig", "Suporte", "Raízes", "Marcus", "Myca"]

# State DDD mapping
ddd_to_state = {
    "11": "SP", "12": "SP", "13": "SP", "14": "SP", "15": "SP", "16": "SP", "17": "SP", "18": "SP", "19": "SP",
    "21": "RJ", "22": "RJ", "24": "RJ",
    "27": "ES", "28": "ES",
    "31": "MG", "32": "MG", "33": "MG", "34": "MG", "35": "MG", "37": "MG", "38": "MG",
    "41": "PR", "42": "PR", "43": "PR", "44": "PR", "45": "PR", "46": "PR",
    "47": "SC", "48": "SC", "49": "SC",
    "51": "RS", "53": "RS", "54": "RS", "55": "RS",
    "61": "DF",
    "62": "GO", "64": "GO",
    "63": "TO",
    "65": "MT", "66": "MT",
    "67": "MS",
    "68": "AC",
    "69": "RO",
    "71": "BA", "73": "BA", "74": "BA", "75": "BA", "77": "BA",
    "79": "SE",
    "81": "PE", "82": "AL", "83": "PB", "84": "RN", "85": "CE", "86": "PI", "87": "PE", "88": "CE", "89": "PI",
    "91": "PA", "92": "AM", "93": "PA", "94": "PA", "95": "RR", "96": "AP", "97": "AM", "98": "MA", "99": "MA"
}

state_names = {
    "SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Minas Gerais", "PR": "Paraná",
    "SC": "Santa Catarina", "RS": "Rio Grande do Sul", "BA": "Bahia", "CE": "Ceará",
    "DF": "Distrito Federal", "SE": "Sergipe", "PE": "Pernambuco", "ES": "Espírito Santo",
    "AL": "Alagoas", "AM": "Amazonas", "RN": "Rio Grande do Norte", "MT": "Mato Grosso",
    "PB": "Paraíba", "GO": "Goiás"
}

# Pre-known explicit locations from active profiles
explicit_states = {
    "Fabio Takwara": "SP", "Marcello Pedro": "RJ", "Michelle Santiago": "SP", "Momento Bela": "SP", "⚡Vânia Távora": "CE",
    "Mandy Bettega 🪷": "SC", "Luciana": "SC", "Fabiane Ji": "BA", "Andréa Claudini ⚡": "PR", "Arlete D'arc": "SP",
    "Lucas Vargas": "RS", "Grupo Tech Lucas Vargas": "RS", "Ju Almeida": "SP", "Monica Marques": "RJ", "Sandra": "SP",
    "Luiza Lyra": "BA", "Rogê Biuzo": "RJ", "Carla Gonçalves": "RJ", "Theo Oliveira": "SP", "Amanda Cardoso": "SE",
    "Arthur Martins": "AL", "Diego Americo": "SP", "Bela Giannini": "MG", "Karime Neder": "RJ", "Nandà Luccâs": "SP",
    "Daniela Teixeira": "SP", "Nathália Pantaleão": "DF", "Maria Regina": "RS", "Rê": "RS", "Ynglety Barros": "AM",
    "Karla Barreiros": "RJ", "Cínthya Alcântara": "SC", "Lari Gaigher": "SP", "Fabiana Fortunato": "MG", "Ilana Lewinsohn": "BA",
    "Evelen Tomaz": "BA", "Evelen Tomaz 🤎": "BA", "Simone Hykavei": "RJ", "Simone Inês": "RJ", "Simone Tamega": "SP", "Maíra Salomão": "SP",
    "Joyce Muzy": "SP", "Fernanda Moraes": "RS", "Elen Rezende": "MG", "Elen Rezende ✨": "MG", "Prem Karima": "RJ",
    "Eron Villar": "PE", "Destrave sua Escrita": "PE", "Jordana Mol": "MG", "Wanúbia": "MG", "Ricardo Arruda": "CE",
    "Joslaene Santos": "SC", "Adriana Barbetta": "PR", "Carolina Bernardo": "DF", "Kaua": "RJ", "ka.consciente": "RJ",
    "Daniela Carneiro": "PR", "Tais Jardim": "CE", "Marisa": "SP", "Milena": "RS", "Tiago Campetti": "PR", "Alex Maciel": "Não Identificado",
    "Ohanna Pacheco": "SC", "Adriana Gaia": "Não Identificado", "Marcia Penna de Castro": "SP", "Tatiana Fávaro Lima": "PR",
    "Carina Vieirat": "RJ", "Dra. Ana Brisolla": "SP", "Raquel Peres": "Não Identificado", "Psi Nara Barreto": "RJ",
    "Marcia Andrade": "SP", "Hernani Albuquerque": "Não Identificado", "Su 😁✨️": "Não Identificado", "Gabriel Martens": "RJ",
    "Si Briganti": "SP",
    "Luiz Eduardo (Eduardo Rocha)": "PB",
    "João Lima": "PR",
    "Helena Woellner": "PR",
    "Manoela Couto": "SP",
    "Elaine Gama": "PR",
    "Micheline": "RJ",
    "Cristiane Monteiro (Instituto FHE)": "SP",
    "Cristina Maria": "SC",
    "Deusilene Leão": "GO",
    "Ludmilla Azevedo": "SP",
    "Elaine Bazilio": "SP",
    "Elany Almeida": "DF",
    "Cris Sathler": "RJ",
    "Karol Marinho": "RN",
    "Dr Douglas Lima": "SC",
    "Kelvin Moreira (Tiziu Capoeira)": "SP",
    "Andrea Santos (ARS Terapias)": "SP"
}

# Nichos for active members
active_niches = {
    "Fabio Takwara": "Inovação Técnica de Base & Sustentabilidade",
    "Marcello Pedro": "Saúde Integrativa, Corpo & Movimento",
    "Michelle Santiago": "Liderança / Organização Corporativa",
    "Momento Bela": "Cuidado Parental & Família",
    "⚡Vânia Távora": "Outros / Em estruturação",
    "Renata Cardinali": "Cuidado Parental & Família",
    "Mandy Bettega 🪷": "Cuidado Parental & Família",
    "Luciana": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Fabiane Ji": "Saúde Integrativa, Corpo & Movimento",
    "Ana Carolina Mattoso": "Educação & Mentoria Acadêmica",
    "Patrícia Bertachini Bissetti": "Educação & Mentoria Acadêmica",
    "Andréa Claudini ⚡": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Adriana Gaia": "Vendas B2B & Consultoria PME",
    "Priscila Kalil": "Liderança / Organização Corporativa",
    "Arlete D'arc": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Lucas Vargas": "Vendas B2B & Consultoria PME",
    "Grupo Tech Lucas Vargas": "Vendas B2B & Consultoria PME",
    "Ju Almeida": "Liderança / Organização Corporativa",
    "Monica Marques": "Cuidado Parental & Família",
    "Daniela Freitas": "Liderança / Organização Corporativa",
    "Sandra": "Saúde Integrativa, Corpo & Movimento",
    "Luiza Lyra": "Liderança / Organização Corporativa",
    "Ana Simões": "Saúde Integrativa, Corpo & Movimento",
    "Rogê Biuzo": "Vendas B2B & Consultoria PME",
    "Carla Gonçalves": "Saúde Integrativa, Corpo & Movimento",
    "Theo Oliveira": "Música, Teatro, Arte & Palhaçaria",
    "Dëbora Nascı": "Saúde Integrativa, Corpo & Movimento",
    "Dëbora Nascı̊uti": "Saúde Integrativa, Corpo & Movimento",
    "Fabrícia Coelho": "Educação & Mentoria Acadêmica",
    "Alex Reis": "Música, Teatro, Arte & Palhaçaria",
    "Angelica Martins": "Música, Teatro, Arte & Palhaçaria",
    "Aline Koller": "Cuidado Parental & Família",
    "Amanda Cardoso": "Música, Teatro, Arte & Palhaçaria",
    "Arthur Martins": "Saúde Integrativa, Corpo & Movimento",
    "Diego Americo": "Liderança / Organização Corporativa",
    "Giovanna Sequeira": "Outros / Em estruturação",
    "Mychael Marcel": "Vendas B2B & Consultoria PME",
    "Bela Giannini": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Joey Jacksonn": "Educação & Mentoria Acadêmica",
    "MaCecilia Beltran": "Cuidado Parental & Família",
    "Telma": "Saúde Integrativa, Corpo & Movimento",
    "Taynara Mattos": "Saúde Integrativa, Corpo & Movimento",
    "Karime Neder": "Saúde Integrativa, Corpo & Movimento",
    "Nandà Luccâs": "Inovação Técnica de Base & Sustentabilidade",
    "Daniela Teixeira": "Liderança / Organização Corporativa",
    "Nathália Pantaleão": "Saúde Integrativa, Corpo & Movimento",
    "Lucas Rodrigues": "Liderança / Organização Corporativa",
    "Maria Regina": "Saúde Integrativa, Corpo & Movimento",
    "Rê": "Saúde Integrativa, Corpo & Movimento",
    "Ynglety Barros": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Allfeed": "Vendas B2B & Consultoria PME",
    "Base Alimentar": "Vendas B2B & Consultoria PME",
    "Marinês Korilo": "Saúde Integrativa, Corpo & Movimento",
    "Céu Caminhos Da Luz": "Saúde Integrativa, Corpo & Movimento",
    "Joyce Costa": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Luiza Doula": "Cuidado Parental & Família",
    "Diulio Gomes": "Outros / Em estruturação",
    "Diulio Gomes✝️⚓": "Outros / Em estruturação",
    "Vladia Lima": "Saúde Integrativa, Corpo & Movimento",
    "Davi Brasil": "Liderança / Organização Corporativa",
    "Karla Barreiros": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Shayenne Moura": "Liderança / Organização Corporativa",
    "Cínthya Alcântara": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Lari Gaigher": "Saúde Integrativa, Corpo & Movimento",
    "Fabiana Fortunato": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Ilana Lewinsohn": "Saúde Integrativa, Corpo & Movimento",
    "Evelen Tomaz": "Liderança / Organização Corporativa",
    "Evelen Tomaz 🤎": "Liderança / Organização Corporativa",
    "Thays Toyofuku": "Liderança / Organização Corporativa",
    "Simone Inês": "Cuidado Parental & Família",
    "Simone Tamega": "Liderança / Organização Corporativa",
    "Ju Zanella": "Saúde Integrativa, Corpo & Movimento",
    "Maíra Salomão": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Joyce Muzy": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Fernanda Moraes": "Saúde Integrativa, Corpo & Movimento",
    "Angela": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Marcia Penna": "Saúde Integrativa, Corpo & Movimento",
    "Marcia Penna de Castro": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Micheline": "Cuidado Parental & Família",
    "Cuidar de Dentro": "Cuidado Parental & Família",
    "Prem Karima": "Inovação Técnica de Base & Sustentabilidade",
    "Sandra Azzari": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Eron Villar": "Educação & Mentoria Acadêmica",
    "Destrave sua Escrita": "Educação & Mentoria Acadêmica",
    "Jordana Mol": "Saúde Integrativa, Corpo & Movimento",
    "Sheila Voos": "Liderança / Organização Corporativa",
    "A. Menegario": "Liderança / Organização Corporativa",
    "Dra Alessandra Menegario": "Liderança / Organização Corporativa",
    "Alivinio": "Vendas B2B & Consultoria PME",
    "Ricardo Arruda": "Vendas B2B & Consultoria PME",
    "Joslaene Santos": "Saúde Integrativa, Corpo & Movimento",
    "Karla Santos": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Viviane": "Saúde Integrativa, Corpo & Movimento",
    "Adriana Barbetta": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Carolina Bernardo": "Inovação Técnica de Base & Sustentabilidade",
    "Kaua": "Gestão Feminina, Transição de Carreira & Maturidade",
    "ka.conscious": "Gestão Feminina, Transição de Carreira & Maturidade",
    "ka.consciente": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Daniela Carneiro": "Vendas B2B & Consultoria PME",
    "Tais Jardim": "Música, Teatro, Arte & Palhaçaria",
    "Alex Maciel": "Educação & Mentoria Acadêmica",
    "Anderson Gonzaga": "Liderança / Organização Corporativa",
    "Marisa": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Milena": "Educação & Mentoria Acadêmica",
    "Tiago Campetti": "Inovação Técnica de Base & Sustentabilidade",
    "Lucas Roel": "Vendas B2B & Consultoria PME",
    "Ohanna Pacheco": "Outros / Em estruturação",
    "Adriana Gaia": "Vendas B2B & Consultoria PME",
    "Marcia Penna de Castro": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Tatiana Fávaro Lima": "Cuidado Parental & Família",
    "Carina Vieirat": "Saúde Integrativa, Corpo & Movimento",
    "Dra. Ana Brisolla": "Outros / Em estruturação",
    "Raquel Peres": "Saúde Integrativa, Corpo & Movimento",
    "Psi Nara Barreto": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Marcia Andrade": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Hernani Albuquerque": "Liderança / Organização Corporativa",
    "Su 😁✨️": "Saúde Integrativa, Corpo & Movimento",
    "Gabriel Martens": "Liderança / Organização Corporativa",
    "Si Briganti": "Liderança / Organização Corporativa",
    "Luiz Eduardo (Eduardo Rocha)": "Educação & Mentoria Acadêmica",
    "Marcela Madureira": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Bruno Mazetto": "Saúde Integrativa, Corpo & Movimento",
    "João Lima": "Educação & Mentoria Acadêmica",
    "Helena Woellner": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Manoela Couto": "Cuidado Parental & Família",
    "Elaine Gama": "Vendas B2B & Consultoria PME",
    "Erika Thiele": "Saúde Integrativa, Corpo & Movimento",
    "Cristiane Monteiro (Instituto FHE)": "Cuidado Parental & Família",
    "Fernanda (fernanda✨️)": "Saúde Integrativa, Corpo & Movimento",
    "Priscila Leite": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Giseli Paulon Ayurveda": "Saúde Integrativa, Corpo & Movimento",
    "Cris Terrazzan": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Cristina Maria": "Saúde Integrativa, Corpo & Movimento",
    "Mari Soccol": "Saúde Integrativa, Corpo & Movimento",
    "Bell Nacif": "Vendas B2B & Consultoria PME",
    "Ju Silva Estética": "Vendas B2B & Consultoria PME",
    "Isabela (Isabela Guilen)": "Saúde Integrativa, Corpo & Movimento",
    "Deusilene Leão": "Saúde Integrativa, Corpo & Movimento",
    "Lucianna Alves - Mentora": "Vendas B2B & Consultoria PME",
    "Ludmilla Azevedo": "Saúde Integrativa, Corpo & Movimento",
    "Elaine Bazilio": "Liderança / Organização Corporativa",
    "Juliana Köenig (Dra. Babosa)": "Saúde Integrativa, Corpo & Movimento",
    "Maria Carolina": "Saúde Integrativa, Corpo & Movimento",
    "Cristiane Silveira": "Educação & Mentoria Acadêmica",
    "Lucia Elena": "Liderança / Organização Corporativa",
    "Daniel Floriani": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Rebeca Madureira": "Vendas B2B & Consultoria PME",
    "Elany Almeida": "Vendas B2B & Consultoria PME",
    "Lana Peres": "Saúde Integrativa, Corpo & Movimento",
    "Aline Seri": "Gestão Feminina, Transição de Carreira & Maturidade",
    "Juliane do Carmo": "Outros / Em estruturação",
    "Cris Sathler": "Saúde Integrativa, Corpo & Movimento",
    "Rui Francisco": "Liderança / Organização Corporativa",
    "Marcos Mauricio de Souza": "Outros / Em estruturação",
    "Teacher Jozy Lima": "Educação & Mentoria Acadêmica",
    "Karol Marinho": "Educação & Mentoria Acadêmica",
    "Dr Douglas Lima": "Saúde Integrativa, Corpo & Movimento",
    "Kelvin Moreira (Tiziu Capoeira)": "Saúde Integrativa, Corpo & Movimento",
    "Andrea Santos (ARS Terapias)": "Saúde Integrativa, Corpo & Movimento"
}

# Load details for active profiles (Instagram, original description/profession)
details = {
    "Fabio Takwara": ("SP (Limeira)", "Ambientalista / Autodidata", "@fabiotakwara", "Bambu termorretificado + PU de Mamona, construção de estruturas leves (cúpulas geodésicas) & workflows de IA. Assista: [Estrutura Leve (Shorts)](https://www.youtube.com/shorts/cR3EY8laLAw) & [Domo de Bambu (Vídeo)](https://youtu.be/OGeVIEGZfb0?si=fB3dTQQi7PW7TnsV)"),
    "Marcello Pedro": ("RJ", "Prof. Ed. Física / Surf", "@bodyboardlgendsclub", "Performance no surf e PCDs (Lei do Mar)"),
    "Michelle Santiago": ("SP (Águas de S. Pedro)", "Enfermeira", "-", "Liderança Sistêmica para equipes de saúde"),
    "Momento Bela": ("SP (Capital)", "Pedagoga / Psicóloga TCC", "@psi.bruarciere", "Orientação parental para mães (crianças/adolescentes)"),
    "⚡Vânia Távora": ("CE (Fortaleza)", "-", "-", "Posicionamento digital no digital"),
    "Renata Cardinali": ("Não Identificado", "Direcionadora Familiar", "@renata.cardinali", "Minha mentoria une famílias"),
    "Mandy Bettega 🪷": ("SC", "Pedagoga / Esp. ABA", "-", "Mentoria para parents e responsáveis de crianças com TEA"),
    "Luciana": ("SC (Floripa)", "Pedagoga / Psicopedagoga", "-", "Mentoria InPulsa: a saída é para dentro para mulheres 35+"),
    "Fabiane Ji": ("BA", "Instrutora de Yoga", "@fabiane_ji", "Sustentabilidade de carreira para viver de Yoga"),
    "Ana Carolina Mattoso": ("Não Identificado", "Prof. / Mentora Acadêmica", "@professora.mattoso", "Mentoria acadêmica para processos seletivos e escrita"),
    "Patrícia Bertachini Bissetti": ("Não Identificado", "Psicopedagoga", "@pbertachini", "Psicopedagogia Clínica e Institucional. Site: [psicopedagogiainovadora.com.br](http://www.psicopedagogiainovadora.com.br)"),
    "Andréa Claudini ⚡": ("PR (Londrina)", "Hipnoterapeuta / Metacampo", "https://www.instagram.com/reel/DZAn_BNReU3/?igsh=MTJ4aGNtZmdnMHE3ZA==", "Novo significado para a segunda metade da vida"),
    "Priscila Kalil": ("Não Identificado", "Psicóloga / RH", "@priscilakalil.psi", "Projeto Lidere-se (Autogestão de Vida)"),
    "Arlete D'arc": ("SP (Poá)", "Psicanalista Cristã", "@arletedarc_mentorapsicanalista", "Recomeço de mulheres após relações abusivas"),
    "Lucas Vargas": ("RS", "Consultor Condominial", "@lucasvargas.consultor", "Vendas B2B para o setor condominial"),
    "Ju Almeida": ("SP", "CMO / Mkt / Eventos", "LinkedIn: jualmeidaa", "Valor estratégico para líderes e executivos"),
    "Monica Marques": ("RJ", "Fonoaudióloga", "@p/DXj7AvLgARv", "Pais de neurodivergentes (Autismo/TDAH)"),
    "Daniela Freitas": ("Não Identificado", "Fisioterapeuta", "@danielasoufreitas", "Mentoria para empreendedoras da saúde"),
    "Sandra": ("SP (Promissão)", "Fisioterapeuta", "@anastore_as", "Saúde integrativa, mente e corpo"),
    "Luiza Lyra": ("BA (Vitória da Conquista)", "Ortodontista", "@luizanayara", "Dentistas saindo da zona de conforto"),
    "Ana Simões": ("Não Identificado", "Psicóloga Intensivista", "@souanasimoes", "Humanização e autoconhecimento hospitalar"),
    "Rogê Biuzo": ("RJ (Saquarema)", "Palestrante / Mágico", "@rogebiuzo", "Além do Contracheque (renda extra p/ pais e profs.)"),
    "Carla Gonçalves": ("RJ (Volta Redonda)", "Adm / Coach de Bem-Estar", "@carlametodorc", "Método RC de emagrecimento para famílias"),
    "Theo Oliveira": ("SP (Capital/Lapa)", "Ator / Palhaço", "@circodisoladies", "Palhaçaria cênica e neurodivergência"),
    "Dëbora Nascı": ("Não Identificado", "Prof. Yoga/Meditação", "@deboranasciuti", "Método Florescer (Ansiedade/Burnout/PNL)"),
    "Dëbora Nascı̊uti": ("Não Identificado", "Prof. Yoga/Meditação", "@deboranasciuti", "Método Florescer (Ansiedade/Burnout/PNL)"),
    "Fabrícia Coelho": ("Não Identificado", "Prof. Alfabetizadora", "-", "Método OnomoFônico p/ professores alfabetizadores"),
    "Alex Reis": ("RJ", "Músico / Baterista", "@alexreisrodriguez", "Método Bateria Essencial (Cirque du Soleil)"),
    "Angelica Martins": ("Não Identificado", "Designer Visual da Cena", "@angelicamartpe", "Design do Espetáculo cênico"),
    "Aline Koller": ("Não Identificado", "Psicóloga Junguiana", "@alinekollerpsi", "Maternidade de filhos neurodivergentes"),
    "Amanda Cardoso": ("SE (Aracaju)", "Fotógrafa", "@amandacardosofotografia", "Fotografia de partos e famílias"),
    "Arthur Martins": ("AL (Maceió)", "Ator / Diretor / Terapeuta", "@arthur.martins.barros", "Mentoria Exale: descompressão, criatividade e espaço interno para quem vive sob pressão e urgência constante (ludicidade da palhaçaria, jogos teatrais, escrita criativa, yoga do riso)."),
    "Diego Americo": ("SP", "Cabeleireiro / Beauty", "@diegoamerico", "Artista da Beleza (Direção de Carreira)"),
    "Giovanna Sequeira": ("Não Identificado", "Atriz / Mentora", "@gisequeira", "Comunicação e escrita de livros"),
    "Mychael Marcel": ("Não Identificado", "SEO / Ads", "@mychaelmarcel", "Posicionamento local no Google e IAs"),
    "Bela Giannini": ("MG (Ouro Preto)", "Recursos Humanos", "-", "Transição de carreira de RH"),
    "Joey Jacksonn": ("PR (Curitiba)", "Prof. de Musicalização / Coordenador", "@joeyjacksonn_", "Método PRO Action: aprender idiomas com propósito, autonomia e constância (método geral aplicável a qualquer idioma, e muito eficaz também para TDAH/neurodivergentes)"),
    "MaCecilia Beltran": ("Não Identificado", "Ortodontista/Psicoemb.", "@dra.maceciliabeltran", "Gestão conectada e maternidade consciente"),
    "Telma": ("RN (Parnamirim)", "Enfermeira", "-", "Psicoterapia Integrativa"),
    "Taynara Mattos": ("Não Identificado", "Fisioterapeuta", "@taynaramattosfisio", "Massoterapia Clínica e Acupuntura"),
    "Karime Neder": ("RJ (Ilha Grande)", "Prof. Yoga", "-", "Formação de professores de Vinyasa Yoga"),
    "Nandà Luccâs": ("SP (USP)", "Bióloga USP", "-", "Honey Trace Brasil (rastreabilidade de mel)"),
    "Daniela Teixeira": ("SP", "Enfermeira", "LinkedIn: daniela-teixeira", "Gestores para Medicine Diagnóstica"),
    "Nathália Pantaleão": ("DF", "Nutricionista", "-", "Rotina funcional para empreendedoras"),
    "Lucas Rodrigues": ("Não Identificado", "Consultor de Mkt", "-", "Branding e posicionamento de empresas premium"),
    "Maria Regina": ("RS (Porto Alegre)", "Biomédica Esteta", "-", "Exames laboratoriais e suplementação"),
    "Rodrigo Dumont": ("Não Identificado", "Líder de Dados / Tech", "@dumontrodrigo", "Liderança em Dados no meio corporativo"),
    "Ynglety Barros": ("AM", "Etiqueta e Comport.", "@yngletybarros", "Forte & Elegante (Presença e Etiqueta)"),
    "Marinês Korilo": ("Não Identificado", "Canalizadora / Xamã", "@madrinhamarineskorilo", "Medicinas da floresta digitais e desenvolvimento"),
    "Joyce Costa": ("Não Identificado", "Arquiteta/Cientista Soc.", "@eu.joycecosta", "Mulheres 40+ de alta performance neurodivergentes"),
    "Luiza Doula": ("Não Identificado", "Doula / Consultora", "@luiza_doula", "Puerpério e amamentação sem caos"),
    "Diulio Gomes": ("RS", "Ator / Teólogo", "@diulio_gomes", "Comunicação e oratória para especialistas"),
    "Diulio Gomes✝️⚓": ("RS", "Ator / Teólogo", "@diulio_gomes", "Comunicação e oratória para especialistas"),
    "Vladia Lima": ("CE (Fortaleza)", "Neuropsicóloga", "@vladialimapsicologa", "Mentoria prática de TDAH para adultos"),
    "Davi Brasil": ("Não Identificado", "Gestor Tech (ex-ITA)", "LinkedIn: davibrasil", "Adultos 2E (TDAH + Altas Habilidades)"),
    "Karla Barreiros": ("RJ (Araruama)", "Advogada / Ceramista", "-", "Transição de carreira e análise consciencial"),
    "Shayenne Moura": ("Não Identificado", "Data Scientist", "-", "Equilíbrio de rotina para líderes de TI"),
    "Cínthya Alcântara": ("SC", "Psicóloga", "@cinthya.alcantarapsi", "Segurança interna para mulheres competentes"),
    "Lari Gaigher": ("SP (Guararema)", "Prof. Yoga", "@larissagaigher", "Espiritualidade viva além do tapetinho"),
    "Fabiana Fortunato": ("MG (Santa Luzia)", "Psicóloga", "-", "Transição de carreira para mulheres"),
    "Ilana Lewinsohn": ("BA (Arraial d'Ajuda)", "Bióloga / Terapeuta", "@massixa", "Massagem Integrativa Xamânica"),
    "Evelen Tomaz": ("BA (Salvador)", "Experiência do Paciente", "-", "Humanização e experiência do paciente em saúde"),
    "Evelen Tomaz 🤎": ("BA (Salvador)", "Experiência do Paciente", "-", "Humanização e experiência do paciente em saúde"),
    "Thays Toyofuku": ("Não Identificado", "Consultora DE&I", "@thaystoyofuku", "Comunicação inclusiva e DEI corporativo"),
    "Simone Inês": ("RJ", "Pedagoga", "@simoneinesescritora", "Maternidade espiritual e seres de luz"),
    "Simone Tamega": ("SP", "Ortodontista / Produtora", "@flavio_calcada", "Suporte clínico para recém-especialistas em Ortodontia (planejamento, discussão de casos e travas clínicas). Produzido por ela, mentorado por Flavio Calçada."),
    "Ju Zanella": ("Não Identificado", "Nutri. Ayurveda", "@juzanella.ayurveda", "Longevidade saudável e cuidados paliativos"),
    "Maíra Salomão": ("SP", "Psicóloga", "-", "Transição de vida para mulheres 30+"),
    "Joyce Muzy": ("SP", "Psicóloga TCC", "@joycemuzy_", "Mentoria para mulheres sobrecarregadas"),
    "Fernanda Moraes": ("RS", "Nutricionista", "@fernandamoraes_nutri", "Mitigação de sintomas da menopausa 40+"),
    "Angela": ("Não Identificado", "Massoterap. Tântrica", "-", "Cura de traumas e independência emocional"),
    "Marcia Penna": ("Não Identificado", "Psicanalista", "@marciacastropsi", "Desenvolvimento emocional"),
    "Marcia Penna de Castro": ("SP (Indaiatuba)", "Psicanalista", "@marciacastropsi", "Mentoria de reconstrução, autoestima e recomeço após separação"),
    "Prem Karima": ("RJ (Búzios)", "Produtora de Eventos", "@relucilara", "Método Evento Vivo (sustentabilidade)"),
    "Sandra Azzari": ("Não Identificado", "Eng. Química/Terapeuta", "@sandraazzari", "Carreira sólida e cavalos 40+"),
    "Eron Villar": ("PE (Recife)", "Doutorando UFPE", "@destravando_a_escrita21", "Redação em concursos (Jornada do Herói). Instagram pessoal: @eronvillar"),
    "Jordana Mol": ("MG (BH)", "Ginecologista", "@drajordanamol", "Saúde integral no climatério"),
    "Sheila Voos": ("Não Identificado", "Educadora", "@sheilavoos", "Soft skills e Neurociência aplicada"),
    "A. Menegario": ("Não Identificado", "Nutricionista", "@allfeedconsultoria", "Boas práticas alimentares e varejo"),
    "Dra Alessandra Menegario": ("Não Identificado", "Nutricionista", "@allfeedconsultoria", "Boas práticas alimentares e varejo"),
    "Alivinio": ("Não Identificado", "Economista / Prof.", "@alivinioalmeida", "Análise e Processos de Gestão para PMEs"),
    "Ricardo Arruda": ("CE (Fortaleza)", "TikToker / Mentor", "@ricardoarrudamentor", "Sair do zero no TikTok Shopping"),
    "Joslaene Santos": ("SC", "Nutricionista", "@joslaene.simao", "Diabetes e capacitação de nutricionistas"),
    "Karla Santos": ("Não Identificado", "Psicóloga / RH", "@karlasantoscarreira", "Planejamento e posicionamento de carreira"),
    "Viviane": ("Não Identificado", "Hipnoterapeuta", "@vivi_terapia_viva", "Hipnose clínica baseada em neurociência"),
    "Adriana Barbetta": ("PR (Londrina)", "Empresária", "@adrianabarbetta", "Desenvolvimento pessoal e financeiro para mulheres"),
    "Carolina Bernardo": ("DF (Brasília)", "Bióloga/Dra. Economia", "@carolinidades", "Leis e políticas ambientais p/ analistas"),
    "Kaua": ("RJ", "Tatuador", "@ka.consciente", "Projeto Caverna (reconstrução de identidade)"),
    "ka.conscious": ("RJ", "Tatuador", "@ka.consciente", "Projeto Caverna (reconstrução de identidade)"),
    "ka.consciente": ("RJ", "Tatuador", "@ka.consciente", "Projeto Caverna (reconstrução de identidade)"),
    "Daniela Carneiro": ("PR (Curitiba)", "Adm / Franquias", "@dfcconsultoria", "Gestão de KPIs para cafeterias/padarias"),
    "Tais Jardim": ("CE (Fortaleza)", "Artesã", "@teaatelie", "Macramê em grandes obras e decoração"),
    "Alex Maciel": ("Não Identificado", "Trainer Educacional", "@alexmacielprofessor", "Apoio e mentoria de estudos para aprovação escolar/concursos"),
    "Anderson Gonzaga": ("Não Identificado", "Prof. / Mentor / Facilitador (Tech & Gestão)", "@eu.sou.gonzaga", "Transformação organizacional, Business Agility e liderança"),
    "Marisa": ("SP (Capital/Lapa)", "Mercado Financeiro / Terapeuta", "@ma.rmalvs", "Mentoria Recalibrar a Rota (autoestima, clareza e equilíbrio)"),
    "Milena": ("RS (Getúlio Vargas)", "Professora / Mentora", "-", "Capacitação e formação continuada para professores"),
    "Tiago Campetti": ("PR (Curitiba)", "Arquiteto", "@arquiteto_tiagocampetti", "Capacitação para planejamento e execução de reformas residenciais"),
    "Lucas Roel": ("Não Identificado", "Agronegócio (Bioinsumos & Fisiologia)", "ROELX", "Advisory, mentorias e performance de vendas no Agronegócio"),
    "Ohanna Pacheco": ("SC (Araranguá)", "Manejo Comportamental de Animais", "@evolu_pet", "Mentoria online de comportamento animal e pets não-convencionais"),
    "Adriana Gaia": ("Não Identificado", "Mercado Ótico / Empresária", "@oticaadrianagaia", "Mentoria Empreender sem Franquia no ramo ótico em 90 dias"),
    "Tatiana Fávaro Lima": ("PR (Curitiba)", "Pedagoga Waldorf / ex-TI Prof.", "-", "Orientação familiar para gestantes ou famílias com crianças de 0 a 3 anos"),
    "Carina Vieirat": ("RJ", "Terapeuta Ayurveda / Prof. de Yoga", "@carinavieirat", "Mentoria de saúde e bem-estar para mulheres em fase de mudança"),
    "Dra. Ana Brisolla": ("SP (Interior)", "Advogada / Amante da Arte", "-", "Nicho de mentoria em estruturação"),
    "Raquel Peres": ("Não Identificado", "Psicóloga Infanto-Juvenil / Esp. ABA", "-", "Mentoria para profissionais de saúde e educação sobre raciocínio clínico criativo em ABA"),
    "Psi Nara Barreto": ("RJ", "Psicóloga TCC", "@narabarretopsicologa", "Mentoria Desperte seu valor (autoestima e independência emocional pós-abuso)"),
    "Marcia Andrade": ("SP", "Terapeuta Transpessoal / ex-Oficial PM SP", "@marcitaregina_terapeuta", "Mentoria de descompressão emocional para mulheres sobrecarregadas"),
    "Hernani Albuquerque": ("Não Identificado", "Educador Físico / CEO Naniko's Circus / Dentista", "@hernanialbuquerque", "Mentoria de carreira e negócios para profissionais circenses"),
    "Su 😁✨️": ("Não Identificado", "Biomédica / Servidora Pública / Terapeuta", "-", "Ressignificação de crenças e liberação de padrões repetitivos para terapeutas"),
    "Gabriel Martens": ("RJ", "Gestor de Processos de TI", "@martensglobal", "Mentoria de gestão de processos de TI e tecnologia para empresas em crescimento"),
    "Si Briganti": ("SP (Embu das Artes)", "Pesquisadora de Mercado / ex-Executiva", "@sousibriganti", "Mentoria Lead2Be (liderança feminina para novas gestoras)"),
    # New Members Added:
    "Luiz Eduardo (Eduardo Rocha)": ("PB (João Pessoa)", "Professor / Advogado", "-", "Licenciado em Matemática, esp. Educação Especial (AH/SD, TEA), bacharel em Direito/Teologia, mestrando em Adm. Pública. Livros sobre Violência Doméstica e Discipulado."),
    "Marcela Madureira": ("Não Identificado", "Mentora de mulheres / Palestrante", "@juntasnajornada2.0", "Líder do Movimento Juntas na Jornada. Ajuda mulheres a se priorizarem sem culpa."),
    "Bruno Mazetto": ("Não Identificado (Nômade)", "Professor de Yoga (17 anos)", "-", "Monetização para professores de Yoga (nômade há 6 anos) ou desenvolvimento pessoal/estilo de vida para profissionais digitais."),
    "João Lima": ("PR (Curitiba)", "Prof. de Piano / Pesquisador", "-", "Mentoria 'Além do Analógico' ajudando profissionais do presencial com travas tecnológicas a gravarem e ensinarem online."),
    "Helena Woellner": ("PR (Curitiba)", "Economista / Psicanalista", "-", "Jornada de autoconhecimento e planejamento financeiro de vida alinhado a valores para mulheres."),
    "Manoela Couto": ("SP (Capital)", "Enfermeira / Consultora em Gerontologia", "@Manoelapcouto", "Apoio a famílias/filhos que cuidam de pais idosos, organizando rotinas de cuidado e promovendo consciência do envelhecimento."),
    "Elaine Gama": ("PR (Curitiba)", "Consultora de Marketing", "@elainegama.co", "Marketing para pequenas empreendedoras organizarem o Instagram e venderem mais. Instagram profissional secundário: @elainegamadigital"),
    "Micheline": ("RJ (Teresópolis)", "Pedagoga / Neuropsicopedagoga / Terapeuta", "@cuidardedentro.oficial", "Mãe de neurodivergentes (Autismo/TDAH). Mentoria de equilíbrio emocional e qualidade de vida. Instagram saúde: @naturalmentesaudavel2024"),
    "Erika Thiele": ("Não Identificado", "Bióloga / Psicoterapeuta Radiestesista", "-", "Fundadora do Instituto Plasma. Ministra cursos e forma terapeutas em radiestesia clássica profunda."),
    "Cristiane Monteiro (Instituto FHE)": ("SP (Santo André)", "Psicopedagoga / Esp. Neurociência", "@crismonteiro.fhe", "Método Criança Bonsai: desenvolvimento neural e emocional infantil (0-2 anos e 2-6 anos). Perfil do marido: @libanomonteiro"),
    "Fernanda (fernanda✨️)": ("Não Identificado", "Artista Visual / Ceramista / Psicanalista Junguiana", "-", "Reconstrução da relação da mulher consigo mesma através da criação simbólica no barro e autoconhecimento."),
    "Priscila Leite": ("Não Identificado", "Coach de Carreira / ex-Seguros", "@priscilaleiteagir", "Mentoria Rota da Senioridade: protagonismo e crescimento profissional para quem está invisível na empresa e busca promoção."),
    "Giseli Paulon Ayurveda": ("Não Identificado", "Terapeuta Ayurveda", "@giselipaulonayurveda", "Atendimentos e mentoria em Ayurveda para saúde integral."),
    "Cris Terrazzan": ("Não Identificado", "Empreendedora / Mentora", "-", "Transição e reinvenção de carreira pós-maternidade."),
    "Cristina Maria": ("SC (Jaraguá do Sul)", "Instrutora de Yoga", "@cristinamaria.om", "Maternidade e reposicionamento profissional pós-recolhimento maternal."),
    "Mari Soccol": ("Não Identificado", "Nutricionista especialista em Saúde da Mulher", "@nutrimarisoccol", "Mentoria de saúde e bem-estar para mulheres 40+."),
    "Bell Nacif": ("Não Identificado", "Consultora / Mentora de Varejo", "@bellnacif", "Especialista em operações de varejo e gestão comercial de lojas."),
    "Ju Silva Estética": ("Não Identificado", "Esteticista / Mentora de Beleza", "-", "Mentoria para esteticistas/profissionais da beleza faturarem mais a partir de casa com estratégias e protocolos simples."),
    "Isabela (Isabela Guilen)": ("Não Identificado", "Prof. de Yoga / Meditação", "@isabelaguilen", "Aulas de Yoga/Meditação e retiros na natureza para mães e mulheres reconectarem habilidades."),
    "Deusilene Leão": ("GO (Goiânia)", "Profa. Dra. em Ciências da Religião", "-", "Mentoria de saúde e cura baseada em Inteligência Espiritual (processo complementar para mulheres com câncer de mama)."),
    "Lucianna Alves - Mentora": ("Não Identificado", "Especialista em B2B & TI", "@luciannaalves85", "Mentoria de Arquitetura Comercial para PMEs destravarem faturamento e estruturarem máquina de vendas. LinkedIn: luciannapalves"),
    "Ludmilla Azevedo": ("SP", "Professora de Yoga / Designer de Moda", "@lud_yoga", "Consultoria Carreira Sustentável no Yoga (posicionamento e negócios para novos professores). Letramento Racial."),
    "Elaine Bazilio": ("SP", "Fisioterapeuta / Gestora Pública", "@elainebaziliooficial", "Mentoria de Gestão em Saúde baseada na Ciência da Melhoria para líderes e gestores da saúde."),
    "Juliana Köenig (Dra. Babosa)": ("Não Identificado", "Engenheira Agrônoma / Terapeuta", "@drababosaoficial", "Cocriadora da Medicina da Babosa® e Mentoria MMB para terapeutas e profissionais da saúde natural."),
    "Maria Carolina": ("Não Identificado", "Dentista / Terapeuta Integrativa", "-", "Transição de carreira de odontologia para terapias (EMF Balancing, constelação, reiki, registros akashicos, kabala)."),
    "Cristiane Silveira": ("Não Identificado", "Profa. de História da Arte / Pesquisadora", "-", "Apoio e mentoria para produtos digitais acadêmicos e curadoria de artes visuais, conciliando rotina de cuidados pós-AVC do filho."),
    "Lucia Elena": ("Não Identificado", "Consultora / Ex-Gerente de Seguros (37 anos)", "-", "Mentoria para novos líderes e executivos se preparando para liderar."),
    "Daniel Floriani": ("Não Identificado", "Mentor de Carreira / Desenvolvimento", "@odanifloriani", "Desenvolvimento pessoal e re-significação de crenças limitantes."),
    "Rebeca Madureira": ("Não Identificado", "Consultora de Marketing Digital", "@rebecamadureiradigital", "Estratégia e reposicionamento de marca no Instagram para atração de público qualificado e nichado."),
    "Elany Almeida": ("DF (Brasília)", "Advogada / Pesquisadora", "@elanyalmeidas", "Advocacia em Direito Médico e da Saúde com foco digital. Consultoria jurídica corporativa e mentoria para carreiras jurídicas. Primeira mulher civil doutora em Ciências Militares no Brasil."),
    "Lana Peres": ("Não Identificado", "Terapeuta / Condução de práticas de bem-estar", "@institutosinergiaa", "Meditação guiada, fortalecimento interior e conexão espiritual (Instituto Sinergia)."),
    "Aline Seri": ("Não Identificado", "Mentora de Desenvolvimento Pessoal", "@alineseri_", "Mentoria de desbloqueio emocional, profissional e financeiro para superação de estagnação."),
    "Juliane do Carmo": ("Não Identificado", "Estratégia / Nicho em estruturação", "@julianeldocarmo", "Nicho de mentoria em estruturação."),
    "Cris Sathler": ("RJ (Rio de Janeiro)", "Psicóloga Clínica / Sexóloga", "@psicrissathler", "Psicologia clínica, Gestalt-terapia, terapia de casais e sexologia."),
    "Rui Francisco": ("Não Identificado", "Mentor de Liderança / Autor", "@ruifrancisco.oficial", "Mentoria em liderança e gestão, autor do livro Liderança Pioneira Metaversa."),
    "Marcos Mauricio de Souza": ("Não Identificado", "Advogado", "@mauriciodesouzaadv", "Nicho de mentoria em estruturação."),
    "Teacher Jozy Lima": ("Não Identificado", "Professora de Inglês / Idiomas", "-", "Mentoria e ensino de idiomas (Instagram temporariamente indisponível)."),
    "Karol Marinho": ("RN (Natal)", "Advogada / Professora Universitária", "@karollinsmarinho", "Advocacia e consultoria em Direito Tributário, professora doutora na UFRN."),
    "Dr Douglas Lima": ("SC (São José)", "Dentista / Implantodontista", "@drdouglaslima.sc", "Odontologia estética, implantes dentários e cirurgia guiada."),
    "Kelvin Moreira (Tiziu Capoeira)": ("SP", "Educador Físico / Contramestre de Capoeira", "@tiziu.capoeira", "Projeto Profissão Capoeira: formação, cursos e mentorias de profissionalização e psicomotricidade aplicada para capoeiristas."),
    "Andrea Santos (ARS Terapias)": ("SP", "Psicanalista / Terapeuta Holística", "@arsterapias", "Psicanálise, espiritualidade, tratamentos energéticos e facilitação de workshops da Filosofia Louise Hay.")
}

# Self-declared neurodivergent mapping
neurodivergences = {
    "Fabio Takwara": "TDAH",
    "Ohanna Pacheco": "TDAH / Bipolar Tipo 2",
    "Aline Koller": "TDAH",
    "Davi Brasil": "TDAH / AH/SD (2E)",
    "Joey Jacksonn": "TDAH / AH/SD",
    "Nandà Luccâs": "TDAH / AH/SD",
    "Joyce Costa": "Neurodivergente",
    "Shayenne Moura": "AH/SD",
    "Marcello Pedro": "TDAH",
    "Micheline": "Autismo Nível 1 / TDAH",
    "Elany Almeida": "AH/SD"
}

# Name normalizations map
name_map = {
    "Ohanna": "Ohanna Pacheco",
    "Carina": "Carina Vieirat",
    "Gabriel": "Gabriel Martens",
    "Momento Bela": "Bruna Arciere",
    "Aline": "Aline Koller",
    "Evelen Tomaz": "Evelen Tomaz 🤎",
    "Elen Rezende": "Elen Rezende ✨",
    "Diulio Gomes": "Diulio Gomes✝️⚓",
    "Marcia Penna": "Marcia Penna de Castro",
    "A. Menegario": "Dra Alessandra Menegario",
    "Alivinio": "Alivinio Econoeduca",
    "ka.conscious": "Kaua (ka.consciente)",
    "ka.consciente": "Kaua (ka.consciente)",
    "Kaua": "Kaua (ka.consciente)",
    "Amanda Cardoso Pessoal": "Amanda Cardoso",
    "Destrave sua Escrita": "Eron Villar",
    "Cuidar de Dentro": "Micheline",
    "Simone": "Simone Inês",
    "Simone Tamega 🪻": "Simone Tamega",
    "Priscila Kalil Psi": "Priscila Kalil",
    "Priscila": "Priscila Leite",
    "Elaine": "Elaine Bazilio",
    "Elaine Gama": "Elaine Gama",
    "sunset": "Sunset",
    "Patrícia Bertachini": "Patrícia Bertachini Bissetti",
    "Joseph (Joey) Jacksonn": "Joey Jacksonn",
    "Eduardo Rocha": "Luiz Eduardo (Eduardo Rocha)",
    "Luiz Eduardo": "Luiz Eduardo (Eduardo Rocha)",
    "Marcela Madureira": "Marcela Madureira",
    "Bruno Mazetto": "Bruno Mazetto",
    "João Lima": "João Lima",
    "Helena": "Helena Woellner",
    "Helena Woellner": "Helena Woellner",
    "Manoela Couto": "Manoela Couto",
    "Erika": "Erika Thiele",
    "Erika Thiele": "Erika Thiele",
    "Instituto FHE": "Cristiane Monteiro (Instituto FHE)",
    "Cristiane Monteiro": "Cristiane Monteiro (Instituto FHE)",
    "fernanda✨️": "Fernanda (fernanda✨️)",
    "Priscila Leite": "Priscila Leite",
    "Giseli Paulon Ayurveda": "Giseli Paulon Ayurveda",
    "Cris Terrazzan": "Cris Terrazzan",
    "Cristina Maria": "Cristina Maria",
    "Cristina Maria🌹🐝": "Cristina Maria",
    "Cristina Maria🌹​🐝": "Cristina Maria",
    "Mari Soccol": "Mari Soccol",
    "Bell Nacif": "Bell Nacif",
    "Ju Silva Estética": "Ju Silva Estética",
    "Isabela": "Isabela (Isabela Guilen)",
    "Isabela Guilen": "Isabela (Isabela Guilen)",
    "Deusilene Leão": "Deusilene Leão",
    "Lucianna Alves - Mentora": "Lucianna Alves - Mentora",
    "Lucianna Alves  Add Value": "Lucianna Alves - Mentora",
    "Lucianna Alves": "Lucianna Alves - Mentora",
    "Lud Azevedo": "Ludmilla Azevedo",
    "Ludmilla Azevedo": "Ludmilla Azevedo",
    "Juliana Köenig/ Dra Babosa": "Juliana Köenig (Dra. Babosa)",
    "Juliana Köenig": "Juliana Köenig (Dra. Babosa)",
    "Maria Carolina": "Maria Carolina",
    "Cristiane Silveira": "Cristiane Silveira",
    "Lucia Elena": "Lucia Elena",
    "Daniel Floriani": "Daniel Floriani",
    "Rê": "Maria Regina",
    "Juliane": "Juliane do Carmo",
    "Tiziu Capoeira": "Kelvin Moreira (Tiziu Capoeira)",
    "Marcos Mauricio": "Marcos Mauricio de Souza",
    "Andrea - ARS Terapias": "Andrea Santos (ARS Terapias)"
}

def clean_sender(sender):
    sender = sender.strip("\u202a\u202c\u200f\u200e").replace("~\u202f", "").replace("~", "").strip()
    return name_map.get(sender, sender)

def get_update_time():
    return "22/06/2026 às 16:59"

def make_clickable(ig_str):
    if not ig_str or ig_str == "-":
        return "-"
    if ig_str.startswith("[") and ig_str.endswith(")"):
        return ig_str  # Already clickable
    if ig_str.startswith("http"):
        return f"[Link]({ig_str})"
    if ig_str.startswith("@"):
        username = ig_str[1:]
        return f"[{username}](https://www.instagram.com/{username})"
    if "linkedin:" in ig_str.lower():
        username = ig_str.split(":")[-1].strip()
        return f"[LinkedIn](https://www.linkedin.com/in/{username})"
    return ig_str

# Read lines from all six files
lines = []
for file_name in ["_chat 5.txt", "_chat 6.txt", "_chat 7.txt", "_chat 8.txt", "_chat 9.txt", "_chat 10.txt"]:
    path = f"/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/01_TRIAGEM_BRUTA/{file_name}"
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        lines.extend(text.split("\n"))
    except FileNotFoundError:
        print(f"Skipping missing file: {path}")

members = set()
line_pattern = re.compile(r"^\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}\] ([^:]+): (.*)")
for line in lines:
    m = line_pattern.match(line)
    if m:
        sender, msg = m.groups()
        sender = clean_sender(sender)
        if sender and sender != "Raízes - Grupo de Entrada - Junho 26":
            if not any(adm.lower() in sender.lower() for adm in admins):
                members.add(sender)
        if "adicionou" in msg:
            parts = msg.split("adicionou")
            if len(parts) > 1:
                added_part = parts[1]
                added_names = re.split(r",| e ", added_part)
                for name in added_names:
                    name = clean_sender(name)
                    if name and name not in ["você", "o", "a", "os", "as"] and not any(adm.lower() in name.lower() for adm in admins):
                        members.add(name)

# Exclude admins
members = {m for m in members if not any(adm.lower() in m.lower() for adm in admins)}
members.add("Ohanna Pacheco") # Manually include active

mapped_members = []
state_counts = {}
niche_counts = {}

for m in sorted(list(members)):
    state = "Não Identificado"
    for name, s in explicit_states.items():
        if name.lower() in m.lower() or m.lower() in name.lower():
            state = s
            break
            
    if state == "Não Identificado":
        digits = "".join(c for c in m if c.isdigit())
        if len(digits) >= 4 and digits.startswith("55"):
            ddd = digits[2:4]
            state = ddd_to_state.get(ddd, "Não Identificado")
        elif len(digits) == 10 or len(digits) == 11:
            ddd = digits[0:2]
            state = ddd_to_state.get(ddd, "Não Identificado")

    niche = "Não se apresentou / Silencioso"
    for name, n in active_niches.items():
        if name.lower() in m.lower() or m.lower() in name.lower():
            niche = n
            break

    detail_tuple = None
    for name, d in details.items():
        if name.lower() in m.lower() or m.lower() in name.lower():
            detail_tuple = d
            break
            
    if detail_tuple:
        state_str = detail_tuple[0]
        prof_str = detail_tuple[1]
        ig_raw = detail_tuple[2]
        desc_str = detail_tuple[3]
    else:
        state_str = state_names.get(state, "Não Identificado") if state != "Não Identificado" else "Não Identificado"
        prof_str = "-"
        ig_raw = "-"
        desc_str = "Não se apresentou / Silencioso"

    neuro_str = "-"
    for name, nd in neurodivergences.items():
        if name.lower() in m.lower() or m.lower() in name.lower():
            neuro_str = nd
            break

    mapped_members.append({
        "name": m,
        "state": state_str,
        "prof": prof_str,
        "ig": make_clickable(ig_raw),
        "desc": desc_str,
        "niche": niche,
        "neuro": neuro_str
    })

    state_lbl = state_names.get(state, "Não Identificado")
    state_counts[state_lbl] = state_counts.get(state_lbl, 0) + 1
    niche_counts[niche] = niche_counts.get(niche, 0) + 1

mapped_members = sorted(mapped_members, key=lambda x: (x["desc"] == "Não se apresentou / Silencioso", x["name"]))

# Build the dynamic censo details
active_count = len([m for m in mapped_members if m["desc"] != "Não se apresentou / Silencioso"])
silent_count = len([m for m in mapped_members if m["desc"] == "Não se apresentou / Silencioso"])
total_m = len(mapped_members)
total_census = 188 # Fixed official participant censo (194 total - 6 admins)

# We will generate a base text block and then replace the logo path dynamically for each file
def build_markdown(logo_path):
    update_t = get_update_time()
    
    md = []
    md.append(f'# <img src="{logo_path}" width="55" style="vertical-align: middle; margin-right: 15px;" /> Raio-X Completo: Grupo Raízes (Junho/26)\n')
    md.append(f"> 📅 **Última atualização:** {update_t}\n")
    md.append("> 📝 **Resumo da atualização:** Processamento do log `_chat 10.txt` com ativação de membros silenciosos e inclusão de dados de perfil (Rebeca Madureira com reposicionamento digital, Elany Almeida com advocacia digital e mentoria para carreiras jurídicas, e outros). Sincronização do painel e balanceamento estatístico dos eixos de atuação.\n")
    
    md.append("## 🌿 Apresentação do Programa Raízes\n")
    md.append("O **Raízes** é um programa de aceleração e implementação de negócios digitais. O foco principal é apoiar você a criar seu primeiro produto e aprender as melhores estratégias de vendas para quem quer começar no digital. Escolhemos esse formato para garantir que você terá resultados. Simples assim.\n")
    md.append("São **dois os pilares principais** que trabalhamos no programa:\n")
    md.append("* 🧭 **Pilar Método:** Durante os últimos dois anos nós testamos e validamos (conosco e com nossos mentorados, em diversos nichos) as melhores estratégias para vender cursos e mentorias de uma maneira leve, sem depender de lançamentos. Tudo isso foi organizado em uma metodologia passo a passo, de rápida execução, para você colocar seus infoprodutos no ar (de cursos baratos até ofertas *High Ticket*) em tempo recorde e com resultados impressionantes.")
    md.append("* ⚡ **Pilar Execução:** 100% do conteúdo do Programa será prático. Não terá espaço para teorias e conceitualizações. Nós respeitamos seu tempo e energia, e sabemos que você precisa de resultados rápidos. Você terá acesso às nossas ferramentas exclusivas, templates de posts e páginas, automações prontas, além do nosso acompanhamento diário mágico.\n")
    
    md.append("---")
    md.append("## 📜 Diretrizes de Convivência & Atalhos do Grupo\n")
    md.append("Para manter o foco nas estratégias de negócios digitais e preservar a boa convivência do grupo, a moderação estabeleceu as seguintes diretrizes na descrição do WhatsApp:\n")
    
    md.append("### 🤝 Aqui você pode:")
    md.append("* ✅ Compartilhar suas conquistas, aprendizados, memes e conhecer melhor seus colegas.")
    md.append("* ✅ Pedir ajuda e opiniões de outros alunos sobre seu conteúdo. **Regra importante:** deixe explícita sua intenção para os colegas saberem como ajudar você, e **nunca utilize o espaço para divulgações frias**.\n")
    
    md.append("### ⚠️ Regras de Convivência (Cuidado):")
    md.append("* ❌ **É proibido** o compartilhamento de links de grupos paralelos, materiais de imersões ao vivo e/ou com direitos autorais e divulgações externas que fogem do foco da metodologia do Raízes (como pedido de ajuda para vaquinhas, propagandas políticas, etc).")
    md.append("* 💬 Dúvidas sobre conteúdo e estratégia devem ser feitas através dos comentários da plataforma oficial ou retiradas diretamente nas tutorias dos plantões de dúvidas.")
    md.append("* 🕊️ Mantenha o espaço da boa convivência: não falamos sobre política, religião, futebol ou outros tópicos que possam gerar conflitos.")
    md.append("* 💙 Seja gentil. Se tiver qualquer incômodo que não queira expressar no grupo, acione o suporte de alunos da Maré no número indicado de suporte.\n")
    
    md.append("### 🔗 Atalhos Úteis:")
    md.append("* 🤖 **Atalho da Raíza (IA):** [ia-raizes.mareeducacao.com.br](https://ia-raizes.mareeducacao.com.br/) *(use seu e-mail de cadastro do Raízes)*")
    md.append("* 🎓 **Área de Alunos (Hotmart):** [Acesso pro Raízes](https://hotmart.com/pt-br/club/mareeducacao/products/3758918)")
    md.append("* 📞 **Suporte do Raízes:** [WhatsApp (11) 5199-8656](https://wa.me/551151998656)")
    md.append("* 🚀 **PEI!**\n")
    
    md.append("---")
    md.append("## 📅 Agenda Exclusiva da Turma (Junho/26)\n")
    md.append("| Encontro / Evento | Data e Horário | Foco do Encontro |")
    md.append("| :--- | :---: | :--- |")
    md.append("| 🤩 **Boas-vindas** | **22/06** (14h - 16h) | Integração oficial e anúncio dos bônus do primeiro dia |")
    md.append("| 🔧 **Plantão Técnico (Van)** | **23/06** (09h - 11h) | Orientação sobre ferramentas e plataforma |")
    md.append("| 🤓 **Tutoria com Lore I** | **25/06** (19h30 - 21h30) | Plantão de dúvidas exclusivo de início |")
    md.append("| 🔨 **Imersão Bate Martelo (Lore)** | **30/06** (09h - 12h) | Definição e alinhamento do Nicho de Negócios |")
    md.append("| 🤓 **Tutoria com Lore II** | **02/07** (19h30 - 21h30) | Plantão de dúvidas final exclusivo da turma |")
    md.append("| 🎯 **Desafio Flecha (Sara)** | **06/07 a 10/07** (08h - 09h) | Aceleração diária de posicionamento |")
    md.append("| ✍️ **Desafio de Conteúdo (Lore)** | **13/07 a 17/07** (08h - 09h) | Emissão prática de narrativas digitais |")
    md.append("| 🔍 **Sessão de Análise (Carol)** | **20/07** (14h - 17h) | Análise aprofundada de entregáveis de alunos |")
    md.append("| 🧘 **Rotina e Produtividade (Myca)** | **04/08** (10h - 12h) | Estruturação de hábitos e alta performance |")
    md.append("| 💬 **Plantões Semanais** | **Todas as quartas** (noite) | Acompanhamento de dúvidas gerais ao vivo |\n")
    md.append("> *Obs: Todos os encontros ao vivo são gravados e sobem na Hotmart em até 24h. A participação é recomendada, mas opcional (siga sua fase).*\n")
    
    md.append("---")
    md.append("## 🌟 Cases de Sucesso & Depoimentos (Turma Junho/26)\n")
    md.append("### 🎭 A \"Estreia\" no Palco das Vendas — Arthur Martins (Ator, Diretor & Terapeuta)")
    md.append("> **\"Caramba!!! Hoje fiz minha primeira call de venda e fechei minha primeira mentorada!!! Estou em êxtase aqui!!! Destravou!!!\"**")
    md.append(">")
    md.append("> \"Sei que posso ter pulado algumas etapas, mas a urgência financeira falou alto. Segui a intuição. Peguei todas as informações assimiladas no Desafio e fui para o 'palco'.")
    md.append(">")
    md.append("> Fiz a call com uma conhecida, minha aluna de meditação. Não é a persona high ticket para a minha mentoria, porém quis fazer com ela para 'ensaiar', destravar meu medo e validar o método.")
    md.append(">")
    md.append("> Segui todo o roteiro do Flecha, com muita escuta ativa, falando sobre o que era do interesse da cliente. Travei um pouco ao apresentar a mentoria, pois quis ler direitinho o que estava escrito, mas fluiu. Quando terminei a apresentação, a cliente falou:")
    md.append("> *— Nossa, você leu meu diagnóstico?* 🤣🤣🤣")
    md.append(">")
    md.append("> A conversa seguiu mais um pouco, e eu ali, tranquilamente ansioso, esperando ela perguntar o preço. Quando finalmente a pergunta veio, eu, com toda a cara lisa do mundo, falei o preço cheio.")
    md.append(">")
    md.append("> Ela travou. Entrou em pânico e começou a se justificar, para dizer que estava fora das possibilidades dela. Eu sabia que era caro para ela mesmo, mas quis dizer o preço cheio para sentir a reação. E perceber como me sentiria ao falar um preço tão distante do que estou acostumado a cobrar.")
    md.append(">")
    md.append("> Como palhaço, sempre tenho cartas na manga. Já tinha calculado três propostas de preço para ver em qual faixa ela se sentiria mais confortável para investir, sem morrer de susto. Fui apresentando uma por uma, até chegar ao valor que foi alegre para ambos. E assim consegui fechar minha primeira venda, na primeira call, por 20% do valor cheio. Vai ser ótimo para treinar, validar o método e ganhar confiança.")
    md.append(">")
    md.append("> Ao final, ainda fiz um exercício de yoga do riso com ela para sairmos leves da reunião.")
    md.append(">")
    md.append("> Percebi, senti que este formato de trabalho com mentoria é onde todos os meus 'eus' — ator, palhaço, poeta, terapeuta Xamânico/holístico, massoterapia, líder de Yoga do riso, condutor de meditação, pai de menina e observador do viver — encontraram assento.")
    md.append(">")
    md.append("> Uau! Funciona! É real! Gratidão, Raízes! Xeros ❤️\"\n")
    
    md.append("---")
    md.append("## 📊 1. Resumo por Estado de Origem\n")
    md.append("| Estado | Quantidade | Porcentagem |")
    md.append("| :--- | :---: | :---: |")
    for s, count in sorted(state_counts.items(), key=lambda x: x[1], reverse=True):
        md.append("| {} | {} | {:.1f}% |".format(s, count, count/total_m*100))
    md.append("| **Total Geral** | **{}** | **100.0%** |\n".format(total_m))
    
    md.append("## 🎯 2. Resumo por Nicho/Habilidade Pretendida\n")
    md.append("| Nicho / Habilidade | Quantidade | Porcentagem |")
    md.append("| :--- | :---: | :---: |")
    for n, count in sorted(niche_counts.items(), key=lambda x: x[1], reverse=True):
        md.append("| {} | {} | {:.1f}% |".format(n, count, count/total_m*100))
    md.append("| **Total Geral** | **{}** | **100.0%** |\n".format(total_m))
    
    md.append("## 💤 3. Quadro de Membros Silenciosos\n")
    md.append(f"* **Membros que se apresentaram (Ativos):** {active_count} ({active_count/total_m*100:.1f}%)")
    md.append(f"* **Membros que não se manifestaram (Silenciosos):** {silent_count} ({silent_count/total_m*100:.1f}%)\n")
    
    md.append("---")
    md.append("## 🧭 3. Agrupamentos por Semelhança de Propósito (Membros Ativos)\n")
    md.append("A tribo ativa é dividida nos seguintes eixos principais de atuação:")
    md.append("1. **Gestão Feminina, Transição de Carreira & Maturidade (30+, 40+, 50+):** Foco em tirar mulheres do piloto automático ou do esgotamento corporativo, redesenhando a vida pessoal e profissional.")
    md.append("2. **Cuidado Parental & Família (TEA, TDAH, Típicas):** Apoio a pais e educadores lidando com neurodivergências infantis ou orientação de rotinas educativas.")
    md.append("3. **Neurodivergências Práticas na Vida Adulta (Dupla Excepcionalidade - 2E/TDAH):** Mentoria cognitiva e de rotinas adaptadas para adultos.")
    md.append("4. **Saúde Integrativa, Corpo & Movimento (Yoga, Ayurveda, Terapias):** Terapias holísticas, clínica moderna e yoga para equilíbrio físico e de carreira.")
    md.append("5. **Inovação Técnica de Base & Sustentabilidade (Construção, Ecologia, Agro):** Modelos ecológicos, engenharia florestal e bioeconomia circular.")
    md.append("6. **Vendas B2B & Consultoria PME:** Processos comerciais, consultoria financeira e vendas de alta performance no digital.")
    md.append("7. **Educação & Mentoria Acadêmica:** Apoio a processos seletivos de mestrado/doutorado, destrave de escrita científica/criativa, formação continuada de professores e ensino de idiomas.\n")
    
    md.append("---")
    md.append("## ⚡ 4. Sinergias e Conexões Estratégicas Internas\n")
    md.append("Conexões e convergências voltadas estritamente para estruturação de parcerias e produtos digitais no grupo:")
    md.append("1. **Fabio Takwara 🤝 Marcello Pedro 🤝 Prem Karima (Ecologia, Surf & Eventos Sustentáveis):** Marcello Pedro (professor de surf no RJ), Fabio Takwara (bambu termorretificado + PU vegetal para projetar pranchas de surf ecológicas) e Prem Karima (especialista em eventos e sustentabilidade - Método Evento Vivo). Sinergia para organizar competições e ativações de surfe ecológico e sustentabilidade no litoral.")
    md.append("2. **A Rede de Pedagogia, Apoio Parental & Cuidados Familiares (Mandy Bettega 🤝 Bruna Arciere 🤝 Luciana 🤝 Monica Marques 🤝 Aline Koller 🤝 Tatiana Fávaro Lima 🤝 Manoela Couto 🤝 Micheline 🤝 Cristiane Monteiro (Instituto FHE) 🤝 Cris Terrazzan 🤝 Isabela (Isabela Guilen)):** Integração de psicólogas, pedagogas Waldorf, especialistas em ABA e gerontólogas para fornecer materiais consolidados e suporte educacional familiar.")
    md.append("3. **Parcerias de Tecnologia, Dados & Processos (Fabio Takwara 🤝 Rodrigo Dumont 🤝 Shayenne Moura 🤝 Davi Brasil 🤝 Anderson Gonzaga 🤝 Gabriel Martens 🤝 Lucianna Alves - Mentora 🤝 Elaine Bazilio):** Sinergia entre líderes de dados, cientistas de dados e gestores de processos de TI para estruturar automações e sistemas eficientes no meio corporativo e ambiental.")
    md.append("4. **Sinergia Ayurveda, Yoga & Terapias (Carina Vieirat 🤝 Dëbora Nascı̊uti 🤝 Ju Zanella 🤝 Ju Almeida 🤝 Jordana Mol 🤝 Bruno Mazetto 🤝 Erika Thiele 🤝 Fernanda (fernanda✨️) 🤝 Giseli Paulon Ayurveda 🤝 Cristina Maria 🤝 Mari Soccol 🤝 Maria Carolina 🤝 Ludmilla Azevedo):** Colaboração entre professoras de Yoga, terapeutas Ayurveda, nutricionistas e ginecologistas integrativas para estruturação de mentorias corporativas e programas de bem-estar focados na saúde da mulher.")
    md.append("5. **Rede de Liderança Feminina & Desenvolvimento (Si Briganti 🤝 Bela Giannini 🤝 Michelle Santiago 🤝 Marcia Andrade 🤝 Psi Nara Barreto 🤝 Evelen Tomaz 🤎 🤝 Marcela Madureira 🤝 Priscila Leite 🤝 Lucia Elena 🤝 Daniel Floriani):** Cruzamento de competências de consultoras de negócios, executivas de RH, especialistas em experiência do paciente e psicólogas para criar mentorias de liderança corporativa feminina, humanização em saúde, experiência do paciente e superação de burnout.")
    md.append("6. **Sinergia Cenografia Ecológica & Estruturas Cênicas (Fabio Takwara 🤝 Hernani Albuquerque 🤝 Theo Oliveira 🤝 Arthur Martins 🤝 Alex Reis 🤝 Angelica Martins):** Conexão entre a especialidade de Fabio Takwara em cúpulas geodésicas de bambu e estruturas circenses com Hernani (Naniko's Circus), Theo e Arthur (artistas cênicos/teatro), Alex (músico) e Angelica (design visual da cena). Abre oportunidades para palcos itinerantes sustentáveis, picadeiros ecológicos e instalações cênicas modulares para espetáculos ao ar livre.")
    md.append("7. **Rede de Educação, Escrita & Mentoria Acadêmica (Ana Carolina Mattoso 🤝 Eron Villar 🤝 Alex Maciel 🤝 Fabrícia Coelho 🤝 Milena 🤝 Joey Jacksonn 🤝 Patrícia Bertachini Bissetti 🤝 Luiz Eduardo (Eduardo Rocha) 🤝 João Lima 🤝 Cristiane Silveira):** Conexão entre mentoras acadêmicas, psicopedagogas, professores e especialistas em escrita/pedagogia para a estruturação de programas de capacitação continuada, destrave de escrita acadêmica/concursos, preparação para seleções de pós-graduação e ensino de idiomas.")
    md.append("8. **Sinergia Negócios Físicos, Varejo, Estética & Escala Local (Bell Nacif 🤝 Ju Silva Estética 🤝 Adriana Gaia 🤝 Lucas Vargas):** Conexão entre especialistas de varejo e operações comerciais (Bell), consultores condominiais (Lucas), empresárias óticas (Adriana) e esteticistas estruturando modelos de negócios escaláveis (Ju). Foco em compartilhar estratégias de ponto físico, serviços locais e atração de clientes.\n")
    
    md.append("---")
    md.append("## 📋 5. Lista Geral Detalhada (Todos os Membros Mapeados)\n")
    md.append("> [!NOTE]")
    md.append("> **Censo e Nota de Metodologia:**")
    md.append("> O censo oficial do WhatsApp conta com **194 membros** no grupo. A equipe de moderação e suporte é composta por **6 integrantes**:")
    md.append("> * 👑 **Marcus** (Co-fundador / Mentor do Raízes)")
    md.append("> * 👑 **Myca** (Co-fundadora / Mentora do Raízes)")
    md.append("> * 👥 **Vanessa Fleig** (Suporte ao Aluno / Sucesso do Aluno)")
    md.append("> * 🛠️ **Suporte** (Atendimento Técnico / Suporte ao Aluno)")
    md.append("> * 📢 **Maré Educação** e **Raízes** (Contas Institucionais / Moderadores)")
    md.append("> \n")
    md.append(f"> Descontados os administradores, o grupo conta com **{total_census}** participantes. A listagem detalhada registra **{total_m}** registros devido a uma sobreposição técnica temporária (membros silenciosos que entraram mostrando apenas o número de telefone e depois interagiram usando seus nomes, ou que utilizaram duas contas distintas no processo).\n")
    
    md.append("| Nome / Identificador | Localização | Profissão Original | Instagram / Contato | Foco Principal / Status | Neurodivergência |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
    for m in mapped_members:
        md.append("| **{}** | {} | {} | {} | {} | {} |".format(m["name"], m["state"], m["prof"], m["ig"], m["desc"], m["neuro"]))
        
    return "\n".join(md)

# Write output files with specific logo paths
md_docs = build_markdown("../assets/images/raizes_logo.png")
md_raw = build_markdown("../docs/assets/images/raizes_logo.png")
md_brain = build_markdown("../assets/images/raizes_logo.png")

with open("/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/docs/raio-x-raizes.md", "w", encoding="utf-8") as out:
    out.write(md_docs)

with open("/Users/fabiotakwara/Documents/GitHub/Mentoria_Comunidades_RaioX/docs/raio-x-raizes.md", "w", encoding="utf-8") as out:
    out.write(md_docs)

with open("/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/01_TRIAGEM_BRUTA/RAIO-X_Raizes_Grupo_Junho26.md", "w", encoding="utf-8") as out:
    out.write(md_raw)

with open("/Users/fabiotakwara/.gemini/antigravity/brain/f4c5e83f-837b-47ad-a666-ce02a196ca03/RAIO-X_Raizes_Grupo_Junho26.md", "w", encoding="utf-8") as out:
    out.write(md_brain)

print("Markdown generated successfully with refined censo, program description, logo, WhatsApp rules, and clickable links!")
