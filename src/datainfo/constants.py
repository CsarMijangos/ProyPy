## The following constants are the paths to the 
## input files:

EF_path = ""         #Enzime family DB
GNM_path = ""        #Genome DB
NP_path = ""         #Natural products DB (default =MIBiG)


## The following are the names of the dataframes of 
## the outpuuts of blastp:

DF_EFvsGNMs = blastpOf(query)

##The following are the paths to the .blast files:

EFvsGNMs_blastp = '' # blastp of Enzime family DB to Genomes DB 
GNMsvsEF_blastp = "" #blastp of GNM vs EF 

## The following are dictionaries with the ids of the
## enzime families, genomes and natural products:

GNMs_ids = {}
EF_ids = {}
NPs_ids = {}



