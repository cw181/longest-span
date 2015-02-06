# Input Data
bed_string = 'chr1 6 12'
#len(bed_string)

def parse_bed(bed_string):
  # Parsing
  bed_list = bed_string.split()
  chrom = bed_list[0]
  start = int(bed_list[1])
  end = int(bed_list[2])
  
  if start < 0 or start > end:
  	print 'bad data!'
  else:
  	span = end - start
  	print 'Chrom:', chrom, 'Span:', span
parse_bed(bed_string)
parse_bed('chr -1 4')
