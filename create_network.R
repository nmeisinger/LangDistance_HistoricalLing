#!/usr/bin/env Rscript


# usage $ Rscript --vanilla create_network.R files_used_in_essay/all_lang.csv test.pdf
library(ape)
library(phangorn)

args = commandArgs(trailingOnly = TRUE)
in_f = args[1]
out_f = args[2]

data = read.table(in_f, header=TRUE, sep=",", row.names = 1)
nnet = neighborNet(data)

pdf(out_f,width=30,height=30)
plot(nnet, "2D", width=100, height=105)
dev.off()