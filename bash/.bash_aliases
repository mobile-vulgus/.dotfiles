#    ___  ___   ______ __   
#   / _ )/ _ | / __/ // /   
#  / _  / __ |_\ \/ _  /    
# /____/_/_|_/___/_//_/     

#  ___ _/ (_)__ ____ ___ ___
# / _ `/ / / _ `(_-</ -_|_-<
# \_,_/_/_/\_,_/___/\__/___/
                    

alias ll='ls -aCF'
alias la='ls -ax'
alias cv='clear'
alias si3='vim .config/i3/config'
alias si3s='vim .config/i3status/config'
alias scm='vim .config/compton.conf'
alias shcolor='function colorgrid( )
{
    iter=16
    while [ $iter -lt 52 ]
    do
        second=$[$iter+36]
        third=$[$second+36]
        four=$[$third+36]
        five=$[$four+36]
        six=$[$five+36]
        seven=$[$six+36]
        if [ $seven -gt 250 ];then seven=$[$seven-251]; fi

        echo -en "\033[38;5;$(echo $iter)m█ "
        printf "%03d" $iter
        echo -en "   \033[38;5;$(echo $second)m█ "
        printf "%03d" $second
        echo -en "   \033[38;5;$(echo $third)m█ "
        printf "%03d" $third
        echo -en "   \033[38;5;$(echo $four)m█ "
        printf "%03d" $four
        echo -en "   \033[38;5;$(echo $five)m█ "
        printf "%03d" $five
        echo -en "   \033[38;5;$(echo $six)m█ "
        printf "%03d" $six
        echo -en "   \033[38;5;$(echo $seven)m█ "
        printf "%03d" $seven

        iter=$[$iter+1]
        printf '\r\n'
    done
}'
