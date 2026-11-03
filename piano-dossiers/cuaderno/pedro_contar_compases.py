# -*- coding: utf-8 -*-
"""Cuenta los compases de cada sistema sobre el PDF (render + barras de compas que cruzan TODO el sistema).
   Uso: python3 pedro_contar_compases.py <pdf> <pentagramas por sistema>. Se ha contrastado a mano con la numeracion
   impresa de cada edicion: las anacrusas y las barras espurias (plicas largas, reguladores) obligan a revisar el resultado."""
import sys, numpy as np, pymupdf
def staves(a):
    h,w=a.shape; dark=a<150
    frac=dark.sum(axis=1)/float(w)
    thr=0.5*frac.max()
    rows=np.where(frac>thr)[0]
    lines=[]
    for r in rows:
        if lines and r-lines[-1][-1]<=1: lines[-1].append(r)
        else: lines.append([r])
    c=[float(np.mean(l)) for l in lines]
    st=[];i=0
    while i+4<len(c):
        g=c[i:i+5]; d=np.diff(g)
        if d.max()-d.min()<=max(1.6,0.12*d.mean()) and d.mean()>5: st.append(g); i+=5
        else: i+=1
    return st,dark
def medir(pdf,dpi=200,k=2):
    d=pymupdf.open(pdf); res=[]
    for pi,p in enumerate(d):
        pm=p.get_pixmap(dpi=dpi,colorspace=pymupdf.csGRAY)
        a=np.frombuffer(pm.samples,dtype=np.uint8).reshape(pm.height,pm.width)
        st,dark=staves(a)
        # emparejar por distancia: pares (sol,fa) si la distancia entre staves < 6*sp
        for j in range(0,len(st),k):
            grupo=st[j:j+k]
            g=grupo[0]; sp=(g[4]-g[0])/4
            ys=[]
            for s in grupo:
                ys+= [(s[k]+s[k+1])/2 for k in range(4)]
            ys=[int(round(y)) for y in ys]
            # extension horizontal
            row=dark[int(round(grupo[0][0])),:]; xs=np.where(row)[0]
            x0,x1=xs.min(),xs.max()
            col=np.ones(x1-x0+1,bool)
            for y in ys: col&=dark[y,x0:x1+1]
            idx=np.where(col)[0]+x0
            cl=[]
            for x in idx:
                if cl and x-cl[-1][-1]<=max(4,int(1.0*sp)): cl[-1].append(x)
                else: cl.append([x])
            cx=[(c[0]+c[-1])/2 for c in cl]
            res.append(dict(pag=pi+1,x0=int(x0),x1=int(x1),sp=sp,n=len(grupo),barras=cx))
    return res
if __name__=='__main__':
    tot=0
    k=int(sys.argv[2]) if len(sys.argv)>2 else 2
    for r in medir(sys.argv[1],k=k):
        b=[x for x in r['barras'] if x>r['x0']+6.5*r['sp'] and x<r['x1']-1.5*r['sp']]
        fin=r['barras'] and abs(r['barras'][-1]-r['x1'])<2.5*r['sp']
        print('p%d pent=%d compases=%d final=%s'%(r['pag'],r['n'],len(b)+1,bool(fin)))
