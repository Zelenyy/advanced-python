#include <fstream>
#include <iostream>


using namespace std;

#pragma pack(push,1)
struct Foo
{
    char ch;
    int value;
};
#pragma pack(pop)

int main(int argc, char* argv[]){
    ofstream fout;
    fout.open("data_q.bin", ios_base::binary | ios_base::trunc);
    Foo foo = {1, 32000};
    for (int i = 0; i < 500; ++i){
        fout.write((char*) &foo, sizeof(foo));
    }
    fout.close();
    return 0;
}