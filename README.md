# heterogeneity-check
THe script uses the median chi-squared method, which involves calculating the median of the observed chi-squared statistics from a set of independent SNPs with expected p-values above a certain threshold (such as 0.1 or 0.5). The median of the observed chi-squared statistics is then divided by the median of the expected chi-squared statistics, which is equivalent to dividing by the degrees of freedom. The resulting value is the estimated λ.

Once  λ value is estimated for each study, we correct the test statistics by dividing them by the estimated λ value. This should be done before conducting the meta-analysis, as well as after the meta-analysis, to ensure that any potential bias due to population stratification is accounted for in each individual study and in the combined analysis.

In summary, to correct for population stratification before and after meta-analysis, you need to estimate the genomic inflation factor (λ) from a set of unlinked genetic markers, using methods such as the median chi-squared method, and adjust the test statistics by dividing them by the estimated λ value.

Usage: python3 hetero.py inputfile.txt outputfile.txt

The input file contains four columns: study_num	rsid	pval	n (aseparated by tab)
If I have 10 SNPs from one study and 13 from another then, the input will look something liket this:
study_num	rsid	pval	n
1	rs109421300	6.94E-03	17925
1	rs110672723	3.14E-02	17925
1	rs135983637	4.59E-02	17925
1	rs137408198	5.18E-02	17925
1	rs135328690	5.49E-02	17925
1	rs109421300	2.51E-03	17925
1	rs110672723	5.54E-03	17925
1	rs135983637	1.41E-02	17925
1	rs137408198	2.25E-02	17925
1	rs135328690	2.94E-02	17925
2	rs380681629	9.79E-10	10597
2	rs207633422	6.93E-22	10597
2	rs378839347	4.23E-11	10597
2	rs379304770	4.8E-11	10597
2	rs135912796	8.36E-14	10597
2	rs136027702	4.72E-19	10597
2	rs797640658	0.00000000191	10597
2	rs453104040	3.38E-10	10597
2	rs109041054	0.00000000132	10597
2	611414	0.00000000302	10597
2	8636364	0.00000000122	10597
2	rs110749311	1.98E-12	10597
2	rs449946672	4.48E-10	10597
