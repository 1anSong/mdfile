##运用dbscan算法分析水团簇的大小
import numpy as np
import time
import copy


def clau_distance(p1,p2,eps):
    distance=np.sqrt(np.sum(np.power(p1-p2,2)))
    if distance <= eps:
        return True 
    else:
        return False

def find_center_and_neigh(data,eps,minpts): #data:数据 eps:邻域半径 minpts:最小对象点数目
    data_num=np.shape(data)[0] #数据点数目
    cluster=[]
    for i in range(data_num):
        tempCluster=[]
        for j in range(data_num):
            if (i!=j and clau_distance(data[i,:],data[j,:],eps)):
                if i not in tempCluster:
                    tempCluster.append(i)
                tempCluster.append(j)

        tempCluster=np.array(tempCluster)
        if len(tempCluster)>=minpts:
            cluster.append(tempCluster)
    return cluster
 
def find_corepoints(fun1):
    corepoints=[]
    for i in  fun1:
        corepoints.append(i[0])
    return corepoints 

def find_clusterGroup(tempcluster,centers):
    corepts_num=len(centers)
    group=[]
    len_group=[]
    position=np.ones(corepts_num)
    unvisited=[]
    unvisited.extend(centers)
    for i in range(corepts_num):
        coreNeihbor=[]
        result=[]
        if position[i]:
            coreNeihbor.extend(list(tempcluster[i]))
            position[i]=0
            temp=coreNeihbor

            while (len(coreNeihbor)) > 0:
                present=coreNeihbor[0]
                for j in range(len(position)):
                    if position[j]==1:
                        if (present in tempcluster[j]):
                            #temp=set(temp)|set(tempcluster[j])
                            #temp=list(temp)
                            #coreNeihbor=temp
                            cluster=tempcluster[j].tolist()
                            diff=[]
                            for x in cluster:
                                if x not in temp:
                                    diff.append(x)
                            temp.extend(diff)
                            position[j]=0
                result.extend(temp)
                del coreNeihbor[0]
            group.append(list(set(result)))
            len_group.append(len(set(result)))
        i+=1
    print(len_group)
    return group

#X=np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9],[8,2]])
def trj():
    O_atoms=np.empty(shape=(2304,3))
    k=0
    with open('1.pdb') as trj:
        for atoms in trj:
            if ' O ' in atoms:
                x,y,z=atoms.split()[-5],atoms.split()[-4],atoms.split()[-3]#O原子坐标
                O_atoms[k]=[x,y,z]
                k+=1
    return O_atoms
#print(O_atoms)
cluster=find_center_and_neigh(trj(),3.5,6)

corepts=find_corepoints(cluster)

find_clusterGroup(cluster,corepts)
