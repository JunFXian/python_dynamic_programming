import numpy as np

def lcs_norm_word(answer_text, source_text):
	'''Computes the longest common subsequence of words in two texts; returns a normalized value.
       :param answer_text: The pre-processed text for an answer text
       :param source_text: The pre-processed text for an answer's associated source text
       :return: A normalized LCS value'''
	answer_list = answer_text.split() # column 
	source_list = source_text.split() # row 
	answer_size = len(answer_list)
	source_size = len(source_list)

	lcs_normalized = 0.
	if answer_size > 0 and source_size > 0:
		count_matrix = np.zeros([source_size+1, answer_size+1], dtype=int)
		for source_index in range(source_size): 
			count_matrix[source_index+1][answer_size] = lcs_calc(answer_list, source_list[source_index], source_index, count_matrix)
        lcs_count = count_matrix[source_size][answer_size]
        lcs_normalized = lcs_count/answer_size
	return lcs_normalized

def lcs_calc(answers, source, source_index, count_matrix):
    answer_size = len(answers)

    count = 0
	if answer_size == 1:
		if answers[0] == source:
			count = count_matrix[source_index][answer_size-1] + 1
		else:
			count = max(count_matrix[source_index+1][answer_size-1], count_matrix[source_index][answer_size]) 
	else:
        count_matrix[source_index+1][answer_size-1] = lcs_calc(answers[:-1].copy(), source, source_index, count_matrix)
		if answers[-1] == source:
			count = count_matrix[source_index][answer_size-1] + 1
		else:
			count = max(count_matrix[source_index+1][answer_size-1], count_matrix[source_index][answer_size]) 
	return count




answer = 'This is a test.'
source = 'This is a source of the answer.'

print(lcs_norm_word(answer, source))