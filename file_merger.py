import pandas as pd
import numpy as np
import argparse

def annotate(go,deg):
    df_go = pd.read_csv(go)
    df_deg = pd.read_excel(deg, header = 1)
    df_deg.rename(columns={df_deg.columns[0]: "GeneID"}, inplace = True)
    df_go.rename(columns={df_go.columns[0]: "GeneID"}, inplace = True)
    df_annotated_deg = pd.merge(df_deg, df_go, on = "GeneID")
    df_annotated_deg.drop(['Ensembl Gene ID', 'Entrez', 'Species', 'Position (Mbp)', 'Description'], axis = 1, inplace = True)
    list1 = list(df_annotated_deg.columns[1:-9])
    list2 = ['GeneID', 'Symbol', 'Gene Type', 'Chr', 'padj', 'log2FoldChange', 'pvalue', 'stat', 'foldChange',
                     'log10padj']
    list2.extend(list1)
    df_annotated_deg = df_annotated_deg.reindex(columns=list2)
    new_file_name = deg.split(".xlsx")[0] + "_new.xlsx"
    df_annotated_deg.to_excel(f"{new_file_name}", index = False)
if __name__=="__main__":
    parser = argparse.ArgumentParser(description ='Annotate DEG')
    parser.add_argument('-g', '--go', type = str, metavar = '', required = True, help = 'GO Excel')
    parser.add_argument('-d', '--deg', type = str, metavar = '', required = True, help = 'Deg Excel')
    args = parser.parse_args()
    annotate(args.go, args.deg)
