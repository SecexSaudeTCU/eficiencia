"""
Constantes utilizadas no projeto.
"""

import pathlib
import os


# String do ano dos dados
ANO = '2019'

# Obtem diretório raiz do projeto
DIRETORIO_RAIZ_PROJETO = pathlib.Path(__file__).parent.parent

# "String" do PATH já pré-existente de localização dos dados originais
DIRETORIO_DADOS_ORIGINAIS = os.path.join(str(DIRETORIO_RAIZ_PROJETO), 'dados', 'originais')

# "String" do PATH de localização dos dados intermediários
DIRETORIO_DADOS_INTERMEDIARIOS = os.path.join(str(DIRETORIO_RAIZ_PROJETO), 'dados', 'intermediarios')
# Cria "DIRETORIO_DADOS_INTERMEDIARIOS" se não existente
if not os.path.exists(DIRETORIO_DADOS_INTERMEDIARIOS):
    os.makedirs(DIRETORIO_DADOS_INTERMEDIARIOS)

# "String" do PATH de localização dos resultados
DIRETORIO_DADOS_RESULTADOS = os.path.join(str(DIRETORIO_RAIZ_PROJETO), 'dados', 'resultados')
# Cria "DIRETORIO_DADOS_RESULTADOS" se não existente
if not os.path.exists(DIRETORIO_DADOS_RESULTADOS):
    os.makedirs(DIRETORIO_DADOS_RESULTADOS)

# Mapeamento entre UF e reigão
UF_REGIAO = {'MS': 'Centro-Oeste', 'DF': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'GO': 'Centro-Oeste',
             'PE': 'Nordeste', 'SE': 'Nordeste', 'BA': 'Nordeste', 'AL': 'Nordeste', 'MA': 'Nordeste',
             'PI': 'Nordeste', 'PB': 'Nordeste', 'CE': 'Nordeste', 'RN': 'Nordeste', 'AC': 'Norte', 'AM': 'Norte',
             'AP': 'Norte', 'PA': 'Norte', 'RR': 'Norte', 'RO': 'Norte', 'TO': 'Norte', 'SP': 'Sudeste',
             'ES': 'Sudeste', 'RJ': 'Sudeste', 'MG': 'Sudeste', 'PR': 'Sul', 'SC': 'Sul', 'RS': 'Sul'}

