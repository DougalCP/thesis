#Directory "test_dataset" contains the fastq files of interest.

1) The"fastqc_files.py" python script performs quality control on the FASTQ files in directory 
"test_data" using the FastQC program putting the output in another subdirectory called "fastqc_out".


2. The "trimm_script.py" python script is performing quality control using the trimmomatic software to remove those reads who fail a set of thresholds related to (i) nucleotide quality (ii) the presence of primers, adapters (iii) sequence length.
