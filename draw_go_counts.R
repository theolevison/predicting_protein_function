library(ggplot2)

go_counts <- read.csv(file="G:/diss/go_count.txt", header=TRUE, check.names=FALSE, strip.white=TRUE, quote="\"", sep=",",na.strings= c("NA", " ", ""))
adjust_counts <- subset(go_counts, Counts<250)
ggplot(adjust_counts, aes(x=Counts)) + geom_histogram(binwidth=10)+theme(text = element_text(size=20))+xlab('Number of Assigned GO Terms')+ylab('Number of PFAM domains')
ggsave("D:/diss/histogram_of_GO_counts.eps", device="eps", width=10, height=7, dpi=300)