# Mapeamento entre natureza jurídica e esfera da federação, quando aplicável
NATJUR_ESFERA = {'1. ADMINISTRAÇÃO PÚBLICA': 'OUTROS', '101-5 ÓRGÃO PÚBLICO DO PODER EXECUTIVO FEDERAL': 'FEDERAL',
                 '102-3 ÓRGÃO PÚBLICO DO PODER EXECUTIVO ESTADUAL OU DO DISTRITO FEDERAL': 'ESTADUAL',
                 '103-1 ÓRGÃO PÚBLICO DO PODER EXECUTIVO MUNICIPAL': 'MUNICIPAL',
                 '104-0 ÓRGÃO PÚBLICO DO PODER LEGISLATIVO FEDERAL': 'FEDERAL',
                 '105-8 ÓRGÃO PÚBLICO DO PODER LEGISLATIVO ESTADUAL OU DO DISTRITO FEDERAL': 'ESTADUAL',
                 '106-6 ÓRGÃO PÚBLICO DO PODER LEGISLATIVO MUNICIPAL': 'MUNICIPAL',
                 '107-4 ÓRGÃO PÚBLICO DO PODER JUDICIÁRIO FEDERAL': 'FEDERAL',
                 '108-2 ÓRGÃO PÚBLICO DO PODER JUDICIÁRIO ESTADUAL': 'ESTADUAL', '110-4 AUTARQUIA FEDERAL': 'FEDERAL',
                 '111-2 AUTARQUIA ESTADUAL OU DO DISTRITO FEDERAL': 'ESTADUAL',
                 '112-0 AUTARQUIA MUNICIPAL': 'MUNICIPAL',
                 '113-9 FUNDAÇÃO PÚBLICA DE DIREITO PÚBLICO FEDERAL': 'FEDERAL',
                 '114-7 FUNDAÇÃO PÚBLICA DE DIREITO PÚBLICO ESTADUAL OU DO DISTRITO FEDERAL': 'ESTADUAL',
                 '115-5 FUNDAÇÃO PÚBLICA DE DIREITO PÚBLICO MUNICIPAL': 'MUNICIPAL',
                 '116-3 ÓRGÃO PÚBLICO AUTÔNOMO FEDERAL': 'FEDERAL',
                 '117-1 ÓRGÃO PÚBLICO AUTÔNOMO ESTADUAL OU DO DISTRITO FEDERAL': 'ESTADUAL',
                 '118-0 ÓRGÃO PÚBLICO AUTÔNOMO MUNICIPAL': 'MUNICIPAL', '119-8 COMISSÃO POLINACIONAL': 'OUTROS',
                 '120-1 FUNDO PÚBLICO': 'OUTROS',
                 '121-0 CONSÓRCIO PÚBLICO DE DIREITO PÚBLICO (ASSOCIAÇÃO PÚBLICA)': 'OUTROS',
                 '122-8 CONSÓRCIO PÚBLICO DE DIREITO PRIVADO': 'OUTROS', '123-6 ESTADO OU DISTRITO FEDERAL': 'ESTADUAL',
                 '124-4 MUNICÍPIO': 'MUNICIPAL', '125-2 FUNDAÇÃO PÚBLICA DE DIREITO PRIVADO FEDERAL': 'FEDERAL',
                 '126-0 FUNDAÇÃO PÚBLICA DE DIREITO PRIVADO ESTADUAL OU DO DISTRITO FEDERAL': 'ESTADUAL',
                 '127-9 FUNDAÇÃO PÚBLICA DE DIREITO PRIVADO MUNICIPAL': 'MUNICIPAL',
                 '2. ENTIDADES EMPRESARIAIS': 'OUTROS',
                 '201-1 EMPRESA PÚBLICA': 'OUTROS', '203-8 SOCIEDADE DE ECONOMIA MISTA': 'OUTROS',
                 '204-6 SOCIEDADE ANÔNIMA ABERTA': 'OUTROS', '205-4 SOCIEDADE ANÔNIMA FECHADA': 'OUTROS',
                 '206-2 SOCIEDADE EMPRESÁRIA LIMITADA': 'OUTROS',
                 '207-0 SOCIEDADE EMPRESÁRIA EM NOME COLETIVO': 'OUTROS',
                 '208-9 SOCIEDADE EMPRESÁRIA EM COMANDITA SIMPLES': 'OUTROS',
                 '209-7 SOCIEDADE EMPRESÁRIA EM COMANDITA POR AÇÕES': 'OUTROS',
                 '212-7 SOCIEDADE EM CONTA DE PARTICIPAÇÃO': 'OUTROS', '213-5 EMPRESÁRIO (INDIVIDUAL)': 'OUTROS',
                 '214-3 COOPERATIVA': 'OUTROS', '215-1 CONSÓRCIO DE SOCIEDADES': 'OUTROS',
                 '216-0 GRUPO DE SOCIEDADES': 'OUTROS',
                 '217-8 ESTABELECIMENTO, NO BRASIL, DE SOCIEDADE ESTRANGEIRA': 'OUTROS',
                 '219-4 ESTABELECIMENTO, NO BRASIL, DE EMPRESA BINACIONAL ARGENTINO-BRASILEIRA': 'OUTROS',
                 '221-6 EMPRESA DOMICILIADA NO EXTERIOR': 'OUTROS', '222-4 CLUBE/FUNDO DE INVESTIMENTO': 'OUTROS',
                 '223-2 SOCIEDADE SIMPLES PURA': 'OUTROS', '224-0 SOCIEDADE SIMPLES LIMITADA': 'OUTROS',
                 '225-9 SOCIEDADE SIMPLES EM NOME COLETIVO': 'OUTROS',
                 '226-7 SOCIEDADE SIMPLES EM COMANDITA SIMPLES': 'OUTROS', '227-5 EMPRESA BINACIONAL': 'OUTROS',
                 '228-3 CONSÓRCIO DE EMPREGADORES': 'OUTROS', '229-1 CONSÓRCIO SIMPLES': 'OUTROS',
                 '230-5 EMPRESA INDIVIDUAL DE RESPONSABILIDADE LIMITADA (DE NATUREZA EMPRESÁRIA)': 'OUTROS',
                 '231-3 EMPRESA INDIVIDUAL DE RESPONSABILIDADE LIMITADA (DE NATUREZA SIMPLES)': 'OUTROS',
                 '232-1 SOCIEDADE UNIPESSOAL DE ADVOGADOS': 'OUTROS', '233-0 COOPERATIVAS DE CONSUMO': 'OUTROS',
                 '3. ENTIDADES SEM FINS LUCRATIVOS': 'OUTROS',
                 '303-4 SERVIÇO NOTARIAL E REGISTRAL (CARTÓRIO)': 'OUTROS', '306-9 FUNDAÇÃO PRIVADA': 'OUTROS',
                 '307-7 SERVIÇO SOCIAL AUTÔNOMO': 'OUTROS', '308-5 CONDOMÍNIO EDILÍCIO': 'OUTROS',
                 '310-7 COMISSÃO DE CONCILIAÇÃO PRÉVIA': 'OUTROS', '311-5 ENTIDADE DE MEDIAÇÃO E ARBITRAGEM': 'OUTROS',
                 '313-1 ENTIDADE SINDICAL': 'OUTROS',
                 '320-4 ESTABELECIMENTO, NO BRASIL, DE FUNDAÇÃO OU ASSOCIAÇÃO ESTRANGEIRAS': 'OUTROS',
                 '321-2 FUNDAÇÃO OU ASSOCIAÇÃO DOMICILIADA NO EXTERIOR': 'OUTROS',
                 '322-0 ORGANIZAÇÃO RELIGIOSA': 'OUTROS', '323-9 COMUNIDADE INDÍGENA': 'OUTROS',
                 '324-7 FUNDO PRIVADO': 'OUTROS', '325-5 ÓRGÃO DE DIREÇÃO NACIONAL DE PARTIDO POLÍTICO': 'OUTROS',
                 '326-3 ÓRGÃO DE DIREÇÃO REGIONAL DE PARTIDO POLÍTICO': 'OUTROS',
                 '327-1 ÓRGÃO DE DIREÇÃO LOCAL DE PARTIDO POLÍTICO': 'OUTROS',
                 '328-0 COMITÊ FINANCEIRO DE PARTIDO POLÍTICO': 'OUTROS',
                 '329-8 FRENTE PLEBISCITÁRIA OU REFERENDÁRIA': 'OUTROS', '330-6 ORGANIZAÇÃO SOCIAL (OS)': 'OUTROS',
                 '331-0 DEMAIS CONDOMÍNIOS': 'OUTROS', '399-9 ASSOCIAÇÃO PRIVADA': 'OUTROS',
                 '4. PESSOAS FÍSICAS': 'OUTROS', '401-4 EMPRESA INDIVIDUAL IMOBILIÁRIA': 'OUTROS',
                 '402-2 SEGURADO ESPECIAL': 'OUTROS', '408-1 CONTRIBUINTE INDIVIDUAL': 'OUTROS',
                 '409-0 CANDIDATO A CARGO POLÍTICO ELETIVO': 'OUTROS', '411-1 LEILOEIRO': 'OUTROS',
                 '412-4 PRODUTOR RURAL (PESSOA FÍSICA)': 'OUTROS',
                 '5. ORGANIZAÇÕES INTERNACIONAIS E OUTRAS INSTITUIÇÕES EXTRATERRITORIAIS': 'OUTROS',
                 '501-0 ORGANIZAÇÃO INTERNACIONAL': 'OUTROS', '502-9 REPRESENTAÇÃO DIPLOMÁTICA ESTRANGEIRA': 'OUTROS',
                 '503-7 OUTRAS INSTITUIÇÕES EXTRATERRITORIAIS': 'OUTROS', 'NÃO ESPECIFICADO OU IGNORADO': 'OUTROS'}

