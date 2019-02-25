import os
import sys
import re

def get_email_body(f_path):
	f = open(f_path, 'r')
	a = f.read()

	regular_exp_1 = r"Message Body :(.*)EDRM Enron Email Data"
	regular_exp_2 = r"[\n\r\t]"
	star_regex = r"\*+"
	regular_exp_to = r"To :(.*) CC"

	pattern = re.compile(regular_exp_1)
	pattern_2 = re.compile(regular_exp_2)
	pattern_3 = re.compile(star_regex)
	pattern_to = re.compile(regular_exp_to)

	a = pattern_2.sub(" ", a)
	result = re.findall(pattern, a)
	message_body = pattern_3.sub("", result[0])
	result_to = re.findall(pattern_to, a)

	f.close()

	return(result_to[0], message_body)

directory = os.path.normpath("data/Enron")
write_train_text_path = "data/train_to.tsv"

roots = next(os.walk(directory))[1]
roots.sort()

for level_1 in roots:
	dir_1 = os.path.join(directory, level_1)
	roots_1 = next(os.walk(dir_1))[1]
	roots_1.sort()
	
	for level_2 in roots_1:
		dir_2 = os.path.join(dir_1, level_2)
		roots_2 = next(os.walk(dir_2))[2]
		roots_2.sort()

		if(len(roots_2) == 0):
			continue
		
		for level_3 in roots_2:
			file_extention = os.path.splitext(level_3)[1]
			if(file_extention == '.txt'):
				cat_file_name = os.path.splitext(level_3)[0] + ".cat"
				txt_file_path = os.path.join(dir_2, level_3)

				if(cat_file_name in roots_2):
					cat_file_path = os.path.join(dir_2, cat_file_name)
					txt_string = get_email_body(txt_file_path)[1]
					to_name = get_email_body(txt_file_path)[0]

					
					with open(cat_file_path, 'r') as read_cat_file, open(write_train_text_path, 'a') as write_train_text_file:
						write_train_text_file.write(to_name.strip() + '\t' + txt_string.strip() + '\t' + read_cat_file.read().strip() + '\n')

