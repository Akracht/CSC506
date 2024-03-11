#Import Statements
import time
import matplotlib.pyplot as plt

#Python Naive String Search Algorithm
def NaiveStringSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    count = 0  # Initialize match count

    for i in range(N - M + 1):
        j = 0
        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1

        if j == M:
            count += 1  # Increment count for each match
    return count

# Python KMP Search Algorithm 
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0
    count = 0  # Initialize match count

    computeLPSArray(pat, M, lps)
    i = 0
    while N - i >= M - j:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            count += 1  # Increment count for each match
            j = lps[j - 1]

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count
 
 
# Function to compute KMP LPS array
def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix
 
    lps[0] = 0  # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

#Python Rabin-Karp Search Algorithm
def RabinKarpSearch(pat, txt, q=101):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    d = 256
    count = 0  # Initialize match count

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
            if j == M - 1:  # Adjust condition for 0-indexing
                count += 1  # Increment count for each match

        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            if t < 0:
                t += q
    return count

# Function wrappers for search algorithms
def RabinKarpWrapper(pat, txt):
    return RabinKarpSearch(pat, txt, q=256)

#Prints results to table w/ algorithms represented by rows and avg. execution time per term in columns for each method. 
def print_results_table(results, match_counts):
    terms = list(results.keys())
    algorithms = ['NaiveStringSearch', 'KMPSearch', 'RabinKarpSearch']  # Adjusted to match the correct names
    
    # Print table header
    print("Search Function", end='')
    for term in terms:
        print(f" | {term} time (s) | {term} matches", end='')
    print()  # Newline after header
    print("-" * 70)  # Adjust length of the separator based on your output width
    
    # Print each row of the table
    for i, algorithm in enumerate(algorithms):
        print(f"{algorithm}", end='')
        for term in terms:
            time = results[term][i]
            matches = match_counts[term][i]
            print(f" | {time:.5f} | {matches}", end='')
        print()  # Newline after each algorithm's row
        
# Function to read text from file
def read_text(filename):
    with open(filename, 'r') as file:
        return file.read()

#time_search function 
def time_search(search_function, pat, txt, iterations=200, **kwargs):
    total_time = 0
    total_matches = 0
    for _ in range(iterations):
        start_time = time.time()
        matches = search_function(pat, txt, **kwargs) if 'q' in kwargs else search_function(pat, txt)
        total_time += time.time() - start_time
        total_matches += matches
    avg_time = total_time / iterations
    avg_matches = total_matches / iterations
    return avg_time, avg_matches

# Benchmark function updated with appropriate q value for RabinKarpSearch
def benchmark_search_functions(text_file):
    txt = read_text(text_file)
    search_terms = ['he', 'his', 'Colonel', 'I asked', 'said my patient']
    algorithms = [NaiveStringSearch, KMPSearch, RabinKarpWrapper]  # Correct use of RabinKarpWrapper
    results = {term: [] for term in search_terms}
    match_counts = {term: [] for term in search_terms}
    
    for term in search_terms:
        for algorithm in algorithms:
            avg_time, avg_matches = time_search(algorithm, term, txt)
            results[term].append(avg_time)
            match_counts[term].append(avg_matches)
            algorithm_name = algorithm.__name__.replace('Wrapper', 'Search')
            print(f"Average time to find '{term}' using {algorithm_name}: {avg_time:.5f} seconds, Matches: {avg_matches}")

    # Plotting the results
    for term in results:
        times = [results[term][i] for i in range(len(algorithms))]
        plt.plot(['NaiveStringSearch', 'KMPSearch', 'RabinKarpSearch'], times, label=term)

    plt.xlabel('Search Algorithm')
    plt.ylabel('Average Execution Time (s)')
    plt.title('Search Algorithm Performance')
    plt.legend()
    plt.show()

    # After plotting, print the results table
    print_results_table(results, match_counts)

    
#Main()
if __name__ == "__main__":
    benchmark_search_functions('engr.txt')
