line <- readChar("G:/diss/duf_annotation_depths.csv", file.info("G:/diss/duf_annotation_depths.csv")$size-1)
number_list <- unlist(strsplit(line, split=","))
number_list <- number_list [! number_list %in% '-']
number_list <- as.integer(number_list)
mean(number_list)
hist(number_list)