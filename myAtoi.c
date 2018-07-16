#include <string.h>
int myAtoi(char* str) {
    long result = 0;
    int multiplier = 1;
    int i;
    for(i = 0; i < strlen(str); i++)
    {
        if(str[i] == ' ')
        {
            continue;
        }
        else if (str[i] == '+')
        {
            i++;
            break;
        }
        else if (str[i] == '-')
        {
            multiplier = -1;
            i++;
            break;
        }
        else if (str[i] < '0' || str[i] > '9')
        {
            return result;
        }
        if(str[i] >= '0' && str[i] <= '9')
        {
            break;
        }
    }
    for (i; i < strlen(str); i++)
    {
        if(str[i] < '0' || str[i] > '9')
        {
            break;
        }
        else
        {
            result = result * 10 + (str[i] - '0');
            if (result * multiplier >= INT_MAX)
            {
                return INT_MAX;
            }
            else if (result * multiplier <= INT_MIN)
            {
                return INT_MIN;
            }
        }
    }
    return result * multiplier;
}