#include <stdio.h>
#include "billing.h"

long calculate_bill(int units)
{
    long bill = FIXED_CHARGE;

    if (units > 200)
        bill += (units - 200) * RATE3;

    if (units > 100)
    {
        int slab = (units < 200) ? units - 100 : 100;
        bill += slab * RATE2;
    }

#ifdef DEBUG
    printf("DEBUG: Units = %d, Bill = %ld\n", units, bill);
#endif

    return bill;
}

int main()
{
    int units;

    printf("Enter units consumed: ");
    scanf("%d", &units);

    printf("Total Bill = Rs %ld.%02ld\n",
           calculate_bill(units) / 100,
           calculate_bill(units) % 100);

    return 0;
}
