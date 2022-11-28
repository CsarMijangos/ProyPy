## The following constants are the paths to the 
## data bases:

# The precharged example:

CENTRAL_DB = "data/data_bases/example/central.fasta"    #Enzime family DB
GENOMES_DB = "data/data_bases/example/17genomes.fasta"        #Genome DB
NAT_PRODS_DB = "data/data_bases/example/nat_prods.fasta"         #Natural products DB (default =MIBiG)


# The user databases

USER_CENTRAL_DB = "data/data_bases/user_data_bases/"
USER_GENOMES_DB = "data/data_bases/user_data_bases/"
USER_NAT_PRODS_DB = "data/data_bases/user_data_bases/"


## The following are the paths to the blast databases files:

##The precharged blast databases example:

CENTRAL_BLAST_DB = "data/blast_dbs/example/central_blastdb"
GENOMES_BLAST_DB = "data/blast_dbs/example/17genomes_blastdb"
NAT_PRODS_BLAST_DB = "data/blast_dbs/example/at_prods_blastdb"


#The user blast databases:

USER_CENTRAL_BLAST_DB = "data/blast_dbs/user_blastdbs/"
USER_GENOMES_BLAST_DB = "data/blast_dbs/user_blastdbs/"
USER_NAT_PRODS_BLAST_DB = "data/blast_dbs/user_blastdbs/"

## The following are the paths to the output files of blastp:

## The precharged example:

CENTRALvsGNMs_blastp = "data/blastp_files/example/blast_1.blast" # blastp of Enzime family DB to Genomes DB 
GNMsvsCENTRAL_blastp = "data/blastp_files/example/blast_2.blast" #blastp of GNM vs EF 
EXP_FAMSvsNAT_PRODS_blastp = "data/blastp_files/example/blast_3.blast"   # blastp of expanded families vs
                                   # natural products 
#The user case:

USER_CENTRALvsGNMs_blastp = "data/blastp_files/user_blastp_files/"
USER_GNMsvsCENTRAL_blastp = "data/blastp_files/user_blastp_files/"
USER_EXP_FAMSvsNAT_PRODS_blastp = "data/blastp_files/user_blastp_files/"

## The following are dictionaries with the ids of the
## enzime families, genomes and natural products:

GNMs_ids = {}
CENTRAL_ids = {}
NPs_ids = {}



