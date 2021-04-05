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