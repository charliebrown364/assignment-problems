#include <iostream>
#include <cassert>

int a(int n) {
    if(n == 0) {
        return 0;
    } else if(n == 1) {
        return 1;
    } else {
        return a(n - 1) + 2 * a(n - 2);
    }
}

// I have no idea why this isn't working

int seqSum(int n) {
    int sum;
    for(int i = 0; i <= n; i++) {
        sum += a(i);
    }
    return sum;
}

int extendedSeqSum(int n) {
    int sum;
    for(int i = 0; i <= n; i++) {
        sum += a(i);
    }
    return seqSum(sum);
}

int main()
{
    std::cout << "Testing...\n";
    
    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!";

    return 0;
}