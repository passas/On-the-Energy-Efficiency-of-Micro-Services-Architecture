import csv

FILES = [
    '1_1_1.csv',
    '1_1_10.csv',
    '1_1_20.csv',
    '1_1_50.csv',
    '1_1_100.csv',
    '1_1_200.csv',
    '1_1_300.csv',
    '1_1_400.csv',
    '1_1_500.csv',
    '1_1_600.csv',
    '1_1_700.csv',
    '1_1_800.csv',
    '1_1_900.csv',
    '1_1_1000.csv',
]

def trata_outliers_produz_media (dados_todos, primeiro_valor=1, ultimo_valor=9):

    media = 0.0
    sem_outliers = []

    dados_todos.sort ()

    sem_outliers = dados_todos[primeiro_valor:ultimo_valor]

    floats = []
    for val in sem_outliers:
        floats.append ( float( val ) )

    sem_outliers = floats

    for val in sem_outliers:
        media += val
    media = media / len ( sem_outliers )

    return {
        "sem_outliers": sem_outliers,
        "media": media
    }

for FILE in FILES:

    analysis = {
        "monolith":
        {
            "core": [], "time": []
        },
    
        "ms":
        {
            "core": [], "time": []
        }
    }
    
    with open(FILE, newline='\n') as file:
    
        rapl = csv.reader(file, delimiter=',')
    
        i = 0
        for row in rapl:
    
            if i>= 1 and i <= 10:
                analysis["monolith"]["core"].append ( row[3] )
                analysis["monolith"]["time"].append ( row[7] )
    
            elif i>=11 and i <= 20:    
                analysis["ms"]["core"].append ( row[3] )
                analysis["ms"]["time"].append ( row[7] )
    
            i += 1
    
    print (f'** {FILE} **')
    
    r = trata_outliers_produz_media ( analysis["monolith"]["core"] )
    print (f'Monolith :: {r["media"]} Watts')
    
    r = trata_outliers_produz_media ( analysis["monolith"]["time"] )
    print (f'Monolith :: {r["media"]} ms')
    
    print ()

    r = trata_outliers_produz_media ( analysis["ms"]["core"] )
    print (f'Micro Services :: {r["media"]} Watts')
    
    r = trata_outliers_produz_media ( analysis["ms"]["time"] )
    print (f'Micro Services :: {r["media"]} ms')

    print ()

