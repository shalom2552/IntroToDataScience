#!/bin/bash
stop_words=(a about above across after afterwards again against all almost alone along
already also although always am among amongst amoungst amount an and another any
anyhow anyone anything anyway anywhere are around as at back be became because
become becomes becoming been before beforehand behind being below beside besides
between beyond bill both bottom but by call can cannot cant co computer con could
couldnt cry de describe detail do done down due during each eg eight either eleven else
elsewhere empty enough etc even ever every everyone everything everywhere except few
fifteen fify fill find fire first five for former formerly forty found four from front full further
get give go had has hasnt have he hence her here hereafter hereby herein hereupon hers
herself him himself his how however hundred i ie if in inc indeed interest into is it its itse
keep last latter latterly least less ltd made many may me meanwhile might mill mine more
moreover most mostly move much must my myse name namely neither never
nevertheless next nine no nobody none noone nor not nothing now nowhere of off often
on once one only onto or other others otherwise our ours ourselves out over own part per
perhaps please put rather re same see seem seemed seeming seems serious several she
should show side since sincere six sixty so some somehow someone something sometime
sometimes somewhere still such system take ten than that the their them themselves
then thence there thereafter thereby therefore therein thereupon these they thick thin
third this those though three through throughout thru thus to together too top toward
towards twelve twenty two un under until up upon us very via was we well were what
whatever when whence whenever where whereafter whereas whereby wherein
whereupon wherever whether which while whither who whoever whole whom whose
why will with within without would yet you your yours yourself yourselves )

# Alice book to lower case 
awk '{print tolower($0)}' Alice_book | tr -cd '\ \t\n[:alnum:]' > Alice_book_clean.txt

# remove stop words 
for i in ${stop_words[@]};
	do
		sed -i "s/\<$i\>//g" Alice_book_clean.txt
done

#remove start line spaces and empty rows
sed '/^[[:space:]]*$/d' -i Alice_book_clean.txt
sed "s/^[ \t]*//" -i Alice_book_clean.txt

# splite book to chapters
rm -rf chapters
mkdir chapters
awk 'BEGIN{RS="chapter "}{
	if (NR!=1)
		{print > "chapters/chapter "(NR-1);}
	}' Alice_book_clean.txt

# find the most common pair and the Most common first word in book
rm -f output.txt
touch output.txt
awk '{
	b[$1]++;
	for (i = 1; i < NF; i++)
		if ($i < $(i+1)) a[$i OFS $(i+1)]++
		else a[$(i+1) OFS $i]++;

	}END {
		for (words in a)
			if (a[words] > a[m]) m = words
		print "Most common pair in the book:",m;
		for (words in b)
			if (b[words] > b[m]) m = words
		print "Most common first word in the book:",m
	}' Alice_book_clean.txt >> output.txt

# find the most common pair and the Most common first word in each chapter
cd chapters
for n in {1..12};
do
	awk '{
		b[$1]++;
		for (i = 1; i < NF; i++)
			if ($i < $(i+1)) a[$i OFS $(i+1)]++
			else a[$(i+1) OFS $i]++
		}END {
			for (words in a)
				if (a[words] > a[m]) m = words
			print "Most common pair in",FILENAME":",m;
			for (words in b)
				if (b[words] > b[m]) m = words
			print "Most common first word in",FILENAME":",m
		}' "chapter "$n >> ../output.txt 
done 
cd ..

# avg row length
awk 'BEGIN{sum=0}
	{sum+=NF}END{print "Average line length:",sum/NR
}' Alice_book_clean.txt >> output.txt

# number of lines shorter then the avg
awk 'BEGIN{sum=0}
	{if (NF <= 4) sum+=1}
	END{print "Number of lines shorter than the average:",sum
}' Alice_book_clean.txt >> output.txt

# alice avg position in row
awk 'BEGIN{pos=0;indicator=0;count=0}
    {n=1;for(i=1;i<=NF;i++){
        if($i == "alice"){pos = pos + n;indicator=1}n++;}
    if(indicator==1){count++; indicator=0};
    }
    END{print "Average place of Alice in a line: "pos/count
}' Alice_book_clean.txt >> output.txt

# remove all trash leftovers
rm -rf chapters Alice_book_clean.txt
cat output.txt