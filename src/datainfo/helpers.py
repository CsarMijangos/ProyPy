def bitscore_filter(data, threshold):
    '''This function filters those genomes in data (data = EFvsGNMs_blastp)
    such that their bitscore is greater or equal to threshold.
    '''
    data.query("bitscore >= @threshold", inplace = True)
    data.reset_index(drop=True, inplace=True)
    return data

def blastpOf(query_path,db_path):
    '''
    This function is responsible of all related to the 
    correct applying of blastp.
    '''
    

def makeblast_db(db_path):
    '''
     
    '''
    
    