# Mapeamento entre natureza jurídica e tipo de administrção pública DIRETA x INDIRETA
NATJUR_TIPO_ADMIN_PUB = {'1. ADMINISTRAÇÃO PÚBLICA': 'OUTROS',
                         '101-5 ÓRGÃO PÚBLICO DO PODER EXECUTIVO FEDERAL': 'DIRETA',
                         '102-3 ÓRGÃO PÚBLICO DO PODER EXECUTIVO ESTADUAL OU DO DISTRITO FEDERAL': 'DIRETA',
                         '103-1 ÓRGÃO PÚBLICO DO PODER EXECUTIVO MUNICIPAL': 'DIRETA',
                         '104-0 ÓRGÃO PÚBLICO DO PODER LEGISLATIVO FEDERAL': 'DIRETA',
                         '105-8 ÓRGÃO PÚBLICO DO PODER LEGISLATIVO ESTADUAL OU DO DISTRITO FEDERAL': 'DIRETA',
                         '106-6 ÓRGÃO PÚBLICO DO PODER LEGISLATIVO MUNICIPAL': 'DIRETA',
                         '107-4 ÓRGÃO PÚBLICO DO PODER JUDICIÁRIO FEDERAL': 'DIRETA',
                         '108-2 ÓRGÃO PÚBLICO DO PODER JUDICIÁRIO ESTADUAL': 'DIRETA',
                         '110-4 AUTARQUIA FEDERAL': 'INDIRETA',
                         '111-2 AUTARQUIA ESTADUAL OU DO DISTRITO FEDERAL': 'INDIRETA',
                         '112-0 AUTARQUIA MUNICIPAL': 'INDIRETA',
                         '113-9 FUNDAÇÃO PÚBLICA DE DIREITO PÚBLICO FEDERAL': 'INDIRETA',
                         '114-7 FUNDAÇÃO PÚBLICA DE DIREITO PÚBLICO ESTADUAL OU DO DISTRITO FEDERAL': 'INDIRETA',
                         '115-5 FUNDAÇÃO PÚBLICA DE DIREITO PÚBLICO MUNICIPAL': 'INDIRETA',
                         '116-3 ÓRGÃO PÚBLICO AUTÔNOMO FEDERAL': 'DIRETA',
                         '117-1 ÓRGÃO PÚBLICO AUTÔNOMO ESTADUAL OU DO DISTRITO FEDERAL': 'DIRETA',
                         '118-0 ÓRGÃO PÚBLICO AUTÔNOMO MUNICIPAL': 'DIRETA',
                         '119-8 COMISSÃO POLINACIONAL': 'OUTROS', '120-1 FUNDO PÚBLICO': 'INDIRETA',
                         '121-0 CONSÓRCIO PÚBLICO DE DIREITO PÚBLICO (ASSOCIAÇÃO PÚBLICA)': 'OUTROS',
                         '122-8 CONSÓRCIO PÚBLICO DE DIREITO PRIVADO': 'INDIRETA',
                         '123-6 ESTADO OU DISTRITO FEDERAL': 'DIRETA', '124-4 MUNICÍPIO': 'DIRETA',
                         '125-2 FUNDAÇÃO PÚBLICA DE DIREITO PRIVADO FEDERAL': 'INDIRETA',
                         '126-0 FUNDAÇÃO PÚBLICA DE DIREITO PRIVADO ESTADUAL OU DO DISTRITO FEDERAL': 'INDIRETA',
                         '127-9 FUNDAÇÃO PÚBLICA DE DIREITO PRIVADO MUNICIPAL': 'INDIRETA',
                         '2. ENTIDADES EMPRESARIAIS': 'OUTROS', '201-1 EMPRESA PÚBLICA': 'INDIRETA',
                         '203-8 SOCIEDADE DE ECONOMIA MISTA': 'INDIRETA',
                         '204-6 SOCIEDADE ANÔNIMA ABERTA': 'OUTROS', '205-4 SOCIEDADE ANÔNIMA FECHADA': 'OUTROS',
                         '206-2 SOCIEDADE EMPRESÁRIA LIMITADA': 'OUTROS',
                         '207-0 SOCIEDADE EMPRESÁRIA EM NOME COLETIVO': 'OUTROS',
                         '208-9 SOCIEDADE EMPRESÁRIA EM COMANDITA SIMPLES': 'OUTROS',
                         '209-7 SOCIEDADE EMPRESÁRIA EM COMANDITA POR AÇÕES': 'OUTROS',
                         '212-7 SOCIEDADE EM CONTA DE PARTICIPAÇÃO': 'OUTROS',
                         '213-5 EMPRESÁRIO (INDIVIDUAL)': 'OUTROS', '214-3 COOPERATIVA': 'OUTROS',
                         '215-1 CONSÓRCIO DE SOCIEDADES': 'OUTROS', '216-0 GRUPO DE SOCIEDADES': 'OUTROS',
                         '217-8 ESTABELECIMENTO, NO BRASIL, DE SOCIEDADE ESTRANGEIRA': 'OUTROS',
                         '219-4 ESTABELECIMENTO, NO BRASIL, DE EMPRESA BINACIONAL ARGENTINO-BRASILEIRA': 'OUTROS',
                         '221-6 EMPRESA DOMICILIADA NO EXTERIOR': 'OUTROS',
                         '222-4 CLUBE/FUNDO DE INVESTIMENTO': 'OUTROS', '223-2 SOCIEDADE SIMPLES PURA': 'OUTROS',
                         '224-0 SOCIEDADE SIMPLES LIMITADA': 'OUTROS',
                         '225-9 SOCIEDADE SIMPLES EM NOME COLETIVO': 'OUTROS',
                         '226-7 SOCIEDADE SIMPLES EM COMANDITA SIMPLES': 'OUTROS',
                         '227-5 EMPRESA BINACIONAL': 'OUTROS', '228-3 CONSÓRCIO DE EMPREGADORES': 'OUTROS',
                         '229-1 CONSÓRCIO SIMPLES': 'OUTROS',
                         '230-5 EMPRESA INDIVIDUAL DE RESPONSABILIDADE LIMITADA (DE NATUREZA EMPRESÁRIA)': 'OUTROS',
                         '231-3 EMPRESA INDIVIDUAL DE RESPONSABILIDADE LIMITADA (DE NATUREZA SIMPLES)': 'OUTROS',
                         '232-1 SOCIEDADE UNIPESSOAL DE ADVOGADOS': 'OUTROS',
                         '233-0 COOPERATIVAS DE CONSUMO': 'OUTROS', '3. ENTIDADES SEM FINS LUCRATIVOS': 'OUTROS',
                         '303-4 SERVIÇO NOTARIAL E REGISTRAL (CARTÓRIO)': 'OUTROS',
                         '306-9 FUNDAÇÃO PRIVADA': 'OUTROS', '307-7 SERVIÇO SOCIAL AUTÔNOMO': 'OUTROS',
                         '308-5 CONDOMÍNIO EDILÍCIO': 'OUTROS', '310-7 COMISSÃO DE CONCILIAÇÃO PRÉVIA': 'OUTROS',
                         '311-5 ENTIDADE DE MEDIAÇÃO E ARBITRAGEM': 'OUTROS', '313-1 ENTIDADE SINDICAL': 'OUTROS',
                         '320-4 ESTABELECIMENTO, NO BRASIL, DE FUNDAÇÃO OU ASSOCIAÇÃO ESTRANGEIRAS': 'OUTROS',
                         '321-2 FUNDAÇÃO OU ASSOCIAÇÃO DOMICILIADA NO EXTERIOR': 'OUTROS',
                         '322-0 ORGANIZAÇÃO RELIGIOSA': 'OUTROS', '323-9 COMUNIDADE INDÍGENA': 'OUTROS',
                         '324-7 FUNDO PRIVADO': 'OUTROS',
                         '325-5 ÓRGÃO DE DIREÇÃO NACIONAL DE PARTIDO POLÍTICO': 'OUTROS',
                         '326-3 ÓRGÃO DE DIREÇÃO REGIONAL DE PARTIDO POLÍTICO': 'OUTROS',
                         '327-1 ÓRGÃO DE DIREÇÃO LOCAL DE PARTIDO POLÍTICO': 'OUTROS',
                         '328-0 COMITÊ FINANCEIRO DE PARTIDO POLÍTICO': 'OUTROS',
                         '329-8 FRENTE PLEBISCITÁRIA OU REFERENDÁRIA': 'OUTROS',
                         '330-6 ORGANIZAÇÃO SOCIAL (OS)': 'OUTROS', '331-0 DEMAIS CONDOMÍNIOS': 'OUTROS',
                         '399-9 ASSOCIAÇÃO PRIVADA': 'OUTROS', '4. PESSOAS FÍSICAS': 'OUTROS',
                         '401-4 EMPRESA INDIVIDUAL IMOBILIÁRIA': 'OUTROS', '402-2 SEGURADO ESPECIAL': 'OUTROS',
                         '408-1 CONTRIBUINTE INDIVIDUAL': 'OUTROS',
                         '409-0 CANDIDATO A CARGO POLÍTICO ELETIVO': 'OUTROS', '411-1 LEILOEIRO': 'OUTROS',
                         '412-4 PRODUTOR RURAL (PESSOA FÍSICA)': 'OUTROS',
                         '5. ORGANIZAÇÕES INTERNACIONAIS E OUTRAS INSTITUIÇÕES EXTRATERRITORIAIS': 'OUTROS',
                         '501-0 ORGANIZAÇÃO INTERNACIONAL': 'OUTROS',
                         '502-9 REPRESENTAÇÃO DIPLOMÁTICA ESTRANGEIRA': 'OUTROS',
                         '503-7 OUTRAS INSTITUIÇÕES EXTRATERRITORIAIS': 'OUTROS',
                         'NÃO ESPECIFICADO OU IGNORADO': 'OUTROS'}
