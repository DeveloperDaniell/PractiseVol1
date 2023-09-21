#include <cstdio>

int main(int argc, char** argv)
{
	for (int i = 0; i <= 98; i++)
		for (int j = i + 1; j <= 99; j++)
			printf("%02d %02d%c", i, j, i != 98 ? ',': ' ');
}
