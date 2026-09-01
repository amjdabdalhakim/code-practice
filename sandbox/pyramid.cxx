#include <iostream.h>
#include <conio.h>
void main()
{
	clrscr();
	int i, j;
	for (i = 0; i < 10 ;i++)
	{
		cout << endl;
		for (j = 20; j >= 0; j--)
		{
			if (j > 10 + i || j < 10 - i)
				cout << " ";
			else
				cout << "^";
		}
	}
	getch();
}