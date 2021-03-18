"""
name=0
fo = open("sorted.txt", "rw+")
print "Name of the file: ", fo.name

#seq = ["This is 6th line\n", "This is 7th line"]
# Write sequence of lines at the end of the file.
#fo.seek(0, 2)
#line = fo.writelines( seq )

# Now read complete file from beginning.
fo.seek(1,0)
for name in range(7):
   line = fo.next()
   print (" %d . %s" % (name, line))

# Close opend file
fo.close()
"""
"""
import csv
with open("Employee2.txt","r")as file:
   reader=csv.reader(file)
   for row in reader:
      print(row)
"""
"""
import csv
with open("Employee2.csv","r")as file:
   reader=csv.reader(file)
   for line in reader:
      print(line[0])
"""

import csv
with open("Employee2.txt","rb")as file:
   csv_reader=csv.reader(file,delimiter=',')
   line=0
   for row in csv_reader:
      #print(row)
      if line==0:
         #print(f'Column names are {", ".join(row)}')
         print('Column names are %s'%", ".join(row))
        
         line+=1
      else:
         #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
         # print('%s', %row[0] 'works in the %s',%row[1] ' and was born in %d',%row[2]) 
         print('{0} work in the {1} department,and age {2} '.format(row[0],row[1],row[2]) )
         line+=1
file.close()         
"""
with open("Wfile.txt","wb")as file2:
   csv_writer=csv.writer(file2)
   writer.writerows(line)
file2.close()
"""      