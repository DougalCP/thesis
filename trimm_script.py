import os
# set up directory variables
seq_dir = 'test_dataset'
trimmed_dir = 'trimmed_out'
# create output directory
isExist= os.path.exists(trimmed_dir)
if not isExist:
	os.mkdir(trimmed_dir)
print('created subdir: ' + trimmed_dir)

# get list of FASTQ files
file_list = os.listdir(seq_dir)
print('# got list of files in: ' + seq_dir)
# create the command string for each sequence
# & implement it
for seq in file_list:
	output_name = " trimmed_out/out_trim_"+seq
	command = 'trimmomatic SE ' + seq_dir + '/' + seq + output_name + " ILLUMINACLIP:TruSeq3-SE:-2:30:10"
	print(command)
	os.system(command)
print('Done')
