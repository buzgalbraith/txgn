import os.path as osp

import torch
from torch_geometric.data import HeteroData
DATA_PATH = "data/"
def base_graph(path, triplets_to_consider  = ["cancer_to_drug", "cancer_to_gene", "cancer_to_treatment", "gene_to_up_regulate_to_cancer"]):
    graph  = HeteroData()
    with open(path + "entities_metadata.txt") as f:
        for line in f:
            line = line.strip().split("\t")
            graph[line[0]].x = torch.tensor([int(line[1]) , 1])
    f.close()
    with open(path + "relations_metadata.txt") as f:
        i = 1
        for line in f:
            line = line.strip().split("\t")
            count = int(line[1])
            line = [x.strip("(' ')") for x in line[0].split(",")]
            graph[line[0].strip("('')"), line[1], line[2].strip("('')")].edge_index = [2, count]
    f.close()
    return graph
if __name__ == "__main__":
    base_graph(DATA_PATH)