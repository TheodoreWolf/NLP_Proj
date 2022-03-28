from genericpath import exists
import os
import glob
from tqdm import tqdm

two_gram_files = sorted([f for f in glob.glob('./2_pos_n/*.txt')])
three_gram_files = sorted([f for f in glob.glob('./3_pos_n/*.txt')])
four_gram_files = sorted([f for f in glob.glob('./4_pos_n/*.txt')])

def collect_mwes(n_gram, infile, threshold):
    mwes = []
    with open(infile, encoding='utf-8', errors='ignore') as f:
        for line in f:
            if int(line.split('\t')[0]) > threshold:
                expression = ' '.join(line.split('\t')[1:1 + n_gram])
                if expression not in mwes:
                    mwes.append(expression)
    return mwes

def write_to_file(lst, outfile):
    if os.path.exists(outfile):
        pass

    else:
        with open(outfile, 'w') as f:
            for letter in lst:
                for mwe in letter:
                    f.write(mwe)
                    f.write('\n')

def generate_mwe_files(two_gram_threshold, three_gram_threshold, four_gram_threshold):

    print(f'Processing 2 gram MWEs with frequency threshold {two_gram_threshold}')
    two_gram_mwes = [collect_mwes(2, x, two_gram_threshold) for x in tqdm(two_gram_files)]
    write_to_file(two_gram_mwes, f'2_gram_mwe_{two_gram_threshold}.txt')

    print(f'Processing 3 gram MWEs with frequency threshold {three_gram_threshold}')
    three_gram_mwes = [collect_mwes(3, x, three_gram_threshold) for x in tqdm(three_gram_files)]
    write_to_file(three_gram_mwes, f'3_gram_mwe_{three_gram_threshold}.txt')


    print(f'Processing 4 gram MWEs with frequency threshold {four_gram_threshold}')
    four_gram_mwes = [collect_mwes(4, x, four_gram_threshold) for x in tqdm(four_gram_files)]
    write_to_file(four_gram_mwes, f'4_gram_mwe_{four_gram_threshold}.txt')

if __name__ == '__main__':
    
    two_gram_threshold = 200
    three_gram_threshold = 50
    four_gram_threshold = 20

    generate_mwe_files(two_gram_threshold, three_gram_threshold, four_gram_threshold)