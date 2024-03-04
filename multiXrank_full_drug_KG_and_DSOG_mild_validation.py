import multixrank
#command for quick working example
#multixrank.Example().write(path="airport")

workdir = '/random_walk/'
output_dir = '/random_walk/outdir'

#creating an object for the config file
multixrank_obj = multixrank.Multixrank(config="config_full_drug_KG_and_DSOG_mild_validation.yml", wdir=workdir)
#multixrank_obj = multixrank.Multixrank(config="config_full_covid_4-layers_PCC_0.1_threshold_drug_KG_ref.yml", wdir="/cbio/users/francis_agamah/SOFT/multiXrank")

print("multixrank_obj created")
print(multixrank_obj)

#perform random walk 
ranking_df = multixrank_obj.random_walk_rank()
print("ranking_df")
print(ranking_df)

##RANKING FOR DRUG
#ranking nodes
multixrank_obj.write_ranking(ranking_df, path=str(output_dir + "results_drug_KG_and_DSOG/mild"))


multixrank_obj.to_sif(ranking_df, path=str(output_dir + "/results_drug_KG_and_DSOG/mild/multi_layer_drug_KG_and_DSOG_mild.sif", top=3))

