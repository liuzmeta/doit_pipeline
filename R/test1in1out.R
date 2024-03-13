args <- commandArgs(trailingOnly = TRUE)
input_data <- args[1]
output_data <- args[2]
input <- read.delim(input_data, header = FALSE)
writeLines(input_data, output_data)
print("test Rscript with 1 in 1 out")
print("-------in--------")
print(input_data)
print("-------out-------")
print(output_data)
