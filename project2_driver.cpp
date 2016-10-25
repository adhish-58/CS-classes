#include <iostream>
#include <time.h>
#include "agenda.h"
#include "treeNode.h"

using namespace std;
using namespace cs310;


template <class Object, class Agenda>
void traverse(const treeNode<Object> *root)
{
  Agenda agenda;
  
  if (root != NULL)
    {
      treeNode<Object> *current_node = root;
      agenda.put(current_node);
      
      while (!agenda.empty())
        {      
          current_node = agenda.get();
          if (current_node.left != NULL)
            {
              agenda.put(current_node->leftchild());
              agenda.put(current_node->rightchild());
            }
        }
    }
}


template <class Object>
void printTree(const treeNode<Object> *root, const string depth = "")
{
  if(root != NULL)
    {
      cout<<depth<<root->retrieve()<<endl;
      printTree(root->leftchild(),depth+"");
      printTree(root->righttchild(),depth+"");
    }
}


int main()
{
  int height;
  
  cout << "Enter the height of the tree: " << endl;
  cin >> height;
  
  treeNode<int> theTree = buildTree(height, 0);
  
  traverse<int,ustack<treeNode<int>*>>(theTree);
  printTree<int>(*root);
  
  traverse<int,uqueue<treeNode<int>*>>(theTree);
}
