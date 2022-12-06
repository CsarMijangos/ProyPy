import constants 
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast.Applications import NcbimakeblastdbCommandline 


class EvoMining:
    def __init__(self, central_path = constants.CENTRAL_DB,
                genomes_path = constants.GENOMES_DB,
                nat_prods_path = constants.NAT_PRODS_DB):
        self.central_path = central_path
        self.genomes_path = genomes_path
        self.nat_prods_path = nat_prods_path
    
    def setup_dbs(self, new_central_path,
                 new_genomes_path,
                 new_nat_prods_path):
        self.central_path = new_central_path
        self.genomes_path = new_genomes_path
        self.nat_prods_path = new_nat_prods_path
    
    def _makeblast_DBs(self):
        list_dbs = [self.central_path, self.genomes_path, self.nat_prods_path]
        lista_names = ["central", "genomes", "nat_prods"]
        if list_dbs == [constants.CENTRAL_DB, constants.GENOMES_DB, constants.NAT_PRODS_DB]:
            for db in list_dbs:
                cline_mkdb = NcbimakeblastdbCommandline(cmd = constants.CMD_makeblastdb,
                                                dbtype="prot",
                                                input_file= db,
                                                out = "data/blast_dbs/example/"+lista_names)






    
    
    