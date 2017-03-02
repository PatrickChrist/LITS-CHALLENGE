# Submission guide for the Liver Tumor Segmentation LITS Challenge
This guide helps you successfully submit to the LITS Challenge www.lits-challenge.com hosted on CodaLab.
## Table of Content
1. Getting the test data
2. Preparing your submission
3. Upload your submission
4. Check your results

## 1. Getting the test data
The test data will be available from March 4th 2017 on Codalab plattform. You will find the link to download the test data after login [here](https://competitions.codalab.org/competitions/15595#participate). The test data was drawn randomly from the overall contributed data pool. The test data was evaluated independently from three expierenced radiologists.
## 2. Preparing your submission
In order to process your submission automatically, the evaluation program expects your submission to have a certain form:
### 2.1. Data format
Your submission files should be in Nifti .nii data format. There exist tools for Python, Matlab and C++ to produce valid .nii files
### 2.2. Segmentation Value
Since we evaluate the lesion/tumor class 2 only, our program expects the submitted segmentation to have 0 for background/non-lesion and 2 for lesion/tumor. We will not consider liver class 1, since this is not part of this challenge.
### 2.3. Numbers of Pixel and Voxel Spacing
The submitted segmentation needs to have the same dimensions and the same voxel-spacing as the medical volume. A volume mismatch will lead to a non valid submission.
### 2.4. Naming conventation
The automatic evaluation script expects the submitted segmentations to follow the following naming convention:
```
test-segmentation-X.nii
```
Where X is the number of the test-volume. For example for the test volume test-volume-7.nii the corresponding correct naming for the test segmentation is test-segmentation-7.nii
### 2.5. Zip Archive of all your files
Codalab only accepts zip archives. Please zip all your test-segmentation-X.nii files into a single zip archive. The zip archives should not contain any other files or subfolder structures.
## 3. Upload your submission
After applying steps 2.1-2.5 you are able to upload your submission to the Codalab submission system. Go to https://competitions.codalab.org/competitions/15595#participate-submit_results and upload your zip file.
## 4. Check your results
After uploading your zip file, the plattform is unzipping your data and running the evaluation program. This can take up to serval hours.
You can check your current status and error reports here.![Image of Codalab Submission](https://github.com/PatrickChrist/LITS-CHALLENGE/blob/PatrickChrist-guide/codalab.png)
## Important note from the evaluation page as a reminder
However, to foster performance we provide liver masks during training time. During test time only the medical volumes not no liver mask will be available.
That means there will be no liver mask for the test data.
