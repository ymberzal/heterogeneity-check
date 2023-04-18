import numpy as np
import pandas as pd
import argparse
from scipy import stats

def gc_correction(pvals):
    lambda_gc = np.median(pvals) / 0.455
    return pvals / lambda_gc

def heterogeneity_test(pvals):
    Q = np.sum([(1 / p) for p in pvals])
    df = len(pvals) - 1
    p_value = 1 - stats.chi2.cdf(Q, df)
    return p_value

def main(file_path, output_path):
    df = pd.read_csv(file_path, sep='\t')
    
    # convert p-value column to numeric
    df['pval'] = pd.to_numeric(df['pval'], errors='coerce')
    
    # drop rows with missing values
    df.dropna(inplace=True)
    
    # split data by study number
    study_results = []
    overall_result = None
    for study_num, study_data in df.groupby('study_num'):
        study_pvals = study_data['pval'].values
        study_pvals_gc = gc_correction(study_pvals)
        study_pvals_het = heterogeneity_test(study_pvals_gc)
        study_results.append((study_num, len(study_pvals), study_pvals_het))
    
    # perform overall heterogeneity test
    overall_pvals = df['pval'].values
    overall_pvals_gc = gc_correction(overall_pvals)
    overall_pval_het = heterogeneity_test(overall_pvals_gc)
    overall_result = len(overall_pvals), overall_pval_het
    
    # save results to file
    with open(output_path, 'w') as f:
        f.write('Study_Num\tSample_Size\tHeterogeneity_p-value\n')
        for study_result in study_results:
            f.write(f'{study_result[0]}\t{study_result[1]}\t{study_result[2]}\n')
        f.write('\n')
        f.write('Overall\tSample_Size\tHeterogeneity_p-value\n')
        f.write(f'Overall\t{overall_result[0]}\t{overall_result[1]}\n')
    
    return study_results, overall_result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform heterogeneity test on p-values from multiple studies.')
    parser.add_argument('file_path', type=str, help='Path to input file.')
    parser.add_argument('output_path', type=str, help='Path to output file.')
    args = parser.parse_args()

    study_results, overall_result = main(args.file_path, args.output_path)
    print('Done.')

