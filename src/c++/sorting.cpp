#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <vector>
#include<algorithm>
#include <string>
using namespace std;
unsigned t0, t1;


void selectionSort(int dizi[], int elemanSayisi) {
    int i, j, enKucuk, temp;
    for (i = 0; i < elemanSayisi - 1; i++) {
        enKucuk = i;
        for (j = i + 1; j < elemanSayisi; j++) {
            if (dizi[j] < dizi[enKucuk])
                enKucuk = j;
        }
        temp = dizi[i];
        dizi[i] = dizi[enKucuk];
        dizi[enKucuk] = temp;
    }
}
void insertionSort(int dizi[], int elemanSayisi) {
    int i, j, temp;
    for (i = 1; i < elemanSayisi; i++) {
        j = i;
        while (j > 0 && dizi[j - 1] > dizi[j]) {
            temp = dizi[j];
            dizi[j] = dizi[j - 1];
            dizi[j - 1] = temp;
            j--;
        }
    }
}
void bubbleSort(int dizi[], int elemanSayisi) {
    int temp;
    int i, j;

    for (i = 1; i < elemanSayisi; i++) {
        for (j = 0; j < elemanSayisi - i; j++) {
            if (dizi[j] > dizi[j + 1]) {
                temp = dizi[j];
                dizi[j] = dizi[j + 1];
                dizi[j + 1] = temp;
            }
        }
    }
}
void shellSort(int dizi[], int elemanSayisi) {
    int j;
    for (int gap = elemanSayisi / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < elemanSayisi; ++i) {
            int temp = dizi[i];
            for (j = i; j >= gap && temp < dizi[j - gap]; j -= gap) {
                dizi[j] = dizi[j - gap];
            }
            dizi[j] = temp;
        }
    }
}

void merge(int arr[], int p, int q, int r) {
  int n1 = q - p + 1;
  int n2 = r - q;
  int L[n1], M[n2];
  for (int i = 0; i < n1; i++)
    L[i] = arr[p + i];
  for (int j = 0; j < n2; j++)
    M[j] = arr[q + 1 + j];
  int i, j, k;
  i = 0;
  j = 0;
  k = p;
  while (i < n1 && j < n2) {
    if (L[i] <= M[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = M[j];
      j++;
    }
    k++;
  }
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }
  while (j < n2) {
    arr[k] = M[j];
    j++;
    k++;
  }
}
void mergeSort(int arr[], int l, int r) {
  if (l < r) {
    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
  }
}

