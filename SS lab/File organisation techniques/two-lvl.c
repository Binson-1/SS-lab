#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

struct node
{
    char name[128];
    bool isDir;
    struct node *p;
    struct node *c[100];
    int i;
    int level;
} * head, *curr;

void contents()
{
    if (curr->i == 0)
    {
        printf("Directory Empty\n");
        return;
    }
    for (int i = 0; i < curr->i; i++)
    {
        if (curr->c[i]->isDir)
            printf("*%s*  ", curr->c[i]->name);
        else
            printf("%s  ", curr->c[i]->name);
    }
}

void create(bool d)
{
    if (d && curr->level >= 1)
    {
        printf("More than two levels of directories is not allowed\n");
        return;
    }
    if (d)
        printf("Enter directory name\n");
    else
        printf("Enter filename\n");
    char fname[128];
    scanf("%s", fname);
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    strcpy(temp->name, fname);
    temp->isDir = d;
    temp->p = curr;
    temp->level = (curr->level) + 1;
    curr->c[curr->i] = temp;
    curr->i = (curr->i) + 1;
}

void change()
{
    printf("Enter directory name\n");
    char dname[128];
    scanf("%s", dname);
    for (int i = 0; i < curr->i; i++)
    {
        if (!strcmp(curr->c[i]->name, dname) && curr->c[i]->isDir == true)
        {
            curr = curr->c[i];
            return;
        }
    }
    printf("Directory Not Found\n");
}

void parent()
{
    if (curr->p == NULL)
    {
        printf("You are at the root directory\n");
        return;
    }
    curr = curr->p;
}

void del(bool d)
{
    printf("Enter Name of File or Directory to be Deleted:\n");
    char name[128];
    scanf("%s", name);
    for (int i = 0; i < curr->i; i++)
    {
        if (!strcmp(curr->c[i]->name, name) && ((d && curr->c[i]->isDir == true) || (!d && curr->c[i]->isDir == false)))
        {
            int t = i;
            while (t < (curr->i) - 1)
            {
                curr->c[t] = curr->c[t + 1];
                t++;
            }
            curr->i = (curr->i) - 1;
            printf("Deletion Successful\n");
            return;
        }
    }
    printf("No file/directory found\n");
}

void main()
{
    int in;
    head = (struct node *)malloc(sizeof(struct node));
    strcpy(head->name, "root");
    head->isDir = true;
    head->p = NULL;
    head->i = 0;
    head->level = 0;
    curr = head;
    while (true)
    {
        printf("Current Directory:%s\n1.Directory Contents 2.Change Directory 3.Go to Parent Directory 4.Create New File 5.Delete a File 6.Create a New Directory 7.Delete a Directory 8.Exit\nEnter an option:", curr->name);
        scanf("%d", &in);
        switch (in)
        {
        case 1:
            contents();
            break;
        case 2:
            change();
            break;
        case 3:
            parent();
            break;
        case 4:
            create(false);
            break;
        case 5:
            del(false);
            break;
        case 6:
            create(true);
            break;
        case 7:
            del(true);
            break;
        default:
            exit(0);
        }
    }
}
