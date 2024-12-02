{
    a[i] = $1
    b[i++] = $2
}

END {
    asort(a)
    asort(b)

    while (i > 0) {
        diff = a[i] - b[i]
        sum += (diff < 0) ? -diff : diff
        i--
    }

    print sum
}
