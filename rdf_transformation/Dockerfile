# Dockerfile VERSION = v0.1
# docker build -t randomwalk_rdf$VERSION . 

FROM continuumio/miniconda3

RUN conda create --name rdf python=3.10 -y
RUN python3 -m pip install rdflib
RUN python3 -m pip install pandas

WORKDIR /rdf_transformation/

#to COPY the remote file at working directory in container
COPY output_to_rdf.py .

ENTRYPOINT [ "python3", "output_t_rdf.py", ".\output\", ".\omics_feature_library\"]