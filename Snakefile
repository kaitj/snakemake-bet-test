import os.path as op
from snakemake.utils import format
from bids import BIDSLayout

configfile: "config.yaml"

subj_prefix = 'sub-001'
subject = "001" 

in_dir = config["in_dir"]
out_dir = op.join(config["in_dir"], "derivatives/snake_out")

layout = BIDSLayout(in_dir, validate=False)
entities = config["entities"]

slices = config["slices"]

rule all:
    input:
        vis = expand(op.join('plots', f'{subj_prefix}_brain_vis.png'),caption="../report/brain_vis.rst",category='Brain Visualization')


include: 'rules/bet.smk'