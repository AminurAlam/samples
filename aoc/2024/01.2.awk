{
    a[i] = $1
    b[i] = $2
    i++
}

END {
    for (i in a) {
        count = 0
        for (j in b) {
            if (a[i] == b[j]) count++
        }
        sum += (a[i]*count)
    }

    print sum
}
