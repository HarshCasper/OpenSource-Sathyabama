# https://www.hackerrank.com/challenges/variadic-functions-in-c/problem


int  sum (int count,...) {
    int sum = 0;

    // define a pointer to the variable list
    va_list ptr;
    // start the pointer to the list
    va_start(ptr, count);
    // access the argument pointed to in the list and increment position
    for (int i = 0; i < count; i ++) {
        sum += va_arg(ptr, int);
    }
    va_end(ptr);
    return sum;
}

int min(int count,...) {
    va_list ptr;
    va_start(ptr, count);
    
    int min = va_arg(ptr, int);
    int tmp;
    for(int i = 1; i < count; i ++) {
        if((tmp = va_arg(ptr, int)) < min) {
            min = tmp;
        }
    }
    va_end(ptr);
    return min;
}

int max(int count,...) {
    va_list ptr;
    va_start(ptr, count);
    
    int max = va_arg(ptr, int);
    int tmp;
    for(int i = 1; i < count; i ++) {
        if((tmp = va_arg(ptr, int)) > max) {
            max = tmp;
        }
    }
    va_end(ptr);
    return max;
}
