#!/bin/bash

	# cd soln
	# g++ temp.cpp &> error	
	# cat error
	# if [[ -s error ]]
	# then
	# 	#compilation error exist
	# 	echo "compilation error"
	# 	cat error
	# else
	# 	timeout -k 2s 3s ./a.out < input > output
	# 	if [[ -s output ]]
	# 	then 
	# 		#if no TLE
	# 		echo "not TLE"
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


#######################################################################################


	# cd soln
 #    touch send
	# g++ temp.cpp &> error	
	# cat error
	# if [[ -s error ]]
	# then
	# 	#compilation error exist
	# 	echo "ce" &>> send
 #        cat error &>> send
	# else
 #        TIMEFORMAT=%R
	# 	(time timeout -k 12s 13s ./a.out < input > output -m 1)&>> send
	# 	if [[ -s output ]]
	# 	then 
	# 		#if no TLE
	# 		#echo "not TLE"
	# 		cat ./output
	# 		echo "--------------------------"
	# 		cat ./out
	# 		if cmp -l  ./out ./output > /dev/null
	# 		then
	# 			#if correct answer
	# 			#printf "accepted\n" &>> send
 #                sed -i '1s/^/ac\n/' send
	# 		else
	# 			#printf "wa\n" &>>send
 #                sed -i '1s/^/wa\n/' send
	# 		fi
	# 	else
	# 		echo "tle" &>> send
	# 	fi
	# 	rm output
	# fi
 #    rm temp.cpp
 #    rm error
 #    exit
     

##################################################################################


	# cd soln
 #    touch send
	# g++ temp.cpp &> error	
	# # cat error
	# if [[ -s error ]]
	# then
	# 	#compilation error exist
	# 	echo "ce" &>> send
 #        cat error &>> send
	# else
 #        TIMEFORMAT=%R
	# 	(time timeout -k 12s 13s ./a.out < input > output -m 1)&>> send
	# 	if [[ -s output ]]
	# 	then 
	# 		#if no TLE
	# 		#echo "not TLE"
	# 		# cat ./output
	# 		# echo "--------------------------"
	# 		# cat ./out
	# 		if cmp -l  ./out ./output > /dev/null
	# 		then
	# 			#if correct answer
	# 			#printf "accepted\n" &>> send
 #                sed -i '1s/^/ac\n/' send
	# 		else
	# 			#printf "wa\n" &>>send
 #                sed -i '1s/^/wa\n/' send
	# 		fi
	# 	else
	# 		echo "tle" &>> send
	# 	fi
	# 	rm output
	# fi
 #    rm temp.cpp
 #    rm error
 #    exit

##################################################################################
   


	cd soln
    send="${1}.send"
    temp="${1}.cpp"
    mv $2 $temp
    out="${1}.out"
    output="${1}.this"
	(g++ $temp -o $out) &> $send
	# cat error
	if [[ -s $send ]]
	then
		#compilation error exist
		sed -i '1s/^/ce\n/' $send
	else
		input_file="/media/input/"+"${1}.input"
		output_file="/media/output/"+"${1}.output"
        TIMEFORMAT=%R
		(time timeout -k 1s 2s ./$out < $input_file > $output -m 1)&>> $send
		dec=$?						#gives exit code
		# echo $dec
		if [[ $dec -eq 0 ]]
		then 
			# cat $output
			if cmp -l  ./output_file ./$output > /dev/null
			then
				#if correct answer
				# printf "accepted\n" &>> $send
                sed -i '1s/^/ac\n/' $send
			else
				# printf "wa\n" &>> $send
                sed -i '1s/^/wa\n/' $send
			fi
		else
			sed -i '1s/^/tle\n/' $send
		fi
		# cat $output
		rm $output
	fi
	cat $send
    rm $temp
    rm $out
    exit

 ########################################################################################
