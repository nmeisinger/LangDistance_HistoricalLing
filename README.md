# LangDistance_HistoricalLing
Final Project for Historical Linguistics in the New Age

How to use:

Create distance matrix and phyolgenetic tree:

`$ python3 kwic.py -f Germanic_Lang_ASJP.csv -o Test`
Ouput: `Test.csv` and `tree_Test.png`

Create phylogenentic network:

`$ Rscript --vanilla create_network.R Test.csv network_Test.pdf`
Output: `network_Test.pdf`

Note: Only tested on Linux systems
