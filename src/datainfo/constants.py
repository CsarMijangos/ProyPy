## The following constants are the paths to the 
## data bases:

# The precharged example:

EXMPL_CENTRAL_DB = "data/data_bases/example/central/central.fasta"    #Enzime family DB
EXMPL_GENOMES_DB = "data/data_bases/example/genomes/17genomes.fasta"  #Genome DB
MIBiG_NAT_PRODS_DB = "data/data_bases/example/mibig/nat_prods.fasta"  #Natural products DB(default =MIBiG)


## The user databases

USER_CENTRAL_DB = "data/data_bases/user_data_bases/central/"
USER_GENOMES_DB = "data/data_bases/user_data_bases/genomes/"
USER_NAT_PRODS_DB = "data/data_bases/user_data_bases/nat_prods/"


## The following are the paths to the blast databases files:

CENTRAL_BLAST_DB = "data/blast_dbs/central/central_blastdb"
GENOMES_BLAST_DB = "data/blast_dbs/genomes/17genomes_blastdb"
NAT_PRODS_BLAST_DB = "data/blast_dbs/nat_prods/nat_prods_blastdb"


#The user blast databases:

#USER_CENTRAL_BLAST_DB = "data/blast_dbs/user_blastdbs/"
#USER_GENOMES_BLAST_DB = "data/blast_dbs/user_blastdbs/"
#USER_NAT_PRODS_BLAST_DB = "data/blast_dbs/user_blastdbs/"

## The following are the paths to the output files of blastp:

CENTRALvsGNMs_blastp = "data/blastp_files/central_to_genomes/blast_1.blast" # blastp of Enzime family DB to Genomes DB 
GNMsvsCENTRAL_blastp = "data/blastp_files/genomes_to_central/blast_2.blast" #blastp of GNM vs EF 
EXP_FAMSvsNAT_PRODS_blastp = "data/blastp_files/expFam_to_natProds/blast_3.blast"   # blastp of expanded families vs
                                                                        # natural products 



## The following are dictionaries with the ids of the
## enzime families, genomes and natural products:





#################### cmd's for using blast tools with biopython ########
CMD_blastp = "/home/csar/ncbi-blast-2.13.0+/bin/blastp"
CMD_makeblastdb = "/home/csar/ncbi-blast-2.13.0+/bin/makeblastdb"



GNMs_ids = {}
CENTRAL_ids = {}
NPs_ids = {}



