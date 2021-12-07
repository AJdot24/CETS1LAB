#include <stdio.h>
#include<stdlib.h>
struct node{
int data;
struct node *next;
};
struct node *head;
void insert();
void display();
int main()
{
int a;
printf("ENter Number of values to be enter to the list :");
scanf("%d",&a);
for(int i=0;i<a;i++)
{
insert();
}
for(int i=0;i<a;i++)
{
display();
}
return 0;
}
void insert()
{

struct node *ptr;
 ptr = (struct node*) malloc(sizeof(struct node*));
if(ptr==NULL)
{
printf("\n Overflow");
}else
{
printf("Please enter the value:");
int item;
scanf("%d",&item);
ptr->data=item;
ptr->next=NULL;
head=ptr;

}
}
void display()
{
struct node *ptr;
ptr = head;   
    if(ptr == NULL)  
    {  
        printf("Nothing to print");  
    }  
    else  
    {     
        while (ptr!=NULL)  
        {  
            printf("\n%d\n",ptr->data);  
            ptr = ptr -> next;  
        }  
}
}
