
 #!/bin/bash

#convert string layout

englett=(z " " x c v b n m , . '/' a s d f g h j k l ';' "'" q w e r t y u i o '[' ']' p)
heblett=(ז " " ס ב ה נ מ צ ת ץ . ש ד ג כ ע י ח ל ך ף , '/' "'" ק ר א ט ו ן ם פ ']' '[' פ )
echo "what do you have to say?"
read wrongStr
 # find wrong layout 
if [[ " ${englett[*]} "  =~ "${wrongStr:0:1}" ]]; then
    english=1
    wrongStr=$(echo $wrongStr | tr '[:upper:]' '[:lower:]')
    setxkbmap il,us
else
    english=0	
    setxkbmap us,il
fi 
#fix wrong string
for (( i=0 ; i < ${#wrongStr} ; i++ )) do
    if [[ $english == 1 ]]; then
    	         #for (( x=0 ; ${wrongStr:i:1} != ${englett[x]} ; x=++x )) do        האם אפשר עשות
    	for x in ${!englett[*]} 34     #find char index
    	do
    	    if [ "${wrongStr:i:1}" == "${englett[$x]}" ]
    	     then
    		ind=$x
    		break
    	    fi
    	done
                 #ind=$(${englett[@]/${wrongStr:i:1}/1} | cut -d1 -f1 | wc -w | tr -d ' ' )  find char index  מה לא בסדר
        if [ $x -eq 34 ] #not a letter
        then
        correctStr=$correctStr${wrongStr:i:1}
        else
        correctStr=$correctStr${heblett[$ind]}
        fi

    else
    	for x in ${!heblett[*]} 
    	do
    	    if [ "${wrongStr:i:1}" == "${heblett[$x]}" ]
    	     then
    		ind=$x
    		break
    	    fi
    	done
        if [ $x -eq 34 ]
        then
        correctStr=$correctStr${wrongStr:i:1}
        else
        correctStr=$correctStr${englett[$ind]}
        fi
    fi
done

 echo $correctStr

