#! /usr/bin/env

import torch_geometric as tg

import Bio.PDB
import biotite
import numpy

db = 'uniprotkb_Q9_2024_08_31.json' # JSON file from uniprot request

#use uniprot db request for dic code:seq
with open(db, 'r') as f:
	db = json.load(f)

for i in a['results']:
	i['primaryAccession']
	i['sequence']
dict_keys = ['entryType', 'primaryAccession', 'uniProtkbId', 'entryAudit', 'annotationScore', 'organism', 'proteinExistence', 'proteinDescription', 'genes', 'comments', 'features', 'keywords', 'references', 'uniProtKBCrossReferences', 'sequence', 'extraAttributes']
	
#for each, blast and MSA beforehandfor speed, and keep how it was done for example
# PyCOM for coevolution matrix of ach entry?


# get structures

gene_list=[] #uniprot id of protein sequences from DB
pdb_list = []
for i in range(len(ltp_list)):
    count_ltp = 0
    req = rq.get("https://rest.uniprot.org/uniprotkb/search?query="+ltp_list[i]+"%20AND%20(organism_id:9606)&size=2")
    try:
        #for i in req.json()['results'][1]['uniProtKBCrossReferences']:
        #    if i['database'] == 'PDB':
        #        count_ltp+=1
        #        pdb_list.append(i['id'])
        #print(ltp + " : " + str(count_ltp))
        #if count_ltp == 0:
            for j in req.json()['results'][0]['uniProtKBCrossReferences']:
                if j['database'] == 'PDB':
                    count_ltp+=1
                    pdb_list.append((j['id'],gene_list[i]))
            print(ltp_list[i] + " : " + str(count_ltp))
    except:
        #print(req.json()['results'])
        pass
#here you get pdb IDs, is it enough to use biotite/biopython or does one need the whole structure and hen parse it? fastest implementation or run?
print(len(pdb_list))
countt=0
for i in range(len(pdb_list)):
    try:
        if not os.path.exists(pdb_list[i][1]):
            os.mkdir(pdb_list[i][1])
        os.chdir(pdb_list[i][1])
        url = "http://files.rcsb.org/download/"+pdb_list[i][0]+".pdb1.gz"
        print(url)
        wget.download(url)
        os.chdir("..")

    except:
        countt+=1
        print(pdb_list[i])
print(countt)

