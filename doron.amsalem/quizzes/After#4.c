void BestProfit(int *arr, int len_arr, int *buy_index, int *sell_index)
{
	int i = 0, temp_buy = 0, temp_sell = 1,
	    profit = *(arr + temp_sell) - *(arr + temp_buy);
	for (i = 2; i < len_arr - 1; i++)
	{
		if ( *(arr + i) < *(arr + temp_buy) )
		{
			temp_buy = i;
		}
		else if ( *(arr + i) - *(arr + temp_buy) > profit)
		{
			*sell_index = i;
			*buy_index = temp_buy;
			profit = *(arr + *sell_index) - *(arr + *buy_index);
		}
	}
}

#include <stdio.h>
int main()
{
	int prices[] = {2, 8, 3, 4, 6, 16, 7}, buy = 0, sell = 1;
	size_t len = sizeof(prices) / sizeof(int);
	BestProfit( prices, len , &buy, &sell);
	printf("your profit for today: %d\n buy index %d with price of %d\n sell index %d with price of %d\n", prices[sell] - prices[buy], buy, prices[buy], sell, prices[sell]); 
	return 0;
}
