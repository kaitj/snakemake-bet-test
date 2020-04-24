import numpy as np
import matplotlib.pyplot as plt 
import nibabel as nib

in_nii = snakemake.input['t1w_brain']
slices = int(snakemake.params['slices'])
out_png = snakemake.output[0]

def compile_slices(img_data, slices):
    """ Function to compite spacing"""
    slice_list = []
    for axis in range(3):
        idxes = np.linspace(0, img_data.shape[axis]-1, slices+2).astype(int)
        
        for i, idx in enumerate(idxes):
            if i == 0 or i == len(idxes)-1:
                continue
            if axis == 0:
                slice_list.append(img_data[idx, :, :])
            elif axis == 1:
                slice_list.append(img_data[:, idx, :])
            elif axis == 2:
                slice_list.append(img_data[:, :, idx])
            else:
                # Need to implement handling of 4D data
                continue 
    
    # Reshape list to corresponding axes
    slice_list = np.reshape(slice_list, (3, slices))
    
    return slice_list

## Display slices
def show_slices(slice_list):
    """ Function to display slices, organized by orientation """
    f, ax = plt.subplots(3, slice_list.shape[1])

    for i in range(3):
        for j, slice in enumerate(slice_list[i]):
            ax[i][j].imshow(slice.T, cmap="gray", origin="lower")


# plot
brain_img = nib.load(in_nii)
brain_img_data = brain_img.get_fdata()

slice_list = compile_slices(brain_img_data, slices=slices)

show_slices(slice_list)

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.savefig(out_png, dpi=200)