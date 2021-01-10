#include <stdio.h>



int main() {
    int T, h, w, n;
    int i;
    scanf("%d", &T);
    for (i = 0; i < T; ++i) {
        scanf("%d %d %d", &h, &w, &n);

        if (n % h) {                
            if (n / h + 1 >= 10)    
                printf("%d%d\n", n % h, n / h + 1);
            else                    
                printf("%d0%d\n", n % h, n / h + 1);
        }
        else {                      
            if (n / h >= 10)        
                printf("%d%d\n", h, n / h);
            else                   
                printf("%d0%d\n", h, n / h);
        }

    }

}
