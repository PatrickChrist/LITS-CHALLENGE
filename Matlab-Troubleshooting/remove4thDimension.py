# Script to fix corrupted Matlab nii Files. Fixes Shape mismatch due to Matlab issues.
# Expects volumes and segmentations in the folder with the correct naming convention.

import nibabel as nb
import numpy as np


if __name__ == "__main__":
    # Iterate over all volumes
    for case in range(70):
        print 'Starting with case %s' % case
        pred = nb.load('test-segmentation-' + str(case) + '.nii')
        volume = nb.load('test-volume-' + str(case) + '.nii')

        # Load the data
        pred_data = pred.get_data()

        # Squeeze Singeton Dimension Dimensions
        pred_data = np.squeeze(pred_data)

        if volume.shape != pred_data.shape:
            print 'Shape of volume %s and predictions %s do not match for case %s' % (volume.get_data().shape, pred_data.shape,case)
        # Check whether label is 2
        if np.max(pred_data)!=2:
            pred_data = pred_data * 2

        # Check if shapes match

        # Construct valid Nii Image
        img_to_save = nb.Nifti1Image(pred_data.astype(volume.get_data_dtype()), volume.get_affine(), header=volume.header)
        save_name = 'test-segmentation-' + str(case) + '_fixed.nii'
        # Saving
        print 'Saving %s' % save_name
        nb.save(img_to_save,  save_name)
