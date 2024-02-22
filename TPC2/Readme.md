wfreq - Calculates the frequency of words in a text

[INSTALL]
	pip install flit
	flit build
	flit install

[SYNOPSIS]
    wfreq [options] input_files:

[OPTIONS]:
    -m 20: Show 20 most common
    -n: Sort alphabetically
    -c: Count occurrences ignoring cases of the same word written in uppercase and lowercase letters
    -r: Sort occurrences by ratio calculated using frequency table
