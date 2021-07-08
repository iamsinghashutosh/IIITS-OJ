#!/bin/bash

	# cd soln
	# javac temp.java &> error	
	# cat error
	# if [[ -s error ]]
	# then
	# 	#compilation error exist
	# 	echo "compilation error"
	# 	cat error
	# else
	# 	time timeout -k 12s 13s java temp < input > output -m 1 #kb
	# 	if [[ -s output ]]
	# 	then 
	# 		#if no TLE
	# 		echo "not TLE"
	# 		cat ./output
	# 		echo "--------------------------"
	# 		cat ./out
	# 		if cmp -l  ./out ./output > /dev/null
	# 		then
	# 			echo "accepted"
	# 		else
	# 			echo "wa"
	# 		fi
	# 	else
	# 		echo "TLE"
	# 	fi
	# 	rm output
	# fi
 #    rm temp.java
 #    rm error
 #    exit

 	cd soln
    send="${1}.send"
    temp="${1}.java"
    mv $2 $temp
    # out="${1}.java"
    output="${1}.this"
	(javac $temp) &> $send
	# cat error
	if [[ -s $send ]]
	then
		#compilation error exist
		sed -i '1s/^/ce\n/' $send
	else
        TIMEFORMAT=%R
		(time timeout -k 12s 13s java $1 < input > $output -m 1)&>> $send
		if [[ -s $output ]]
		then 
			# cat $output
			if cmp -l  ./out ./$output > /dev/null
			then
				#if correct answer
				# printf "accepted\n" &>> $send
                sed -i '1s/^/ac\n/' $send
			else
				# printf "wa\n" &>> $send
                sed -i '1s/^/wa\n/' $send
			fi
		else
			echo "tle" &>> $send
		fi
		cat $output
		rm $output
	fi
	cat $send
    rm $temp
    rm "$1.class"
    exit
