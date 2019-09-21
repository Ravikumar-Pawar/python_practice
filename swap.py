// you
can
also
use
imports,
for example:
    // import java.util. *;

    // you
    can
    write
    to
    stdout
    for debugging purposes, e.g.
        // System.out.println("this is a debug message");


    class Solution
        {
            int
        findMaximumApplesImpl(int
        A[], int
        k, int
        l)
        {int
        max = -1;
        int
        Alice = 0, Bob = 0;
        int
        total = k + l;
        int
        lA = A.length;

        if (total > lA)
        {


    return -1;
    }

    int
    sum[] = new
    int[1000];
    sum[0] = A[0];
    for (int i=1;i < A.length;i++)
    {
        sum[i] = sum[i - 1] + A[i];
    }


    for (int i=0;i+k-1 < A.length;i++)
    {
        if (i > 0)
            Alice = sum[i + k - 1] - sum[i - 1];
        else
            Alice = sum[i + k - 1];
        for (int j=i+k;j+l-1 < A.length;j++)
            {
            if (j > 0)
            Bob = sum[j + l - 1] - sum[j - 1];
            else
            Bob = sum[j + l - 1];
            if (Alice + Bob > max)
            {
            max=Alice+Bob;
            }
            }
    }
    return max;
    }

    public
    int
    solution(int[]
    A, int
    K, int
    L)
    {
    // write
    your
    code in Java
    SE
    8
    int
    p = findMaximumApplesImpl(A, K, L);
    int
    q = findMaximumApplesImpl(A, L, K);
    return Math.max(p, q);

    }
    }