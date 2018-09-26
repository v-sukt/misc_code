#include <stdio.h>

/*This is a comment*/
int main(int argc, char *argv[])
{
    int distance = 590;
    int width = 5;
    //char *city = "Vividhan";
    char city[8] = "Vividhan";

    //This is also a comment
    printf("There's an ancient city named %s\n", city);
    //The first argument if %* used is the width
    printf("Which is Exactly %*dkm away\n", width, distance);
    printf("As you are here, Your are %d km away.\n", distance);
    return 0;
}
