#include<stdio.h>
#include<stdlib.h>
int main()
{
int queue[100],ch=1,front=0,rear=0,i=1,j=1,n;
printf("Enter Size of queue:");
scanf("%d",&n);
int x=n;
printf("queue using an array");
printf("\n1.insertion\n2.deletion\n3.display\n4.exit\n");

while(1)
{
printf("\n enter the choice:");
scanf("%d",&ch);
switch(ch)
{
case 1:
if(rear==x)
printf("\n queue is full");
else if(front==rear)
{ 
printf("\n enter number :");
scanf("%d",&queue[rear]);
rear++;
}
else{
printf("\n enter number :");
scanf("%d",&queue[rear]);
rear++;
}
break;
case 2:
if(front==rear)
{
printf("\n queue is empty");
}
else
{
printf("\n deleted element is %d",queue[front++]);
x++;
}
break;
case 3:
printf("\n queue elements are:\n");
if(front==rear)
printf("\n queue is empty");
else
{
for(i=front;i<rear;i++)
{
printf("%d",queue[i]);
printf("\n");
}
break;
case 4:
exit(0);
default:
printf("wrong");  
}
}
}
return(0); 
}

