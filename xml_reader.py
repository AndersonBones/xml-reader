from xml.dom import minidom
import os
import glob
import pandas as pd
from dict_list import pad_dict_list
# parse an xml file by name


class XML_Reader():
    def __init__(self, nfes_path) -> None:
        
        
        self.nfes_path = nfes_path 

        os.chdir(self.nfes_path)
        self.dir_parth_nfe = glob.glob('*.xml')

        self.progress = 0

        self.NFe = {
            "Chave":[],
            "Data emissão":[],
            "Nº Nota Fiscal":[],
            "Série":[],
            "Quantidade":[],
            "Valor Total":[],
            "Nº Log":[],
            "Nº Aleatório":[],
            "Dígito":[],
            "UF_Emissor":[],
            "Data extraída":[],
            "UF_Destino":[],
            "Remetente":[],
            "Tomador":[],
            "Transportadora":[],
            "NFe-Chave":[],
            "Nº NFe":[],
            "Produto":[],
            "Valor. Un":[],
        }


    
    def set_nfe_from_cte(self, cte):

        chaves_nfes = ''
        nfes = ''
        
        if cte.getElementsByTagName('nCT').length >=1:
            if cte.getElementsByTagName('infNFe').length >= 1:

                for infNfe in cte.getElementsByTagName('infNFe'):

                    nfes+=infNfe.getElementsByTagName('chave')[0].firstChild.data[28:-10]+"  "
                    chaves_nfes+=infNfe.getElementsByTagName('chave')[0].firstChild.data+"  "

                self.NFe['NFe-Chave'].append(chaves_nfes)
                self.NFe['Nº NFe'].append(nfes)
        else:

            self.NFe['NFe-Chave'].append("")
            self.NFe['Nº NFe'].append("")



    def set_n_nota_fiscal(self, nfe=[], cte=[]):
        if nfe.length >= 1:
            self.NFe['Nº Nota Fiscal'].append(nfe[0].firstChild.data)
       
        if cte.length >= 1:
            self.NFe['Nº Nota Fiscal'].append(cte[0].firstChild.data)
      


    def set_chave(self, nfe=[], cte=[]):
        if nfe.length >= 1:
            self.NFe['Chave'].append(nfe[0].firstChild.data)
       

        if cte.length >= 1:
            self.NFe['Chave'].append(cte[0].firstChild.data)
    



    def set_serie(self, nfe=[]):
        if nfe.length >= 1:
            self.NFe['Série'].append(nfe[0].firstChild.data)



    def set_quantidade(self, nfe=[], cte=[]):
        if nfe.length >= 1:
            self.NFe['Quantidade'].append(nfe[0].firstChild.data.replace('.',','))

        if cte.length >= 1:
            self.NFe['Quantidade'].append(cte[0].firstChild.data.replace('.',','))



    def set_valor_total(self,nfe=[], cte=[]):
        if nfe.length >= 1:
            self.NFe['Valor Total'].append(nfe[0].firstChild.data.replace('.',','))

        if cte.length >= 1:
            self.NFe['Valor Total'].append(cte[0].firstChild.data.replace('.',','))



    def set_n_log(self,nfe=[]):
        if nfe.length >= 1:
            self.NFe['Nº Log'].append(nfe[0].firstChild.data)


    def set_n_aleatorio(self, nfe=[], cte=[]):
        if nfe.length >= 1:
            self.NFe['Nº Aleatório'].append(nfe[0].firstChild.data)


        if cte.length >= 1:
            self.NFe['Nº Aleatório'].append(cte[0].firstChild.data)



    def set_digito(self, nfe=[]):
        if nfe.length >= 1:
            self.NFe['Dígito'].append(nfe[0].firstChild.data)


    def set_uf_emissor(self, nfe=[]):
        if nfe.length >= 1:
            if nfe[0].getElementsByTagName("UF").length >= 1:
                self.NFe['UF_Emissor'].append(nfe[0].getElementsByTagName("UF")[0].firstChild.data)


    def set_remetente(self, nfe=[], cte=[]):
        if nfe.getElementsByTagName('nNF').length >= 1:
            if nfe.getElementsByTagName('emit').length >= 1:
                if nfe.getElementsByTagName('emit')[0].getElementsByTagName("xNome").length >= 1:
                    self.NFe['Remetente'].append(nfe.getElementsByTagName('emit')[0].getElementsByTagName("xNome")[0].firstChild.data)

        if cte.length >= 1:
            if cte[0].getElementsByTagName("xNome").length >= 1:
                self.NFe['Remetente'].append(cte[0].getElementsByTagName("xNome")[0].firstChild.data)



    def set_uf_destino(self, nfe, cte=[]):
        if nfe.getElementsByTagName('nNF').length >= 1:
            if nfe.getElementsByTagName('enderDest').length >= 1:
                if nfe.getElementsByTagName('enderDest')[0].getElementsByTagName("UF").length >= 1:
                    self.NFe['UF_Destino'].append(nfe.getElementsByTagName('enderDest')[0].getElementsByTagName("UF")[0].firstChild.data)
          

        if cte.length >= 1:
            if cte[0].getElementsByTagName("UF").length >= 1:
                self.NFe['UF_Destino'].append(cte[0].getElementsByTagName("UF")[0].firstChild.data)



    def set_produto(self, nfe=[]):
        if nfe.length >= 1:
            self.NFe['Produto'].append(nfe[0].firstChild.data)
        else:
            self.NFe['Produto'].append("")

                
    
    def set_tomador(self, nfe=[]):
        if nfe.length >= 1:
            if nfe[0].getElementsByTagName("xNome").length >= 1:
                self.NFe['Tomador'].append(nfe[0].getElementsByTagName("xNome")[0].firstChild.data)


    def set_valor_un(self, nfe=[]):
        if nfe.length >= 1:
            self.NFe['Valor. Un'].append(nfe[0].firstChild.data.replace('.',','))
        else:
            self.NFe['Valor. Un'].append("")


    def set_data(self, nfe=[]):
        if nfe.length >= 1:
            self.NFe['Data emissão'].append(nfe[0].firstChild.data)
            self.NFe['Data extraída'].append(nfe[0].firstChild.data[0:10].replace('-','.'))


    def set_transportadora(self, cte=[]):
        if cte.getElementsByTagName('nCT').length >= 1:
            if cte.getElementsByTagName("emit").length >= 1:
                if cte.getElementsByTagName("emit")[0].getElementsByTagName("xNome").length >= 1:
                    self.NFe['Transportadora'].append(cte.getElementsByTagName("emit")[0].getElementsByTagName("xNome")[0].firstChild.data)
        
        else:
            self.NFe['Transportadora'].append("")

    def setValues(self):

        for file in self.dir_parth_nfe:
        
            try:

                self.set_nfe_from_cte(
                    cte=minidom.parse(fr'{self.nfes_path}\{file}')
                )

                self.set_transportadora(
                    cte=minidom.parse(fr'{self.nfes_path}\{file}')
                )

                self.set_produto(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName("xProd")
                )
                self.set_uf_destino(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}'),
                    cte=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('enderReme')
                )

                self.set_remetente(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}'),
                    cte=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('rem')
                )
          
               
                self.set_tomador(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('dest'),
                )


                self.set_valor_un(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName("vUnCom")
                )
               
            
                self.set_data(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('dhEmi')
                )
               

                self.set_chave(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('chNFe'),
                    cte=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('chCTe')
                )
                self.set_n_nota_fiscal(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('nNF'),
                    cte=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('nCT')    
                )

                self.set_serie(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('serie'),
                )
                
                self.set_quantidade(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('qCom'),
                    cte=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('qCarga')
                )


                self.set_valor_total(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('vNF'),
                    cte=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('vRec')
                )
                
                self.set_n_log(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('nProt'),
                )
             

                self.set_n_aleatorio(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('cNF'),
                    cte=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('cCT')
                )
                
                self.set_digito(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('cDV'),
                )

                self.set_uf_emissor(
                    nfe=minidom.parse(fr'{self.nfes_path}\{file}').getElementsByTagName('enderEmit'),

                )
        

                self.progress+=1

            except Exception as error:
            
                print('Erro', error)
                


    

    def to_data_frame(self):
        self.newNfe = pad_dict_list(self.NFe)
        self.df_nfe = pd.DataFrame.from_dict(self.newNfe)
        self.progress+=1
    
    def export_file(self, output_path):
        self.df_nfe.to_excel(output_path, index=False, sheet_name='Notas Fiscais')
        self.progress+=1

    def run(self):

        self.setValues()
        self.to_data_frame()
     
        
