read -rp "enter a number: " num
cpy=$num

while [[ "$num" -gt 0 ]]; do
    rev=$((rev * 10 + num % 10))
    num=$((num / 10))
done

if [[ "$rev" -eq "$cpy" ]]; then
    echo "$cpy is a palindrome"
else
    echo "$cpy is NOT a palindrome"
fi
