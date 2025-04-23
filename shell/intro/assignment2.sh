read -rp "enter value of a, b, c: " a b c

if [[ $a -gt $b && $a -gt $c ]]; then
    echo "a is the biggest number"
elif [[ $b -gt $c ]]; then
    echo "b is the biggest number"
else
    echo "c is the biggest number"
fi
