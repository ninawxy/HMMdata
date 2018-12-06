# HMMdata
Script takes downloaded .tsv files from phmmer search result and implement the sequence of interest to the similarity matrix.

## Introduction to phmmer search 

The phmmer search takes a protein sequence as a query and compare it with the selected database to return all homologous protein 
sequences using Hidden Markov Model (HMM). The result can be downloaded in various forms and the ones being process in this
project is the .tsv file with mainly focuses on the target name and E-value. 

Website to do phmmer search: <https://www.ebi.ac.uk/Tools/hmmer/search/phmmer>


*The .tsv file needed to be converted to .txt file to be processed using the script.*



## Processing E-values

The E-values in the file represents the similarity between the query sequence and the target sequences in the result. The lower
the E-value the higher the similarity between the sequences. The E-values range from 0 to 1 with most of them being very small 
numbers. Therefore, the original E-values are processed in a way to be taken the -log10 of the original number and give a positive
number that are used to amplify the differences between the original E-values. 

However, some of the sequences pairs, they have E-values 
that equal to 0, so it can't undergo the math. An incredibly large number (in this case, 1000,000) is assigned to these sequence pairs
to make sure the matrix can be process by clustering softwares.


## Building the Matrix

The columns and rows in the matrix are the target sequences. The values in the matrix are the processed E-values between the sequences. 
The higher the values, the more similarity between the sequences. The script export the matrix to your local device and can be used
to do clustering analysis on software like Morpheus.






## 
*Sample input files downloaded from the phmmer website, sample output files after E-value calculation, and sample matrix file can be found in this project.*

*All sequence files being analyzed can be found in the branch called Dataset*
