import pandas as pd
import numpy as np

def generar_dataframes_ventana(numero_ventana,dataframe):
    
    if numero_ventana == 4 :   #Para la ventana 4 se necesitan los 11 mil usuarios existentes
        df = pd.read_csv("../data/users.csv", dtype = {"USER_ID": "category"}, index_col = 0)
    
    else:    
        condicion = dataframe["trimestre"] == numero_ventana
        df = dataframe[condicion]["USER_ID"].drop_duplicates().to_frame().set_index("USER_ID").copy()
    
    return df.sort_index()
    
    
    
def feature_ya_generado(nombre_feature, trimestre):
    """Corrobora si un feature ya fue generado """
    
    #Obtengo las columnas que genera ese feature
    columnas = DATOS_FEATURES[nombre_feature][POS_COLUMNAS_DEL_FEATURE]
    for columna in columnas:
        if columna in FEATURES_YA_GENERADOS[trimestre]:
            return True
    return False


def generar_features_faltantes(dataframe,destino,trimestre):
    """
    Funcion para generar los features faltantes para un trimestre, 
    evita la repeticion de calculo de features si estos ya se encuentran generados.
    
    dataframe: Dataframe a partir de cual se calcularan los features.
    destino: Diccionario de ventanas para los que calcular los features.
    trimestre: Numero de ventana a partir de la cual se calculan los features.
    """
    
    for nombre_feature in FUNCIONES_FEATURES:    
        if feature_ya_generado(nombre_feature, trimestre):
            continue

        #Si no fueron generados, los genero y actualizo el listado:   
        generar_feature_en_ventana(dataframe,trimestre, nombre_feature, destino)   
        
        #Agrego las columnas nuevas al diccionario
        columnas_generadas = DATOS_FEATURES[nombre_feature][POS_COLUMNAS_DEL_FEATURE]
        FEATURES_YA_GENERADOS[trimestre].extend(columnas_generadas)
    return

def generar_feature_en_ventana(dataframe,trimestre, nombre_feature, destino):
    """Genera un feature en la ventana correspondiente, con los tipos de datos correspondientes"""
    
    #Calculo el feature
    funcion_feature = FUNCIONES_FEATURES[nombre_feature]
    dataframe = funcion_feature( dataframe[dataframe["trimestre"] == trimestre] )
    
    #Uno los features nuevos con los viejos
    dataframe = destino[trimestre].merge(dataframe, left_index = True, right_index= True, how = 'left')
    
    #Rello los nans, si es que los hubiera
    dataframe = dar_formato_al_feature_nuevo(dataframe,nombre_feature)
    
    destino[trimestre] = dataframe
    
    return
 
        
   
    
    
def dar_formato_al_feature_nuevo(dataframe, nombre_feature):
    """Rellena los Nans de un dataframe con features nuevos"""
    
    
    #Datos para rellenar los Nan
    columnas = DATOS_FEATURES[nombre_feature][POS_COLUMNAS_DEL_FEATURE]
    tipo_dato= DATOS_FEATURES[nombre_feature][POS_TIPO_DATO]
    valor_nan = DATOS_FEATURES[nombre_feature][POS_DATO_NAN]
    
    dataframe.fillna(valor_nan, inplace = True)
    dataframe[columnas] = dataframe[columnas].astype(tipo_dato)
    
    return dataframe

        
