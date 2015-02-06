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
  	return None
  else:
  	span = end - start
  	return {'chrom': chrom, 'span': span}

def print_bed(bed_dict):
  if bed_dict is None:
    print 'Bad data!'
  else:
    print 'Chrom:',bed_dict['chrom'], 'Span:',bed_dict['span']

print_bed(parse_bed(bed_string))
print_bed(parse_bed('chrX 20 33'))
print_bed(parse_bed('chr -1 4'))
