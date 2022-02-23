import json
import pandas as pd
import csv

def load_dataset_as_json(path, train_filename, test_filename, out_path, format='txt'):
    if format == 'txt':
        train_df = pd.read_table(path + train_filename, quoting=csv.QUOTE_NONE, delimiter='\t', encoding='utf-8')
        test_df = pd.read_table(path + test_filename, quoting=csv.QUOTE_NONE, delimiter='\t', encoding='utf-8')
    
    train_json = open(out_path + 'train.json', 'w')
    for i in range(len(train_df)):
        d = {'sentence': train_df['sentence'][i], 'complexity': float(train_df['complexity'][i])}
        json.dump(d, train_json)
        train_json.write('\n')


    test_json = open(out_path + 'test.json', 'w')
    for i in range(len(test_df)):
        d = {'sentence': test_df['sentence'][i], 'complexity': float(test_df['complexity'][i])}
        json.dump(d, test_json)
        test_json.write('\n')
        
    print(f'Loaded {len(train_df)} training entries and {len(test_df)} test entreies.')


if __name__ == '__main__':
    load_dataset_as_json('./datasets/', 'lcp_single_train.tsv.txt', 'lcp_single_test_labels.tsv.txt', './temp/')