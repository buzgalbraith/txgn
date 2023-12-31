- we are reimplementing this [example](https://github.com/pyg-team/pytorch_geometric/blob/master/examples/tgn.py) 
- the example data they use can be viewed [here](https://snap.stanford.edu/jodie/)
- [paper link](https://cs.stanford.edu/people/jure/pubs/jodie-kdd19.pdf#page=9&zoom=100,76,502)
- [package documentation](https://pytorch-geometric.readthedocs.io/en/latest/modules/loader.html)
    - one of the things we want to think about is what kind of loader to use. 
    - I think we may want to use [HGTLoader](https://pytorch-geometric.readthedocs.io/en/latest/modules/loader.html#torch_geometric.loader.HGTLoader) or [imbalanced sampler](https://pytorch-geometric.readthedocs.io/en/latest/modules/loader.html#torch_geometric.loader.ImbalancedSampler)
- [heterogeneous graph example](https://pytorch-geometric.readthedocs.io/en/latest/tutorial/heterogeneous.html)