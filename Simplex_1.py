def SIMPLEXM(tbl):
  x=[]
  p=[]
  for i in range(1, len(tbl)):
    if tbl[i][len(tbl[i])-1]!=0:
      if tbl[i][tbl[0].index(min(tbl[0][1:len(tbl[0])-1]))]>0:
        x.append(tbl[i][tbl[0].index(min(tbl[0][1:len(tbl[0])-1]))]/tbl[i][len(tbl[i])-1])
      else:
        x.append(0)
    else:
      x.append(0)
  d=tbl[x.index(max(x))+1][tbl[0].index(min(tbl[0][1:len(tbl[0])-2]))]
  for u in range(len(tbl[0])):
    tbl[x.index(max(x))+1][u]=tbl[x.index(max(x))+1][u]/d
  for j in range(len(tbl)):
    p.append(tbl[j][tbl[0].index(min(tbl[0][1:len(tbl[0])-2]))])
  for i in range(len(tbl)):
    for j in range(len(tbl[0])):
      if (x.index(max(x))+1)==i:
        pass
      else:
        tbl[i][j]= tbl[i][j]-(p[i]*tbl[x.index(max(x))+1][j])
  return tbl
n = int(input("Ingrese el número de variables: "))
m = int(input("Ingrese el número de restricciones: "))
def tablaM(n,m):
  fo=[]
  r0=[]
  ab=[]
  rw=[]
  gg=('<=','>=','=')
  for i in range(int(n)):
    fo.append(-float(input("Ingrese el valor del coeficiente x{} : ".format(i+1))))
  # coeficientes de restricciones
  for i in range(int(m)):
    r0.append([])
    for j in range(int(n)):
      r0[i].append(float(input("ingrese el valor del coeficiente de x{} para la restricción {}: ".format(j+1,i+1))))
  for k in range(int(m)):
    ab.append(int(input("ingrese los valores del lado derecho de la restricción {}: ".format(k+1))))
  U=(10**len(str(min(ab))))**(10**len(str(min(ab))))
  an=[0.]+list(map(float,ab))
  for gg in gg:
    rw.append(int(input('Restricciones {}: '.format(gg))))
  if rw[0]!=0:
    for i in range(rw[0]):
      fo.append(0.)
      for j in range(rw[0]):
        if i==j:
          r0[j].append(1.)
        else:
          r0[j].append(0.)
    for h in range(rw[0],len(r0)):
      for g in range(rw[0]):
        r0[h].append(0.)
  if rw[1]!=0:
    for i in range(rw[1]):
      for j in range(rw[1]):
        if i==j:
          r0[rw[0]+i].append(-1.)
          r0[rw[0]+i].append(1.)
          fo.append(0.)
          fo.append(U)
        else:
          r0[rw[0]+i].append(0.)
          r0[rw[0]+i].append(0.)
    for h in range(rw[1]+rw[0],len(r0)):
      for g in range(2*rw[1]):
        r0[h].append(0.)
    for f in range(rw[0]):
      for l in range(2*rw[1]):
        r0[f].append(0.)
  if rw[2]!=0:
    for i in range(rw[2]):
      for j in range(rw[2]):
        if i==j:
          r0[rw[0]+rw[1]+j].append(1.)
          fo.append(U)
        else:
          r0[rw[0]+rw[1]+j].append(0.)
          fo.append(0.)
    for f in range(rw[0]+rw[1]):
      for l in range(rw[2]):
        r0[f].append(0.)
  tbl=[fo]+r0
  for i in range(len(tbl)):
    tbl[i].append(an[i])
  if rw[0]>0 and rw[1]==0 and rw[2]==0:
    pass
  else:
    for j in range(rw[1]+rw[0],rw[1]+rw[2]+rw[0]+1):
      for l in range(len(tbl[0])):
        tbl[0][l]=tbl[0][l]-(U*tbl[j][l])
  for i in range(len(tbl)):
    if i ==0:
      tbl[i].insert(0,1.)
    else:
      tbl[i].insert(0,0.)
  return tbl
tbl=tablaM(n,m)
while min(tbl[0][0:len(tbl[0])-1])<0:
  tbl=SIMPLEXM(tbl)
print('z:',round(tbl[0][len(tbl[0])-1]))
for i in tbl[1:]:
  for j in range(1,3):
    if i[j]==1 and tbl[0][j]==0:
      print('x{}:'.format(j),i[len(i)-1])
    else:
      pass
