rule bet:
    input:
        t1w_nii = op.join(in_dir, subj_prefix, 'anat', f'{subj_prefix}_acq-MP2RAGE_run-01_T1w.nii.gz')
    output:
        t1w_brain = op.join(out_dir, subj_prefix, 'anat', f'{subj_prefix}_T1w_brain.nii.gz')
    log:
        f'logs/bet/{subj_prefix}.log'
    shell:
        "(bet {input.t1w_nii} {output.t1w_brain} -f 0.2) &> {log}"

rule visualise_brain:
    input:
        t1w_brain = op.join(out_dir, subj_prefix, 'anat', f'{subj_prefix}_T1w_brain.nii.gz'),
    output:
        report(op.join('plots', f'{subj_prefix}_brain_vis.png'),caption="../report/brain_vis.rst",category='Brain Visualization')
    params:
        slices = f'{slices}'
    conda: "../envs/vis.yml"
    script: "../scripts/visualize_brain.py"