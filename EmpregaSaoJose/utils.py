def calcular_data(self, data):
    '''
        Função para calcular a distancia entre duas datas
    '''
    
    dataPublicacao = datetime.date(
        day = int( data[0:2] ), 
        month = int( data[3:5] ), 
        year = int( data[-4:] ) 
    )
    hoje = datetime.date.today()
    
    return (hoje - dataPublicacao).days
