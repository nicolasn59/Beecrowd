#include <stdio.h>
#include <stdlib.h>

int quicksort(int *arr, int start, int end);
int partitionAscending(int *arr, int start, int end);
int partitionDescending(int *arr, int start, int end);


int main(){
    int len;
    scanf("%d", &len);
    int *evenNumbers, *oddNumbers, number, evenCount=0, oddCount=0;
    evenNumbers = (int*) malloc(len*sizeof(int));
    oddNumbers = (int*) malloc(len*sizeof(int));
    while (len != 0){
        scanf("%d", &number);
        if (number % 2 == 0){
            evenNumbers[evenCount] = number;
            evenCount += 1;
        }
        else{
            oddNumbers[oddCount] = number;
            oddCount += 1;
        }
        len -= 1;
    } 

    // evenCount-1 and oddCount-1 are the final positions of the array
    quicksort(evenNumbers, 0, evenCount-1); 
    quicksort(oddNumbers, 0, oddCount-1);

    for (int i=0; i < evenCount; i++)
        printf("%d\n", evenNumbers[i]);
    for (int i=0; i < oddCount; i++)
        printf("%d\n", oddNumbers[i]);
    free(evenNumbers);
    free(oddNumbers);
}

int quicksort(int *arr, int start, int end){
    
    if (start < end)
    {
        if (arr[0] % 2 == 0) // if arr[0] == even number
        {
            int pivotPosition = partitionAscending(arr, start, end);
            quicksort(arr, start, pivotPosition-1);
            quicksort(arr, pivotPosition+1, end);
        }
        else // if arr[0] == odd number
        {
            int pivotPosition = partitionDescending(arr, start, end);
            quicksort(arr, start, pivotPosition-1);
            quicksort(arr, pivotPosition+1, end);
        }
    }
    return 0;
}

int partitionAscending(int *arr, int start, int end)
{
    int pivot = arr[end], i=start-1, temp;
    for (int j=start; j < end; j++)
    {
        if (arr[j] <= pivot)
        {
            i += 1;
            temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }
    }
    i += 1;
    temp = arr[i];
    arr[i] = arr[end]; // pivot == arr[end]
    arr[end] = temp;
    return i;
}


int partitionDescending(int *arr, int start, int end)
{
    int pivot = arr[end], i=start-1, temp;
    for (int j=start; j < end; j++)
    {
        if (arr[j] >= pivot)
        {
            i += 1;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    i += 1;
    temp = arr[i];
    arr[i] = arr[end]; //pivot == arr[end]
    arr[end] = temp;
    return i;
}
