# Random walk workflow

## Docker

### Build from Dockerfile

```
git clone https://gitlab.cmbi.umcn.nl/x-omics-twoc/randomwalk.git
cd randomwalk/
docker build -t random_walk_workflow:v0.3 . 
```

### Build docker container and mount local directory
```
# ${pwd} should be pointing to randomwalk/
docker  run  -it -d  --name container_name -v ${pwd}:/random_walk random_walk_workflow:v0.3 
```

### Execute docker container, specifying Python script
``` 
# Example with mild script
docker exec -i container_name python3 multiXrank_full_drug_KG_and_DSOG_mild.py config_full_drug_KG_and_DSOG_mild.yml
```

### Execute docker container for the moderate disease state.
``` 
# Example with mild script
docker exec -i container_name python3 multiXrank_full_drug_KG_and_DSOG_moderate.py config_full_drug_KG_and_DSOG_moderate.yml
```


Output files should be found in `randomwalk/outdir/`