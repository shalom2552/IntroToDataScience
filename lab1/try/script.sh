#!/bin/bash

# split stop words
cat stop_words.txt | tr " " "\n" > stop_words_lines.txt

# Alice book to lower case 
awk '{print tolower($0)}' Alice_book | tr -cd '\ \t\n[:alnum:]' > Alice_book_clean.txt

# remove stop words !!! stop words are need to be in a separated file conatined only one word per line
while IFS= read -r word; do 
	sed -ri "s/( |)\b$word\b//g" Alice_book_clean.txt; 
done < stop_words_lines.txt

#remove start line spaces and empty rows
sed '/^[[:space:]]*$/d' -i Alice_book_clean.txt
sed "s/^[ \t]*//" -i Alice_book_clean.txt

# splite book to chapters
rm -rf chapters
mkdir chapters
awk 'BEGIN{RS="chapter "}{
	if (NR!=1)
		{print > "chapters/chapter_"(NR-1);}
	}' Alice_book_clean.txt

# find the most common pair and the Most common first word in book
awk '{
	b[$1]++;
	for (i = 1; i < NF; i++)
		if ($i < $(i+1)) a[$i OFS $(i+1)]++
		else a[$(i+1) OFS $i]++;

	}END {
		for (words in a)
			if (a[words] > a[m]) m = words
		print "Most common pair in the book: "m;
		for (words in b)
			if (b[words] > b[m]) m = words
		print "Most common first word in the book: ",m
	}' Alice_book_clean.txt

# find the most common pair and the Most common first word in each chapter
cd chapters
for chapter in chapter_{1..12};
do
	awk '{
		b[$1]++;
		for (i = 1; i < NF; i++)
			if ($i < $(i+1)) a[$i OFS $(i+1)]++
			else a[$(i+1) OFS $i]++
		}END {
			for (words in a)
				if (a[words] > a[m]) m = words
			print "Most common pair for",FILENAME":",m;
			for (words in b)
				if (b[words] > b[m]) m = words
			print "Most common first word for",FILENAME":",m
		}' $chapter
done
cd ..

# avg row length
awk 'BEGIN{sum=0}{sum+=NF}END{print "Average line length:",sum/NR}' Alice_book_clean.txt

# number of lines shorter then the avg
awk 'BEGIN{sum=0}
	{if (NF <= 4) sum+=1}
	END{print "Number of lines shorter than the average:",sum
}' Alice_book_clean.txt

# alice avg position in row
awk 'BEGIN{pos=0;indicator=0;count=0}
    {n=1;for(i=1;i<=NF;i++){
        if($i == "alice"){pos = pos + n;indicator=1}n++;}
    if(indicator==1){count++; indicator=0};
    }
    END{print "Average place of Alice in a line: "pos/count}' Alice_book_clean.txt

# remove all trash leftovers
rm -rf chapters Alice_book_clean.txt stop_words_lines.txt