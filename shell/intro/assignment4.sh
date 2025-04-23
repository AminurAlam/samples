read -rp "enter a number: " n

for ((i = 0; i < n; i++)); do
    if [[ $((n % i)) -eq 0 ]]; then
        echo "NOT prime"
        exit
    fi
done

echo "prime"
