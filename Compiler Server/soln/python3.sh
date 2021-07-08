#!/bin/bash

	cd soln
	python3 temp.py &> error	
	cat error
	err=cat out1 | tail -n1 | awk '{print $1;}'
	echo {$err -6}

	# if [["$err"=="File" ] | ["$err"=="Traceback"]]
	# then
	# 	#compilation error exist
	# 	echo "compilation error"
	# 	cat error
	# else
	# 	time timeout -k 12s 13s  < input > output -m 1 #kb
	# 	if [[ -s output ]]
	# 	then 
	# 		#if no TLE
	# 		echo "not TLE"
	# 		cat ./output
	# 		echo "--------------------------"
	# 		cat ./out
	# 		if cmp -l  ./out ./output > /dev/null
	# 		then
	# 			#if correct answer
	# 			echo "accepted"
	# 		else
	# 			echo "wa"
	# 		fi
	# 	else
	# 		echo "TLE"
	# 	fi
	# 	rm output
	# fi
 #    rm temp.cpp
 #    rm error
 #    exit