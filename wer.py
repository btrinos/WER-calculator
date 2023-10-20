def wer(reference, hypothesis):
    """
    Calculate the Word Error Rate (WER) between reference and hypothesis.
    
    :param reference: The ground truth text.
    :param hypothesis: The predicted text.
    :return: Word error rate as a float.
    """

    # References: 
    # https://www.assemblyai.com/blog/word-error-rate/
    # https://en.wikipedia.org/wiki/Word_error_rate
    # https://www.mathworks.com/matlabcentral/fileexchange/55825-word-error-rate
            
    # Split both reference and hypothesis by spaces to get word lists
    r = reference.split()
    h = hypothesis.split()
    
    # Initialize the matrix for dynamic programming
    # The matrix will store the edit distances between prefixes of r and h
    d = [[0] * (len(h)+1) for _ in range(len(r)+1)]
    
    # Initialize the first column of the matrix. This represents the cost of deleting words from r
    for i in range(len(r)+1):
        d[i][0] = i
        
    # Initialize the first row of the matrix. This represents the cost of inserting words to r
    for j in range(len(h)+1):
        d[0][j] = j

    # Iterate over the matrix to compute the edit distances
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            # If the words are the same, the cost is 0
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                # Calculate costs of substitution, insertion and deletion
                substitution = d[i-1][j-1] + 1
                insertion = d[i][j-1] + 1
                deletion = d[i-1][j] + 1
                # Take the minimum of the three costs
                d[i][j] = min(substitution, insertion, deletion)
    
    # The value at the bottom-right corner of the matrix represents
    # the edit distance between r and h. Divide it by the length of r
    # to get the Word Error Rate.
    return d[len(r)][len(h)] / len(r)


def main():
    # Read the reference text from d1.txt
    with open('d1.txt', 'r', encoding='utf-8') as f:
        reference = f.read()

    # Read the hypothesis text from d2.txt
    with open('d2.txt', 'r', encoding='utf-8') as f:
        hypothesis = f.read()

    # Calculate and print the Word Error Rate
    print(f"Word Error Rate (WER): {wer(reference, hypothesis)*100:.2f}%")

# Entry point of the script
if __name__ == '__main__':
    main()
