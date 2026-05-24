# Compositional and interpretable representation of histology using AI foundation models and sparse autoencoders

Table of Contents
------------------
* General Information
  * Associated Publication
  * Recommended Citation
  * Useful Links
* Demo for the FM-SAE workflow
  * Installation
  * Demo notebook 
* Additional notes / comments

------------------ 
General Information
------------------
### Compositional and interpretable representation of histology using AI foundation models and sparse autoencoders <Publication or Dataset Title>   
**Authors:** Ziyuan Zhao*, Zoltan Maliga*, Emmanuel C. Ogbonna, Soheil R. Talemi, Shannon Coy, Andréanne Gagné, Kapongo Lumamba, Isaac H. Solomon, Angela Shih, Sandro Santagata, Adrie J.C. Steyn, Threnesan Naidoo†, Peter K. Sorger† 
  
*Co-first Authors: Z.Z., Z.M.

†Co-Senior Authors: T.N., P.K.S.  
​  
**Please cite this data as the following:**      
Zhao, Z. et al. (2026). Compositional and interpretable representation of histology using AI foundation models and sparse autoencoders. {journal/biorxv}    

**Relevant links:** <remove links that are not relevant>  
> * Publication DOI: [doi.org/MY-PAPER-DOI](https://doi.org/MY-PAPER-DOI-URL) 
> * Associated GitHub Repository: [MY-REPO](https://github.com/labsyspharm/2025-Vallius-Shi-Novikov-melanoma-PCAII)  
> * To view an archived record of this repository: [My-ZENODO-DOI](https://zenodo.org/doi/MY-ZENODO-DOI-URL) 
> * To view the image data online, visit: [My-ATLAS-PAGE](https://tissue-atlas.org/MY-ATLAS-PAGE-URL)
​
**Licenses/restrictions placed on the data:** CC-BY [creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)


------------------ 
Applying the FM-SAE workflow
------------------

### Installation
Make a minimal working environment for running the demo notebook with just `spatialdata` installed:
```bash
conda create -n fmsae python=3.10 -y
conda activate fmsae
pip install "spatialdata[extra]"
```

The notebook shows how to apply a pre-trained SAE model to patch-level FM embeddings from UNI and then make multi-feature maps for whole-slide image outside of the training dataset.

------------------ 
Additional notes / comments
------------------