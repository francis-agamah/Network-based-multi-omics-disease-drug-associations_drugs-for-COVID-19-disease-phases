#!/usr/bin/env python3
# import statements
import os
import pandas as pd 
from rdflib import Graph, Literal, RDFS, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD #most common namespaces
from sys import argv

# functions

def parse_sif(f):
    # parsing the sif file to dataframe
    df = pd.read_csv(f, sep='\t', header=None)
    df[1] = None
    df[3] = None
    print (df)
    return df
    
def parse_refs_combine(path):
    # parsing the reference files to dataframes and ccombine them into 1 dataframe
    df_list = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            r_df = pd.read_csv(os.path.join(root, filename))
            df_list.append(r_df)
    lib_df = pd.concat(df_list)
    return lib_df

def df_onto_transformation_old(df, r_df):
    for row in df.index:
        if df.loc[row, 0] or df.loc[row, 2] in r_df['feature.name'].values:
            if '**' in df.loc[row, 0]:
                dfrow0 = df.loc[row, 0].replace('**', '')
            else:
                dfrow0 = df.loc[row, 0]
            if '**' in df.loc[row, 2]:
                dfrow2 = df.loc[row, 2].replace('**', '')
            else:
                dfrow2 = df.loc[row, 2]
            s_df = r_df[r_df['feature.name'].str.contains(str(dfrow0))]
            for r in s_df.iterrows():
                if r[1]['feature.name'] == dfrow0:
                    df.loc[row, 1] = f"{r[1]['database']}{r[1]['database.ID']}"
            t_df = r_df[r_df['feature.name'].str.contains(str(dfrow2))]
            for r in t_df.iterrows():  
                if r[1]['feature.name'] == dfrow2:
                    df.loc[row, 3] = f"{r[1]['database']}{r[1]['database.ID']}"
    df.to_csv(r'output/df.csv', index=False)
    return df


def df_onto_transformation(df, r_df):
    # Create a set of unique feature names from r_df for faster lookup
    r_feature_names = set(r_df['feature.name'].values)
    
    for row in df.index:
        row0 = df.loc[row, 0]
        row2 = df.loc[row, 2]
        
        if row0 in r_feature_names or row2 in r_feature_names:
            # Perform replacements if '**' is present
            if '**' in row0:
                row0 = row0.replace('**', '')
            if '**' in row2:
                row2 = row2.replace('**', '')
            
            # Filter r_df to find matching feature.name
            s_df = r_df[r_df['feature.name'] == row0]
            if not s_df.empty:
                df.loc[row, 1] = f"{s_df['database'].values[0]}{s_df['database.ID'].values[0]}"
            
            t_df = r_df[r_df['feature.name'] == row2]
            if not t_df.empty:
                df.loc[row, 3] = f"{t_df['database'].values[0]}{t_df['database.ID'].values[0]}"
    
    df.to_csv(r'output/df.csv', index=False)
    return df


def creating_graph(df, path):
    # creating the graph
    g = Graph()
    ncbi = Namespace('https://www.ncbi.nlm.nih.gov/nuccore/')
    uniprot = Namespace('https://www.uniprot.org/uniprotkb/')
    chebi = Namespace('https://www.ebi.ac.uk/chebi/')
    obo = Namespace('http://purl.obolibrary.org/obo/')
    g.bind('ncbi', ncbi)
    g.bind('uniprot', uniprot)
    g.bind('chebi', chebi)
    g.bind('obo', obo)
    is_associated_with = URIRef('http://purl.obolibrary.org/obo/PATO_0001668')
    for row in df.iterrows():
        if row[1][1] == None or row[1][3] == None:
            continue
        else:
            g.add((URIRef(f'{row[1][1]}'), is_associated_with, URIRef(f'{row[1][3]}')))
            g.add((URIRef(f'{row[1][1]}'), RDFS.label, Literal(row[1][0] ,datatype = XSD.string)))
            g.add((URIRef(f'{row[1][3]}'), RDFS.label, Literal(row[1][2] ,datatype = XSD.string)))
    g.serialize(destination = path, format = 'turtle')
    return

# main
if __name__ == "__main__":
    workdir = argv[1]
    lib_dir = argv[2]
    for root, dirs, files in os.walk(workdir):
        for filename in files:
            if filename.endswith('.sif'):
                df = parse_sif(os.path.join(root, filename))
    # parsing the tsv file
    #df = parse_sif(r'output/seed_top3_full_4-layers_PCC_0.1_threshold_severe_data_driven.sif')
    # parsing the reference file
    #transcriptomics_df = parse_ref(r'omics_feature_library\transcriptomics_Su_2020_feature-metadata.csv')
    #metabolomics_df = parse_ref(r'omics_feature_library\metabolomics_Su_2020_feature-metadata.csv')
    #proteomics_df = parse_ref(r'omics_feature_library\proteomics_Su_2020_feature-metadata.csv')
                lib_df = parse_refs_combine(lib_dir)
                onto_df = df_onto_transformation(df, lib_df)
                output_ttl_path = str(os.path.join(root, filename)).replace('.sif', '_new.ttl')
    # creating the graph
                g = creating_graph(onto_df, output_ttl_path)
    # adding the data to the graph