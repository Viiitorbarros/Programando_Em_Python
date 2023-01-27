import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base (self):
        indice_interrogação = self.url.find('?')
        ulr_base = self.url[:indice_interrogação]
        return ulr_base

    def get_url_parametros(self):
        indice_interrogação = self.url.find('?')
        url_parametros = self.url[indice_interrogação+1:]
        return url_parametros

    def get_valor_parametro(self,parametro_Busca):
        indice_parametro = self.get_url_parametros().find(parametro_Busca)
        indice_valor = indice_parametro + len(parametro_Busca) + 1
        indice_e_Comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_Comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_Comercial]
        return valor

    def get_coversao(self):
        if moeda_origem == 'real' and moeda_destino == 'dolar' :
          Novo_Valor =  VALOR_DOLAR / int(quantidade)
          print (f'{quantidade}R$ equivalem a {Novo_Valor}US$')

        elif moeda_origem == 'dolar' and moeda_destino == 'real':
          Novo_Valor = VALOR_DOLAR * int(quantidade)
          print (f'{quantidade}US$ equivalem a {Novo_Valor}R$')


    def __len__(self):
        return len(self.url)

    #def __str__(self):
        #return self.url + "\n" + 'Parametros:' + self.get_url_parametros() +'\n' + 'URL Base:' + self.get_url_base()


extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real")

VALOR_REAL = 1
VALOR_DOLAR = 5.5  # 1 dólar = 5.50 reais

moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")
#CONVERSAO
Conversao = extrator_url.get_coversao()

