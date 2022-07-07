from Bio import SeqIO
import re

re_string = "\|(.+)\|"

def parse_file(path, dom_type):
    for record in SeqIO.parse(path, "fasta"):
        if "XXX" in record.seq:
            raw_desc = record.description.replace(record.name+" ", "")
            raw_desc = raw_desc.replace(",", "")
            result = re.search(re_string, record.name)
            uniprot_id = result.group(1)
            for m in re.finditer(r'X{3,}', str(record.seq)):
                print(uniprot_id+"\tIPRXXXXXX\t"+raw_desc+"\t"+dom_type+"\t" +
                      str(m.start()+1)+"\t"+str(m.end()+1))
            # return()


parse_file("G:/diss/"
           "uniprot_trembl_masked.fasta", "LowComplexity")
parse_file("G:/diss/"
           "uniprot_trembl_masked.fasta", "CoiledCoil")
