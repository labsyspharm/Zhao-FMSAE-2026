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
**Authors:** Ziyuan Zhao*, Zoltan Maliga*, Emmanuel C. Ogbonna, Soheil R. Talemi, Shannon Coy, Andréanne Gagné, Kapongo Lumamba, Isaac H. Solomon, Sandro Santagata, Adrie J.C. Steyn, Threnesan Naidoo†, Peter K. Sorger† 
  
*Co-first Authors: Z.Z., Z.M.

†Co-Senior Authors: T.N., P.K.S.  
​  
**Please cite this data as the following:**      
Zhao, Z. et al. (2026). Compositional and interpretable representation of histology using AI foundation models and sparse autoencoders. {journal/biorxiv}    

**Relevant links:** <remove links that are not relevant>  
> * Publication DOI: https://doi.org/10.64898/2026.XX.XX.725182
> * Associated GitHub Repository: https://github.com/labsyspharm/Zhao-FMSAE-2026
> * To view an archived record of this repository: TBD
​
**Licenses/restrictions placed on the data:** CC-BY [creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)


------------------ 
Applying the FM-SAE workflow
------------------

### Installation
Make a minimal working environment for running the demo notebook:
```bash
conda create -n Zhao-FMSAE-2026 python=3.10 -y
conda activate Zhao-FMSAE-2026
pip install .
```

The notebook shows how to apply a pre-trained SAE model to patch-level FM embeddings from [UNI](https://github.com/mahmoodlab/UNI) and then make multi-feature maps for whole-slide image outside of the training dataset. You can use the provided SAE model on other H&E datasets of your choice as long as you use [UNI](https://github.com/mahmoodlab/UNI) to embed patches with size of ~120 x 120 µm.

------------------ 
Additional notes / comments
------------------