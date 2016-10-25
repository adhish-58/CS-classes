#include<iostream>
#include<iomanip>
#include<cstdlib>    // exit() and EXIT_SUCCESS

using namespace std;

int month(int current_month, int& initial_day);
int month_days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int month_days_leap[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const char* month_names[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

int main()
{  
  int initial_day = 0, current_month, date, year;
  
  cout << "Enter the year you want to find the calender of." << endl;
  
  cin >> year;
 
  for (int x = 0; x <= 12; x++)
    {    
      cout << endl << month_names[x] << endl;
      
      if((year/4) == 0)
        {
          while (date <= month_days_leap[x])
            {
              current_month = month_days_leap[x];
            }
        }

        else
          {
            while (date <= month_days_leap[x])
              { 
                current_month = month_days_leap[x];
              }
          }
      
      date = month(current_month, initial_day);
    }
  date = 1;

exit(EXIT_SUCCESS);
}

int month(int current_month, int& initial_day)
{
  int initial_date = 1, day, date, for_set, count = 0;
  const char names[] = "SMTWTFS";
  
  day = initial_day;
  date = initial_date;
      
  if ((initial_day >= 0) && (initial_day <= 6))
    {
      for (int x = 0; x < 8; x++)
        {
          cout << setw(2) << right << names[x] << " ";
        }
          
      cout << endl;
          
      for_set = day * 3;
      
      if (initial_day != 0)
        {
          cout << setw(for_set) << right << " ";
        }
          
      while (date <= current_month)
        { 
          date = initial_date + count;
          day++;
          count++;
              
          cout << setw(2) << right << date << " ";
              
          date ++;
              
          day = day % 7;
              
          if ((day == 0))            
            {
              cout << endl;
            }
        }
    }

  cout << endl;

  initial_day = day;
  
  return(date);
}
  
 
