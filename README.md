# Source Data

uniprot_trembl and id mappings from uniprot
interpro 88

## Data file generation:

### Scripts and their order

In theory if you run these scripts in order you will regenerate the word2vec model. (good luck!)

1) run pfilt for CC and LC over all of uniprot  
**SCRIPT**: `parse_masked_regions.py`  
parse the fasta files which have been masked for lc and cc sequence and output dummy interpro-like domain regions maskedregions.dat  
**PRODUCES**:  
`masked_regions.dat`
2) retrieve the disorder region assignments from interpro  
**SCRIPT**: `parse_match_complete.py`  
parse the interpro match_complete.xml to extract all the MOBIDB disorder regions  
**PRODUCES**:  
`disorder_regions.dat`
3) retrieve the pfam assignments from interpro  
`get_pf_ipr_assignments.py`  
parse the interpro file to remove only the pfam  
**PRODUCES**:  
`protein2ipr_pfam.dat`
4) assign the NCBI taxonomy information to the uniprot IDs  
**SCRIPT**: `map_taxonomy.py`
open the uniprot and ncbi tax data and add the taxa_id and kingdom to the pfam assignments  
**PRODUCES**:  
`protein2ipr_pfam_taxonomy.dat`  
`protein2ipr_pfam_taxonomy_withipr.dat`  
`masked_regions_taxonomy.dat`  
5) Use domain, masked and disorder regions to extract only eukaryotic proteins.  
**SCRIPT**: `extract_eukaryotic_proteins.py`  
**PRODUCES**:  
`protein2ipr_pfam_taxonomy_E.dat`  
`disorder_regions_taxonomy_E.dat`  
`masked_regions_taxonomy_E.dat`  
6) Build the domain regions set  
**SCRIPT**: `combine_domains.py`  
reads `disorder_regions_taxonomy.dat` and `masked_regions_taxonomy.dat` then interleaves these with `protein2ipr_pfam_taxonomy.dat`  
**PRODUCES**:  
`combined_domains_E.dat` (29,277,053 annoated segments)
7) Resolve domain region overlaps  
**SCRIPT**: `winnow_domains.py`  
reads the `combined_domains_E.dat` and outputs a smaller file which resolves any overlaps. Pfam domains take precedence over disorder, lc and cc regions Disorder is kept in favour of lc and cc. cc is kept in favour of lc. If Pfam domains conflict the longer one is kept.  
**PRODUCES**:  
`final_domains_E.dat` (25,776,649 annotated segments)  
8) Make pseudo-sentence strings  
**SCRIPT**: `construct_word2vec_strings.py`  
Run through the `final_domains_E.dat` and produce the word2 vec strings  
**PRODUCES**:  
`word2vec_input_E.dat` (9,030,650 sentences)
9) Build embedding  
**SCRIPT**: `build_vectors_word2vec.py`  
read the word2vec_input.dat sentences and train word2vec, word2vec training min_count=0, size=x? default 100  
**PRODUCES**: `word2vec.model`
10) get distances  
**SCRIPT**: `get_distance.py`  
read the gensim model and output the distance matrix produced  
**PRODUCES**: `word2vev_E.similarity` - cosine similarity matrix
11) annotate the pfam stuff  
**SCRIPT**: `annotate_pfam_go.py`  
read in interpro2go to get ipr to GO mapping. Read in `protein2ipr` to map uniprot to go via ipr lastly read `final_domains_E.dat` to work out which GO terms can be associated with which pfam domains  
**PRODUCES**: `pfam_go_mapping.csv`

# Analysis

These scripts did various bits and pieces of the embedding topology analysis for the paper itself. WARNING POSSIBLY THERE ARE SOME MISSING SCRIPTS (or maybe 7 and 8 are calculated when 6 is run)

1) get the pfam domain list and extract the DUFs  
used grep to produce
`DUF_list.txt` and `PfamID_list.txt`
2) Select 1,000 NON-duf domains  
`select_random_pfams.py` takes the lists and outputs 1,000 pfam domains  
`pfam_random_list.txt`
3) score what the accuracy would be if we didn't know their GO goterms on a gensims nearest neighbour basis. scrub `final_domains_E.dat` for all possible EUK pfam domains that COULD be predicted  
4) `calculate_nn_accuracy.py` - aggregates data and calculates the precision, and hit rate  
`summarise_accuracy.R` - total the accuracy scores we counted up
5) Annotate DUFs  
`annotate_dufs.py` takes the distance matrix and finds the nearest neighbour to each duf and outputs the putative annotations K=1. produces `duf_annotations.csv`

# Ancillary/Analysis

Some other bits of analysis or chart drawing for the paper that aren't algebra_output the embedding

1) calculate gap distribution over the uniprot pfam assignments information
used in `construct_word2vec_strings.py`  
`calculate_gaps.py` - protein2ipr_pfam_taxonomy.dat protein assignments and output a list of the gap lengths
2) calculate distribution of # of domains with x many GO terms  
`go_count_distribution.py`  
read in the `pfam_go_mapping.csv` output counts
3) `summary_stats.py`  
calculate the number of euk proteins, GO terms and PFam domains we see

1) `calculate_region_counts.py` - fraction of interpro sequences which are gap, domain, etc...  
**outputs**: assignment_statistics.csv
2) `count_gap_classes.py` - total up the number of proteins that have at least one of X gap count_gap_classes  
**outputs**: gap_class_populations.csv
3) `count_go_distribution` - read the pfam to go assignments and spit out go_counts.txt  
`draw_go_counts.R` - outputs histogram or less than 250
4) repurpose calculate_nn_accuracy.py to output stats for markov process. e.g: `python3 calculate_nn_accuracy.py 1 molecular_function > nn1_markov_accuracy_mf.csv`
`repurpose summarise_accuracy.R` - total the accuracy scores we counted up
