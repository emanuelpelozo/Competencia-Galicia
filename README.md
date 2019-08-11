# Competencia-Galicia

Conversión es que el cliente haya realizado la acción que el banco quiere predecir. Existe un registro en el dataset de conversiones por cada mes que cada cliente realizó esa acción durante 2018. La ausencia de registro en ese dataset implica que el cliente no realizó la acción en todo el período.
Un mismo USER_ID puede convertir varias veces en el año

El desafío es usar datos de 2018 para predecir 3 meses para adelante. El kernel entrena en datos hasta septiembre de 2018 con el Target de conversión entre octubre y diciembre. Luego se usan todos los datos del año para predecir 1Q2019

La mayoría de los registros en device_data se pueden cruzar con pageviews por los campos USER_ID y FEC_EVENT. Supongo que con eso lo que obtenés es qué PAGE usaron para ingresar a la plataforma.

Descripción de los Datos

    pageviews.csv - Los datos de navegación de 2018
        USER_ID - Id del usuario
        FEC_EVENT - Fecha
        PAGE - código de la página
        CONTENT_CATEGORY - Categoría de la pagina
        CONTENT_CATEGORY_TOP - Categoría de mas alto rango para la pagina
        CONTENT_CATEGORY_BOTTOM - Categoría de mas bajo rango para la pagina
        SITE_ID - Id del sitio visitado
        ON_SITE_SEARCH_TERM - Palabra clave buscada

    device_data.csv - Datos de los dispositivos asociados a los usuarios
        USER_ID - Id del usuario
        FEC_EVENT - Fecha
        CONNECTION_SPEED - Categoría de conexión
        IS_MOBILE_DEVICE - Categoría de si es telefono móvil o no
    sampleSubmission.csv - un ejemplo de entrega correcta

Archivos con descripciones textuales de variables categoricas

    CONTENT_CATEGORY.csv
    CONTENT_CATEGORY_TOP.csv
    CONTENT_CATEGORY_BOTTOM.csv
    SITE_ID.csv

