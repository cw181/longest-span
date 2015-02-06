small tweak
# test change
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
  	return {'chrom': chrom, 'span': span, 'chromStart': start, 'chromEnd':end}

def print_bed(bed_dict):
  if bed_dict is None:
    print 'Bad data!'
  else:
    print 'Chrom:',bed_dict['chrom'], 'Span:',bed_dict['span'], 'Start:', bed_dict['chromStart'], 'End:', bed_dict['chromEnd']
    # you could also use a built in function to print all the keys and values - check documentation

def is_longest_span(bed_dict, longest_dict):
  if longest_dict is None:
    return True
  previous_longest = longest_dict['span']
  span = bed_dict['span']
  return span > previous_longest
  
longest_dict = None
for line in fileinput.input():      #this allows you to type the input file as a parameter from bash when you call the python script (i.e. python longest_span_v6.py a.bed
  bed_dict = parse_bed(line)
  if is_longest_span(bed_dict, longest_dict):
    longest = bed_dict
print_bed(longest)

 
