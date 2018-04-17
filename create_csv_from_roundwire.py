


with open("roundwire.txt") as INFILE:

   used_data = []
   linecount = 1;
   for line in  INFILE:
      #print line
      if linecount < 13:
          linecount += 1
          continue

      line = line.rstrip()
      line = line.lstrip()

      if len(line) == 0:
         continue
      if 'preference' in line:
         continue

      wire_data = line.split()
      

      wire = {}
      wire["bare_diameter"] = wire_data[0]
      if len(wire_data) == 10:
         wire["gd_1_diameter"] = wire_data[7]
         wire["gd_2_diameter"] = wire_data[9]
         used_data.append(wire)
         continue
      elif len(wire_data) == 13:
         wire["gd_1_diameter"] = wire_data[7]
         wire["gd_2_diameter"] = wire_data[9]
         used_data.append(wire)
         continue
      elif len(wire_data) == 14:
         wire["gd_1_diameter"] = wire_data[8]
         wire["gd_2_diameter"] = wire_data[10]
         used_data.append(wire)
         continue
      elif len(wire_data) == 12:
         wire["gd_1_diameter"] = wire_data[6]
         wire["gd_2_diameter"] = wire_data[8]
         used_data.append(wire)
         continue
      elif len(wire_data) == 9:
         wire["gd_1_diameter"] = wire_data[6]
         wire["gd_2_diameter"] = wire_data[8]
         used_data.append(wire)
         continue
      else:
         print "Unable to parse line"
         

with open("wire_sizes.csv", "w") as OUTFILE:
     OUTFILE.write('"bare wire diameter","grade 1 diameter","grade 2 diameter"\n')

     for wire in used_data:
	diameter = wire["bare_diameter"]
        g1 = wire["gd_1_diameter"]
        g2 = wire["gd_2_diameter"]

	if '*' in diameter:
           diameter = diameter.lstrip('*')
        OUTFILE.write("%s,%s,%s\n" % (diameter,g1,g2))




