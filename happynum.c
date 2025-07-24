#include <stdio.h>

// Function to calculate sum of squares of digits
/*int sum_of_squares(int n) {
    int sum = 0;
    while (n > 0) {
        int digit = n % 10;
        sum += digit * digit;
        n /= 10;
    }
    return sum;
}*/

int main() {
    int num, i;

    printf("Enter a number: ");
    scanf("%d", &num);

    // Use a for loop to check for happy number (max 100 iterations to avoid infinite loop)
    for (i = 0; i < 100; i++) {
        int sum=0;
        int temp = num;
        // num = sum_of_squares(num);
        while (num > 0) {
        int digit = num % 10;
        sum += digit * digit;
        num /= 10;
        printf("%d ", sum);
        }
        printf("%d ", sum);
        // If it reaches 1, it's a happy number
        if (sum == 1) {
            printf("Happy Number \n");
            break ; // Exit the program
        }

        // If it reaches 4, it's not a happy number (cycle)
        if (sum == 4) {
            printf("Not a Happy Number \n");
            break ; // Exit the program
        }
       
        num=sum;
    }
    return 0;
}


