# TreeGraph

Treegraph is a Python library for extracting structural parameters from point clouds of individual trees.

## Installation

1.  Create a conda environment and install dependencies:
    `$ conda env create -f environment.yaml`

2.  Download the source codes from Github:
    `$ git clone https://github.com/wanxinyang/treegraph.git --branch v1.8`

3.  Copy the source codes to the conda env site-packages directory:
    `$ cp -r treegraph/treegraph/ ~/.conda/envs/treegraph/lib/python3.7/site-packages/`

## Usage

### File structure

It is assumed the following folders have been created:

```
treegraph_tutorial/
├── clouds/
│   └── <individual tree point clouds in .ply format>
├── inputs/
│   └── <input parameters files for individual trees created by generate_inputs.py>
└── results/
    └── <outputs from treegraph generated by tree2qsm.py>

```

### Generate input files

You can keep the default parameter settings. If you want to adjust the settings, then open and edit `treegraph/scripts/generate_inputs.py`.

```
conda activate treegraph
cd treegraph_tutorial/inputs/
python /PATH/TO/treegraph/scripts/generate_inputs.py -d '/PATH/TO/clouds/*.ply' -o '/PATH/TO/results/'

```

### Run Treegraph

#### Option 1: Run on a single tree

`python treegraph/script/tree2qsm.py -i 'inputs/XXX.yml'`

#### Option 2: Run all the trees one after another:

`python treegraph/script/batch_tree2qsm.py -i 'inputs/*.yml'`

#### Option 3: Batch process on HPC

Example job_script.sh for SLURM system

    #!/bin/bash 
    # scheduling queue
    #SBATCH --partition=high-mem
    # max runtime limit
    #SBATCH --time=12:00:00
    # job name
    #SBATCH --job-name=treegraph
    # job output and error output
    #SBATCH --output %j.out 
    #SBATCH --error %j.err
    # required memory, unit MB
    #SBATCH --mem=102400
    # working dir 
    #SBATCH -D /PATH/TO/OUTPUTS/
    # Number of CPU cores
    #SBTACH -n 1

    # executable 
    conda activate treegraph
    echo "python ~/miniconda3/envs/treegraph/lib/python3.7/treegraph/scripts/tree2qsm.py -i '$tree'"
    python ~/miniconda3/envs/treegraph/lib/python3.7/treegraph/scripts/tree2qsm.py -i "${tree}"

## Authors

*   Wanxin Yang
*   Phil Wilkes
*   Matheus Boni Vicari
*   Mathias Disney

