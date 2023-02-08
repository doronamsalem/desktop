from os import listdir, path

def find_word(word, file_path):
    """:param file_path: file path
    :param word: specific word to search in file
    :return: print path and lines where word appeared in
    """
    line_num = 0
    exist = False
    appearance_lines = []
    try:
    	with open(file_path, "r") as file:
        	# iterate on each line in file
        	for line in file:
        	    line_num += 1
        	    if word in line:
        	        exist = True
        	        appearance_lines.append(line_num)
    except:
    		print( f"had problem searching in {file_path}" )
	# print path and lines where word appeared in
    if exist:
    	print(f"{file_path}: '{word}' appeared in lines: {appearance_lines}")


def iterate_FS(directory="/", word="Word"):
    """
    :param start: path to start files iteration, default: root
    :param word: specific word to search in file system
    :return: call find_word() for each file
    """
    # run over each file in directory
    for filename in listdir(directory):
    	print(listdir(directory))
        file_path = path.join(directory, filename)
    	try:
        	if "." in filename:   # hidden files
		        continue
        	# search for the word if file was found
        	elif path.isfile(file_path):
            		find_word(word, file_path)
        	# iterate over sub-directory
        	elif path.isdir(file_path):
            		iterate_FS(file_path, word)
	except:
		print(f"had problem with {path}")
		continue

iterate_FS("/home/parallels/Desktop", "sdfsdf")
