read -rp "enter a, b: " a b
read -rp "enter operation: " op

case "$op" in
1) echo "a + b =" $((a + b)) ;;
2) echo "a - b =" $((a - b)) ;;
3) echo "a * b =" $((a * b)) ;;
4) echo "a / b =" $((a / b)) ;;
*) echo "wrong input" ;;
esac
