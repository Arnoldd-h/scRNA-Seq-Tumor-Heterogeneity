#!/usr/bin/env python3
"""
==============================================================================
00_project_setup.py - Melanoma Single-Cell Landscape Project Setup
==============================================================================

Script to create the directory structure for the scRNA-seq melanoma analysis
project aimed at identifying exhausted T cell populations associated with
immunotherapy resistance.

Author: Bioinformatics Pipeline
Project: Melanoma-Single-Cell-Landscape
Dataset: Jerby-Arnon et al. (Cell, 2018) - GSE115978

Project Structure:
├── data/
│   ├── raw/          # Original count files (.mtx, .h5ad)
│   └── processed/    # Processed and filtered AnnData objects
├── notebooks/        # Step-by-step analysis (01_QC, 02_Clustering...)
├── results/
│   ├── figures/      # High-quality plots (UMAP, DotPlots)
│   └── tables/       # Gene markers (DEGs)
├── src/              # Helper functions
└── README.md         # Project documentation
"""

import os
from pathlib import Path


def create_project_structure(base_path: str = ".") -> None:
    """
    Create the directory structure for the scRNA-seq project.
    
    Parameters
    ----------
    base_path : str
        Base path where to create the project structure.
        Defaults to the current directory.
    
    Returns
    -------
    None
    """
    
    # Define directory structure
    directories = [
        "data/raw",           # Raw data: count matrices, original h5ad files
        "data/processed",     # Processed data: post-QC AnnData objects
        "notebooks",          # Jupyter notebooks for analysis
        "results/figures",    # High-quality figures for publication
        "results/tables",     # Result tables (DEGs, markers)
        "src",                # Python modules with helper functions
    ]
    
    base = Path(base_path)
    
    print("=" * 60)
    print("🧬 Melanoma Single-Cell Landscape - Project Setup")
    print("=" * 60)
    print(f"\n📁 Creating structure at: {base.resolve()}\n")
    
    # Create each directory
    for directory in directories:
        dir_path = base / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        
        # Create .gitkeep file to preserve empty directories in git
        gitkeep_path = dir_path / ".gitkeep"
        if not gitkeep_path.exists():
            gitkeep_path.touch()
        
        print(f"  ✅ {directory}/")
    
    # Create __init__.py in src to make it a Python module
    init_file = base / "src" / "__init__.py"
    if not init_file.exists():
        init_file.write_text(
            '"""\n'
            'src - Helper functions for scRNA-seq analysis\n'
            '\n'
            'This module contains utility functions for:\n'
            '- Quality Control (QC)\n'
            '- Normalization and preprocessing\n'
            '- Clustering and cell annotation\n'
            '- Data visualization\n'
            '- Differential expression analysis\n'
            '"""\n'
        )
    
    # Create README.md with project description
    readme_path = base / "README.md"
    readme_content = """# 🧬 Melanoma Single-Cell Landscape

## Tumor Heterogeneity Analysis via scRNA-seq

### 📋 Objective
Analyze scRNA-seq data from melanoma patients to identify **exhausted T cell** 
populations associated with **immunotherapy resistance**.

### 📊 Dataset
- **Primary Study**: Jerby-Arnon et al. (Cell, 2018)
- **GEO Accession**: [GSE115978](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE115978)
- **Alternative**: Tirosh et al. 2016 (GSE72056)

### 🛠️ Technology Stack
- **Python 3.8+**
- **Scanpy** - Single-cell analysis
- **AnnData** - Data structure
- **Matplotlib/Seaborn** - Visualization
- **Pandas** - Data manipulation

### 📂 Project Structure
```
├── data/
│   ├── raw/          # Original count files (.mtx, .h5ad)
│   └── processed/    # Processed and filtered AnnData objects
├── notebooks/        # Step-by-step analysis
│   ├── 01_QC.ipynb
│   ├── 02_Clustering.ipynb
│   └── ...
├── results/
│   ├── figures/      # High-quality plots (UMAP, DotPlots)
│   └── tables/       # Gene markers (DEGs)
├── src/              # Helper functions
└── README.md
```

### 🔬 Analysis Pipeline
1. **Quality Control (QC)**
   - Filtering by detected genes
   - Filtering by mitochondrial content
   - Doublet removal

2. **Preprocessing**
   - Normalization
   - Highly variable gene selection
   - Scaling

3. **Dimensionality Reduction**
   - PCA
   - UMAP

4. **Clustering**
   - Leiden clustering
   - Cell type annotation

5. **T Cell Analysis**
   - Identification of exhausted populations
   - Markers: PD-1, TIM-3, LAG-3, TIGIT

### 📈 QC Metrics
| Metric | Description | Typical Threshold |
|--------|-------------|-------------------|
| `n_genes` | Genes detected per cell | 200-5000 |
| `n_counts` | Total UMIs per cell | Variable |
| `pct_counts_mt` | % mitochondrial counts | <20% |

### 📚 References
1. Jerby-Arnon L, et al. (2018). A Cancer Cell Program Promotes T Cell Exclusion 
   and Resistance to Checkpoint Blockade. *Cell*.
2. Tirosh I, et al. (2016). Dissecting the multicellular ecosystem of metastatic 
   melanoma by single-cell RNA-seq. *Science*.

---
*Project developed as part of Bioinformatics Portfolio*
"""
    
    readme_path.write_text(readme_content)
    print(f"\n  ✅ README.md")
    
    print("\n" + "=" * 60)
    print("✨ Project structure created successfully!")
    print("=" * 60)
    print("\n📌 Next steps:")
    print("   1. Download data from GEO (GSE115978) to data/raw/")
    print("   2. Run QC notebook: notebooks/01_QC.ipynb")
    print("   3. Review results in results/figures/")


if __name__ == "__main__":
    # Run from project directory
    create_project_structure(".")
