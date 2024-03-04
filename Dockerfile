# Dockerfile VERSION = v0.2
# docker build -t random_walk_workflow$VERSION . 

FROM continuumio/miniconda3

RUN conda create --name multixrank python=3.10 -y
RUN python3 -m pip install multixrank
RUN python3 -m pip install scipy==1.8

WORKDIR /random_walk/

#ENTRYPOINT [ "python3", "multiXrank_full_drug_KG_and_DSOG.py", "config_full_drug_KG_and_DSOG_mild.yml"]