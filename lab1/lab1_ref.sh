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


#******* deleting punct, stop words, empty line and such**************

#changing all to lowercase and removing puncts
sed "s/\(.\)/\L\1/g" Alice_book | sed "s/[[:punct:]]\+//g" > Alice_book_edited

#removing stop wards
for i in ${stop_words[@]};
	do
		sed -i "s/\<$i\>//g" Alice_book_edited
done

#double spaces to one space
sed -i "s/[[:space:]][[:space:]]*/ /g" Alice_book_edited

#spaces in the start of the line
sed -i "s/^[[:space:]]*//g" Alice_book_edited

#full spaces line
sed -i '/^$/d' Alice_book_edited

#******* end of deleting punct, stop words, empty line and such**************

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#             QUESTION 1
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------


#*************creating chaters files*****************
#create a file to each chapter
mkdir alice_chapters
awk '
	BEGIN{n=0;}
	{if($1=="chapter") n++;
	if(n > 0) print > "alice_chapters/chapter_"n}
' Alice_book_edited
#*********end of creting chapters files************


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#             QUESTION 2
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------


#*******q2a all book******************

#creating all the pairs in the books in a file and sorting it alphabetically
awk '{
	for (t=1;t<NF;t++){
		string=$(t+1) " " $t;
		if($t < $(t+1)){string=$t " " $(t+1);}fi
		print string;
	}
}' Alice_book_edited > pairs
sort -t= pairs -o pairs

#find the most common pair in the book
awk '{++a[$0]}END{for(i in a)if(a[i]>max){max=a[i];k=i}print "Most common pair in the book: "k}' pairs >> output.txt

#creating a file with all the first words and sorting it
awk ' BEGIN{}{print $1}' Alice_book_edited > first_words
sort -t= first_words -o first_words

#find the most common first word in the book
awk '{++a[$0]}END{for(i in a)if(a[i]>max){max=a[i];k=i}print "Most common first word in the book: "k}' first_words >> output.txt

#********end of q2a all book************


#************q2a each champer************
for n in {1..12}
do
	#creating all the pairs in the chapters in a file and sorting it alphabetically
	awk '{
		for (t=1;t<NF;t++){
			string=$(t+1) " " $t;
			if($t < $(t+1)){string=$t " " $(t+1);}fi
			print string;
		}
	}' "alice_chapters/chapter_"$n > "alice_chapters/pairs_"$n
	sort -t= "alice_chapters/pairs_"$n -o "alice_chapters/pairs_"$n
		
	#find the most common pair in the book
	awk -v var=$n '{++a[$0]}END{for(i in a)if(a[i]>max){max=a[i];k=i}print "Most common pair in cpater "var" is: "k}' "alice_chapters/pairs_"$n >> output.txt


	#creating a file with all the first words and sorting it
	awk ' BEGIN{}{print $1}' "alice_chapters/chapter_"$n > "alice_chapters/firstwords_"$n
	sort -t= "alice_chapters/firstwords_"$n -o "alice_chapters/firstwords_"$n
	#find the most common first word in the chapter
	awk -v var=$n '{++a[$0]}END{for(i in a)if(a[i]>max){max=a[i];k=i}print "Most common first word in capter "var" is: "k}' "alice_chapters/firstwords_"$n >> output.txt
done

#********q2a each champer************


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#             QUESTION 3
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#prints the number of words in each line to a separated
awk '{ print NF, $0 }' Alice_book_edited > Lines_counter
sed 's/^[^0-9]*//g' Lines_counter > words
 
#counts all the words in the file, counts num of lines in the file
Var=$(awk 'BEGIN {counter = 0; n=0}
    {counter = counter + $0; n++}
    END {print counter/n}' words )

printf "Average line length: %.1f\n" $Var >> output.txt

#print how much lines are shorter than the average line
awk -v mid=$Var ' BEGIN {n=0} 
    {if($1 < mid) n++;}
    END{print "Number of lines shorter than the average: "n}' words >> output.txt




#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#             QUESTION 4
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#returns the average location of the string "alice"
avg4=$(awk ' BEGIN{pos=0;j=0;k=0}
    {n=1;for(i=1;i<=NF;i++){
        if($i == "alice"){pos = pos + n;j=1}n++;}
    if(j==1){k++; j=0};
    }
    END{print pos/k}' Alice_book_edited )

printf "Average place of Alice in a line: %.1f\n" $avg4 >> output.txt


