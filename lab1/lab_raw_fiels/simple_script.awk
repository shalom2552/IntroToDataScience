BEGIN{ 
      FS=","
}
{if ($1!=$3) 
print $2; $4=$1; print;}END{print "number of lines: "NR;}