void quickSort(int arr[], int left, int right) {
    int i = left, j = right;
    int tmp;
    int pivot = arr[(left + right) / 2];
    while (i <= j) {
        while (arr[i] < pivot)
            i++;
        while (arr[j] > pivot)
            j--;
        if (i <= j) {
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    };
    if (left < j)
        quickSort(arr, left, j);
    if (i < right)
        quickSort(arr, i, right);
}
void swap(int a[], int *g, int *b) {
    int temp;
    temp = a[*g];
    a[*g] = a[*b];
    a[*b] = temp;
}

void maxHeapify(int a[], int parent, int last) {
    int child;
    child = 2 * parent;
    while (child <= last) {
        if ((child + 1 <= last) && (a[child + 1] > a[child]))
            child++;
        if (a[parent] < a[child])
            swap(a, &parent, &child);
        parent = child;
        child = 2 * parent;
    }
}

void buildHeap(int a[], int last) {
    int i;
    for (i = last / 2; i > 0; i--) {
        maxHeapify(a, i, last);
    }
}

void heapSort(int a[], int last) {
    int l;
    l = 1;
    buildHeap(a, last);
    while (last > 1) {
        swap(a, &l, &last);
        last--;
        maxHeapify(a, 1, last);
    }
}


void countSort(int arr[], int n, int exp) {
    int output[n];
    int i, count[10] = {0};
    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    for (i = 0; i < n; i++)
        arr[i] = output[i];
}

void BucketSort(int* data, int count) {
	int minValue = data[0];
	int maxValue = data[0];

	for (int i = 1; i < count; i++)
	{
		if (data[i] > maxValue)
			maxValue = data[i];
		if (data[i] < minValue)
			minValue = data[i];
	}

	int bucketLength = maxValue - minValue + 1;
	vector<int>* bucket = new vector<int>[bucketLength];

	for (int i = 0; i < bucketLength; i++)
	{
		bucket[i] = vector<int>();
	}

	for (int i = 0; i < count; i++)
	{
		bucket[data[i] - minValue].push_back(data[i]);
	}

	int k = 0;
	for (int i = 0; i < bucketLength; i++)
	{
		int bucketSize = bucket[i].size();

		if (bucketSize > 0)
		{
			for (int j = 0; j < bucketSize; j++)
			{
				data[k] = bucket[i][j];
				k++;
			}
		}
	}
}
void countSort1(int array[], int size) {
  int output[size];
  int count[size];
  int max = array[0];
  for (int i = 1; i < size; i++) {
    if (array[i] > max)
      max = array[i];
  }
  for (int i = 0; i <= max; ++i) {
    count[i] = 0;
  }
  for (int i = 0; i < size; i++) {
    count[array[i]]++;
  }
  for (int i = 1; i <= max; i++) {
    count[i] += count[i - 1];
  }
  for (int i = size - 1; i >= 0; i--) {
    output[count[array[i]] - 1] = array[i];
    count[array[i]]--;
  }
  for (int i = 0; i < size; i++) {
    array[i] = output[i];
  }
}



int main() {
    //Create Dummy Array!!!
    int numberData[10] = {200,400,800,1600,3200,6400,12800,25600,51200,102400};
    string method1 = "";
    string method2 = "";
    string method3 = "";
    string method4 = "";
    string method5 = "";
    string method6 = "";
    string method7 = "";
    string method8 = "";
    string method9 = "";
    for(int l=0; l<10;l++){
	    int lenData = numberData[l];

	    srand(time(NULL));
		int sirala [lenData];
	
	    for (int fila = 0; fila < lenData; fila++)
	    {
	        sirala[fila] = rand() % 101;
	
	    }

		t0=clock();
		bubbleSort(sirala,lenData);
		t1 = clock();
		 
		double time = (double(t1-t0)/CLOCKS_PER_SEC);
		cout << "Metodo: bubbleSort"<<endl;
		cout << "Tiempo de ejecucion: " << time << endl;
		cout << "Cantidad de datos: " << numberData[l]<<endl;
		method1 = method1 + "(" + to_string(numberData[l]) + "," + to_string(time) + ")";
		cout << "Vector: (" << numberData[l] << ","<< time<< ")"<<endl;
		
		
		t0=clock();
		BucketSort(sirala,lenData);
		t1 = clock();
		 
		double time1 = (double(t1-t0)/CLOCKS_PER_SEC);
		cout << "Metodo: bucketSort"<<endl;
		cout << "Tiempo de ejecucion: " << time1 << endl;
		cout << "Cantidad de datos: " << numberData[l]<<endl;
		method2 = method2 + "(" + to_string(numberData[l]) + "," + to_string(time1) + ")";
		cout << "Vector: (" << numberData[l] << ","<< time1<< ")"<<endl;
		
		
		t0=clock();
		heapSort(sirala, lenData);
		t1 = clock();
		 
		double time2 = (double(t1-t0)/CLOCKS_PER_SEC);
		cout << "Metodo: heapSort"<<endl;
		cout << "Tiempo de ejecucion: " << time2 << endl;
		cout << "Cantidad de datos: " << numberData[l]<<endl;
		method3 = method3 + "(" + to_string(numberData[l]) + "," + to_string(time2) + ")";
		cout << "Vector: (" << numberData[l] << ","<< time2<< ")"<<endl;
		
		
		t0=clock();
		insertionSort(sirala,lenData);
		t1 = clock();
		 
		double time3 = (double(t1-t0)/CLOCKS_PER_SEC);
		cout << "Metodo: insertionSort"<<endl;
		cout << "Tiempo de ejecucion: " << time3 << endl;
		cout << "Cantidad de datos: " << numberData[l]<<endl;
		method4 = method4 + "(" + to_string(numberData[l]) + "," + to_string(time3) + ")";
		cout << "Vector: (" << numberData[l] << ","<< time3<< ")"<<endl;
		
		
		t0=clock();
		quickSort(sirala, 0, lenData-1);
		t1 = clock();
		 
		double time4 = (double(t1-t0)/CLOCKS_PER_SEC);
		cout << "Metodo: quickSort"<<endl;
		cout << "Tiempo de ejecucion: " << time4 << endl;
		cout << "Cantidad de datos: " << numberData[l]<<endl;
		method5 = method5 + "(" + to_string(numberData[l]) + "," + to_string(time4) + ")";
		cout << "Vector: (" << numberData[l] << ","<< time<< ")"<<endl;
		
		
		t0=clock();
		selectionSort(sirala,lenData);
		t1 = clock();
		 
		double time5 = (double(t1-t0)/CLOCKS_PER_SEC);
		cout << "Metodo: selectionSort"<<endl;
		cout << "Tiempo de ejecucion: " << time5 << endl;
		cout << "Cantidad de datos: " << numberData[l]<<endl;
		method6 = method6 + "(" + to_string(numberData[l]) + "," + to_string(time5) + ")";
		cout << "Vector: (" << numberData[l] << ","<< time5<< ")"<<endl;
		
		
		t0=clock();
		shellSort(sirala,lenData);
		t1 = clock();
		 
		double time6 = (double(t1-t0)/CLOCKS_PER_SEC);
		cout << "Metodo: shellSort"<<endl;
		cout << "Tiempo de ejecucion: " << time6 << endl;
		cout << "Cantidad de datos: " << numberData[l]<<endl;
		method7 = method7 + "(" + to_string(numberData[l]) + "," + to_string(time6) + ")";
		cout << "Vector: (" << numberData[l] << ","<< time6<< ")"<<endl;
		
		t0=clock();
		countSort1(sirala,lenData);
		t1 = clock();
		 
		double time7 = (double(t1-t0)/CLOCKS_PER_SEC);
		cout << "Metodo: countSort"<<endl;
		cout << "Tiempo de ejecucion: " << time7 << endl;
		cout << "Cantidad de datos: " << numberData[l]<<endl;
		method8 = method8 + "(" + to_string(numberData[l]) + "," + to_string(time7) + ")";
		cout << "Vector: (" << numberData[l] << ","<< time7<< ")"<<endl;
		
		t0=clock();
		mergeSort(sirala,0,lenData-1);
		t1 = clock();
		 
		double time8 = (double(t1-t0)/CLOCKS_PER_SEC);
		cout << "Metodo: mergeSort"<<endl;
		cout << "Tiempo de ejecucion: " << time8 << endl;
		cout << "Cantidad de datos: " << numberData[l]<<endl;
		method9 = method9 + "(" + to_string(numberData[l]) + "," + to_string(time8) + ")";
		cout << "Vector: (" << numberData[l] << ","<< time8<< ")"<<endl;
		
	    //mergeSort(sirala,0,9);
	    //quickSort(sirala, 0, 9);
	    //heapSort(sirala, 10);
	    //radixSort(sirala,10);
	    cout << "___________________________________"<<endl;
	}
	cout << '1: ' << method1<< endl;
	cout << '2: ' << method2<< endl;
	cout << '3: ' << method3<< endl;
	cout << '4: ' << method4<< endl;
	cout << '5: ' << method5<< endl;
	cout << '6: ' << method6<< endl;
	cout << '7: ' << method7<< endl;
	cout << '8: ' << method8<< endl;
	cout << '9: ' << method9<< endl;
    return 0;
}

