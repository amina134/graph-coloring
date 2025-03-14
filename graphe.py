class graphe:
     def __init__(self,n):
          self.n=n
          self.mat= [[0 for _ in range(n)] for _ in range(n)]
          self.tab_couleur=['R','G','B']
          self.tab_res=[0 for _ in range(n)]

        
     def fill_mat(self):
        print(f"enter {self.n}*{self.n}elements for the matrix:")
        for i in range(self.n):
            for j in range(self.n):
                self.mat[i][j]=int(input(f"Element[{i}][{j}]:"))

     def print_mat(self):
        print("Matrix:")
        for row in self.mat:
            print(' '.join(map(str, row))) 
    
     def travail(self):
         test=True
         self.tab_res[0]=self.tab_couleur[0]
         
         for i in range (1,len(self.tab_res)):
             j=0
             self.tab_res[i]=self.tab_couleur[j]
             for e in range(i,i+1):
                 for k in range(i+1):
                      
                     if self.mat[e][k]==1 and self.tab_res[k]==self.tab_res[i] :
                             if  j<len(self.tab_couleur)-1:
                               j=j+1
                               self.tab_res[i]=self.tab_couleur[j]

                             else :
                                 test=False
                                 print("impossible")

        
         if(test):  
          return self.tab_res
         else:
           print('impossible de colorer')
                            


   
                             
                         
                 
             
             
             
         
     

     






n = 4
obj = graphe(n)
obj.fill_mat()
obj.print_mat()
result=obj.travail()
print("result is ",result)