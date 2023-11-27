DATA_PATH = "data/"
SAVE_PATH = "data/meta_data.txt"
triplets_map = {"cancer_to_drug": {"head": 'cancer_type', "relation":'drug_used', 'tail':'drug'}, "cancer_to_gene": {'head':'cancer_type', 'relation':'mutation_type', 'tail':"gene_mutated"}, "cancer_to_treatment":{'head':'cancer_type', 'relation':'treated_with', 'tail':'treatment'}, "gene_to_up_regulate_to_cancer": {'head':'gene', 'relation':'up_down_regulates', 'tail':'cancer_type'}}
## we want to write a function that counts the number of appearances of each entity type that is cancer_type etc instead of like specific entity value or triplet
def get_metadata(path, triplets_map):
    entities_metadata = {}
    relations_metadata = {}
    for triplet in triplets_map.keys():
        file_types = ["/train.txt", "/valid.txt", "/test.txt"]
        for file_type in file_types:
            with open(DATA_PATH + triplet+file_type) as f:
                for line in f:
                    line = line.strip().split("\t")
                    try:
                        entities_metadata[triplets_map[triplet]["head"]] += 1
                    except:
                        entities_metadata[triplets_map[triplet]["head"]] = 1
                    try:
                        entities_metadata[triplets_map[triplet]["tail"]] += 1
                    except:
                        entities_metadata[triplets_map[triplet]["tail"]] = 1
                    working_tuple = (line[0], line[1], line[2])
                    try:
                        relations_metadata[working_tuple] += 1
                    except:
                        relations_metadata[working_tuple] = 1
            f.close()
    with open(DATA_PATH+"relations_metadata.txt", "w") as f:
        for key in relations_metadata.keys():
            f.write(str(key) + "\t" + str(relations_metadata[key]) + "\n")
        f.close()
    with open(DATA_PATH+"entities_metadata.txt", "w") as f:
        for key in entities_metadata.keys():
            f.write(str(key) + "\t" + str(entities_metadata[key]) + "\n")
        f.close()
if __name__ == "__main__":
    get_metadata(DATA_PATH, triplets_map)
    # a = get_metadata(DATA_PATH)
    # print(a)