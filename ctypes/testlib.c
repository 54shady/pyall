#include <stdio.h>
#include <string.h>

struct Point {
    int x;
    int y;
};

struct Rect {
    struct Point upperleft;
    struct Point lowerright;
};

/* gcc -fPIC -shared -o testlib.so testlib.c */

static int g_value = 0;
char g_string[10] = "Cstring";
struct Point point = {
	.x = 911,
	.y = 811
};

void vv_func(void)
{
	printf("%s, %d\n", __FUNCTION__, __LINE__);
}

void set_value(int value)
{
	g_value = value;
}

int get_value(void)
{
	return g_value;
}

void get_value2(int *value)
{
	*value = g_value;
}

char *get_string(void)
{
	return g_string;
}

void get_string2(char *str)
{
	strncpy(str, g_string, 9);
	str[9] = '\0';
}

void set_string(char *str)
{
	strncpy(g_string, str, 9);
	g_string[9] = '\0';
}

void set_string2(char *str, char c)
{
	strncpy(g_string, str, 9);
	g_string[0] = c;
	g_string[9] = '\0';
}

/*
 * 输入参数p1, p2
 * 输出参数p3
 */
void set_struct(struct Point p1, struct Point *p2, struct Point *p3)
{
	printf(">>> x = %d, y = %d\n", p1.x, p1.y);
	printf(">>> x = %d, y = %d\n", p2->x, p2->y);
	p3->x = point.x;
	p3->y = point.y;
}

void null_func(char *str)
{
	if (NULL == str)
		printf("str is null\n");
	else
		printf("str is %s\n", str);
}

int test_callback(int a, int(*call_back)(int))
{
	int ret;
	ret = call_back(a);
	return ret;
}
