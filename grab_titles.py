import pandas as pd

url = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_'

def obtener_datos(url):
    """TODO: Detallar función
    
    Arguments:
        url {str} -- Cadena que contendrá la dirección desde donde se quieren
                     obtener los datos
    
    Returns:
        pandas.DataFrame -- Conjunto de datos que contendrá las tablas de las
                            urls enviadas
    """
    datos = pd.read_html(url, header=0)
    for tabla in datos:
        if tabla.shape[1] == 3:
            datos = tabla
            break
    datos = datos.drop(columns=datos.columns[0])
    return datos

anos_datos = []
for i in range(1959, 2018):
    nueva_url = "{}{}".format(url, i)
    my_df = obtener_datos(nueva_url)
    
    if my_df.shape[1] != 2:
        print("error en el año {}".format(i))
        print(my_df.shape)
        quit()

    for j, col in enumerate(my_df.columns):
        my_df.iloc[:, j] = my_df.iloc[:, j].str.replace('"', '')

    my_df['Año'] = i
    anos_datos.append(my_df)

tabla_final = pd.concat(anos_datos, ignore_index=True)

print(tabla_final)
print(anos_datos[0])

tabla_final.to_csv('lista_de_canciones.csv', 
                   columns=['Año', 'Title', 'Artist(s)'], index=False)
