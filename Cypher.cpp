#include<bits/stdc++.h>
using namespace std;
string alp="abcdefghijklmnopqrstuvwxyz";
void make_matrix(string* mat){
    for(int i=0;i<26;i++){
        mat[i]=alp.substr(alp.length()-i,alp.length())+alp.substr(0,alp.length()-i);
    }
    //for(int i=0;i<26;i++){
    //    cout<<mat[i]<<endl;
    //}
}

void encrypt_mssg(string key, string mssg, string* mat){
    string encrypt="";
    for(int i=0;i<mssg.length();i++){
        if(mssg[i]>96 && mssg[i]<=122){
            int a=0,b=0;
            for(int j=0;j<26;j++){
                if(mat[j][0]==key[i%key.length()]){
                    a=j;
                }
                if(mat[0][j]==mssg[i]){
                    b=j;
                }
            }
            encrypt+=mat[a][b];
        } else {
            encrypt+=mssg[i];
        }
    }
    cout<<encrypt<<endl;
}
void decrypt_mssg(string key, string* mat){
    string mssg;
    cout<<"Enter encrypted message: ";
    cin.ignore();
    getline(cin,mssg);
    string decrypt="";
    for(int i=0;i<mssg.length();i++){
        if(mssg[i]>96 && mssg[i]<=122){
            int a=0,b=0;
            for(int j=0;j<26;j++){
                if(mat[j][0]==key[i%key.length()]){
                    a=j;
                    for(int k=0;k<26;k++){
                        if(mat[a][k]==mssg[i]){
                            b=k;
                        }
                    }
                }
            }
            decrypt+=mat[0][b];
        } else {
            decrypt+=mssg[i];
        }
    }
    cout<<decrypt<<endl;
}
int main(){
    string matrix[26];
    make_matrix(matrix);
    string key="a";
    string mssg="hello";
    cout<<"------Substitution Cipher-------"<<endl;
    int choice=0;
    while(true){
        cout<<"1)New message"<<endl;
        cout<<"2)New key"<<endl;
        cout<<"3)View Message"<<endl;
        cout<<"4)Get decrypted message"<<endl;
        cout<<"5)Exit"<<endl;
        cout<<"Enter choice:";
        cin>>choice;
        cout<<endl;
        switch(choice){
            case 1:
                cout<<"Enter message:";
                cin.ignore();
                getline(cin,mssg);
                break;
            case 2:
                cout<<"Enter key:";
                cin.ignore();
                getline(cin,key);
                break;
            case 3:
                encrypt_mssg(key,mssg,matrix);
                break;
            case 4:
                decrypt_mssg(key,matrix);
                break;
            case 5:
                exit(0);
            default:
                cout<<"Invalid choice"<<endl;
        }
        cout<<endl;
    }
}