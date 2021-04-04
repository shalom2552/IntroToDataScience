#include <iostream>

using namespace std;

int main()
{
    
double sum = 0.0;
double temp = 0.0;
double count = 0.0;

cout<<"Enter real numbers (between 0.0 and 1000.0) separated by a space, when your done write char"<<endl;

while (cin >> temp) {
   if (temp == '\n') break;
   if ((temp > 1000.0) || (temp < 0.0)){
       cerr << "The numbers should be between 0.0 and 1000.0" <<endl;
       return 0;
   } 
   sum += temp;
   count += 1.0;
}

if (count != 0.0){
    cout<<"The sum of numbers:" <<sum<<endl;
    cout<<"The avarege of numbers:" <<(sum/count)<<endl;
} 
else{
    cerr << "wHERE IS YOUR INPUT??" <<endl;
}

}

