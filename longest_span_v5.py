import fileinput

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

for line in fileinput.input():      #this allows you to type the input file as a parameter from bash when you call the python script (i.e. python longest_span_v6.py a.bed
  print_bed(parse_bed(line))

