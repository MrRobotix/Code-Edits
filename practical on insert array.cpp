#include<stdio.h>
int main()

{
	printf("Jadhav Yashodip,Roll no.29.....................");
int arr[50],i,n,value,pos;
printf("Enter the no of elements: ");
scanf("%d",&n);
printf("Enter %d elements: ",n);
for(i=0;i<n;i++)
{
scanf("%d",&arr[i]);
}
printf("Enter the insert value: ");
scanf("%d",&value);
printf("Enter the insert position: ");
scanf("%d",&pos);
if(pos<1 || pos>n+1)
{
printf("Insert is not possible!!!");
}
else
{
for(i=n-1;i>=pos-1;i--)
{
arr[i+1]=arr[i];
}
arr[pos-1]=value;
printf("Before insert Array is: ");
for(i=0;i<n;i++)
{
printf("%d ",arr[i]);
}
printf("\n");
printf("After insert Array is: ");
for(i=0;i<=n;i++)
{
printf("%d ",arr[i]);
}
}
return 0;
}
