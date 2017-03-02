# Submission guide for the Liver Tumor Segmentation LITS Challenge
This guide helps you successfully submit to the LITS Challenge www.lits-challenge.com hosted on CodaLab.
## Table of Content
1. Getting the test data
2. Preparing your submissio
n
3. Upload your submission
4. Check your results

## 1. Getting the test data
The test data will be available from March 4th 2017 on Codalab plattform. You will find the link to download the test data after login [here](https://competitions.codalab.org/competitions/15595#participate). The test data was drawn randomly from the overall contributed data pool. The test data was evaluated independently from three expierenced radiologists.
## 2. Preparing your submission
In order to process your submission automatically, the evaluation program expects your submission to have a certain form:
1. Data format
Your submission files should be in Nifti .nii data format. There exist tools for Python, Matlab and C++ to produce valid .nii files
2. Segmentation Value
Since we evaluate the lesion/tumor class 2 only, our program expects the submitted segmentation to have 0 for background/non-lesion and 2 for lesion/tumor. We will not consider liver class 1, since this is not part of this challenge.
3. Numbers of Pixel and Voxel Spacing
The submitted segmentation needs to have the same dimensions and the same voxel-spacing as the medical volume. A volume mismatch will lead to a non valid submission.
4. Naming conventation
The automatic evaluation script expects the submitted segmentations to follow the following naming convention:
`
test-segmentation-X.nii
'''
Where X is the number of the test-volume. For example for the test volume test-volume-7.nii the corresponding correct naming for the test segmentation is test-segmentation-7.nii

