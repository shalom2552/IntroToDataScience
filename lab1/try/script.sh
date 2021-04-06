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
# find the most apearing pair in book
awk '{
	for (i = 1; i < NF; i++)
		if ($i < $(i+1)) a[$i OFS $(i+1)]++
		else a[$(i+1) OFS $i]++
	}END {
		for (words in a)
			if (a[words] > a[m]) m = words
		print "most first word in the book : "m,a[m]
	}' Alice_book_clean.txt
# find the most apearing pair in chapters
cd chapters
for chapter in chapter_{1..12};
do
	awk '{
		for (i = 1; i < NF; i++)
			if ($i < $(i+1)) a[$i OFS $(i+1)]++
			else a[$(i+1) OFS $i]++
		}END {
			for (words in a)
				if (a[words] > a[m]) m = words
			print "most coomon pair in",FILENAME,":",m,a[m]
		}' $chapter
done
cd ..
echo "********************************"
# find most first word apearence in the book
awk '{
	b[$1]++
	}END {
		for (words in b)
			if (b[words] > b[m]) m = words
		print "most first word in the book :",m,b[m]
	}' Alice_book_clean.txt
# find most first word apearence in chapters
cd chapters
for chapter in chapter_{1..12};
do
	awk '{
		b[$1]++
		}END {
			for (words in b)
				if (b[words] > b[m]) m = words
			print "most first word in",FILENAME,":",m,a[m]
		}' $chapter
done
cd ..
echo "********************************"

# avg row length

# alice avg position in row
