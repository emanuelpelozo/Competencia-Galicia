# Competencia-Galicia

Conversión es que el cliente haya realizado la acción que el banco quiere predecir. Existe un registro en el dataset de conversiones por cada mes que cada cliente realizó esa acción durante 2018. La ausencia de registro en ese dataset implica que el cliente no realizó la acción en todo el período.
Un mismo USER_ID puede convertir varias veces en el año

El desafío es usar datos de 2018 para predecir 3 meses para adelante. El kernel entrena en datos hasta septiembre de 2018 con el Target de conversión entre octubre y diciembre. Luego se usan todos los datos del año para predecir 1Q2019

La mayoría de los registros en device_data se pueden cruzar con pageviews por los campos USER_ID y FEC_EVENT. Supongo que con eso lo que obtenés es qué PAGE usaron para ingresar a la plataforma.
