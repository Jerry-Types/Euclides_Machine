#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sin título.py
#       
#       Copyright 2012 Manuel <manuel@Manuel>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#
from math import sqrt
tam=[300,30]

stxlistapuntos=[]
stxlistalineas=[]
stxlistacirculos=[]
codigo=[]
listanuevapuntos=[]
listacirculos=[]
listacirculosetiquetados=[]
listalineas=[]
listadelineasetiquetadas=[]
listaetiquetas=[]

def checasintaxis(linea):
    global stxlistapuntos,stxlistalineas,stxlistacirculos
    cad=list(linea)
    puntos=[]
    i=0
    error=0
    salto=0
    retro=""
    try:
        ind=cad.index('%')
        salto=1
    except:
        salto=0
        
    if salto==0:
        if cad[i]=='P':
            i+=1
            if cad[i]=='(':
                if cad[-1]==')':
                    aux=linea[2:-1]
                    pts=aux.split(',')
                    for pt in pts:
                        if ((ord(pt[0])>=65 and ord(pt[0])<=90) or (ord(pt[0])>=97 and ord(pt[0])<=122)):
                            puntos.append(pt)
                        else:
                            retro+=", El nombre del punto deve siempre empezar con una letra"
                            error+=1
                    npts=[]+puntos
                    while len(npts)!=0:
                        aux=npts.pop(0)
                        if ((aux in stxlistapuntos) or (aux in stxlistalineas) or (aux in stxlistacirculos)):
                            error+=1
                            retro+=", El punto ya existe"
                    if error == 0:
                        stxlistapuntos+=puntos
                else:
                    error+=1
            else:
                error+=1
        elif cad[i]=='C':
            i+=1
            if cad[i]=='(':
                if cad[-1]==')':
                    aux=linea[2:-1]
                    pts=aux.split(',')
                    if len(pts)==2:
                        while len(pts)!=0:
                            punto=pts.pop(0)
                            if punto not in stxlistapuntos:
                                retro+=", Punto indefinido"
                                error+=1
                    else:
                        error+=1
                else:
                    error+=1
            else:
                error+=1
        elif cad[i]=='L':
            i+=1
            if cad[i]=='C':
                i+=1
                if cad[i]=='(':
                    if cad[-1]==')':
                        aux=linea[3:-1]
                        arg=aux.split(';')
                        if len(arg)==2:
                            ptcir=arg[0]
                            etiqueta=arg[1]
                            pts=ptcir.split(',')
                            if len(pts)==2:
                                correcto=1
                                while len(pts)!=0:
                                    punto=pts.pop(0)
                                    if punto not in stxlistapuntos:
                                        error+=1
                                        correcto=0
                                        retro+=", Punto indefinido"
                                if correcto==1:
                                    if ((etiqueta not in stxlistacirculos) and (etiqueta not in stxlistalineas) and (etiqueta not in stxlistapuntos)):
                                        stxlistacirculos.append(etiqueta)
                                    else:
                                        retro+=", Etiqueta repetida"
                                        error+=1
                            else:
                                error+=1
                        else:
                            error+=1
                    else:
                        error+=1
                else:
                    error+=1
            elif cad[i]=='L':
                i+=1
                if cad[i]=='(':
                    if cad[-1]==')':
                        aux=linea[3:-1]
                        arg=aux.split(';')
                        if len(arg)==2:
                            ptlin=arg[0]
                            etiqueta=arg[1]
                            pts=ptlin.split(',')
                            if len(pts)==2:
                                correcto=1
                                while len(pts)!=0:
                                    punto=pts.pop(0)
                                    if punto not in stxlistapuntos:
                                        retro+=", Punto indefinido"
                                        error+=1
                                        correcto=0
                                if correcto==1:
                                    if ((etiqueta not in stxlistacirculos) and (etiqueta not in stxlistalineas) and (etiqueta not in stxlistapuntos)):
                                        stxlistalineas.append(etiqueta)
                                    else:
                                        retro+=", Etiqueta repetida"
                                        error+=1
                            else:
                                error+=1
                    else:
                        error+=1
                else:
                    error+=1
            elif cad[i]=='P':
                i+=1
                if cad[i]=='(':
                    if cad[-1]==')':
                        aux=linea[3:-1]
                        arg=aux.split(';')
                        if len(arg)==2:
                            objetos=arg[0]
                            argpuntos=arg[1]
                            obj=objetos.split(',')
                            if len(obj)==2:
                                if obj[0]!=obj[1]:
                                    correcto=1
                                    while len(obj)!=0:
                                        cosa=obj.pop(0)
                                        if ((cosa not in stxlistacirculos) and (cosa not in stxlistalineas)):
                                            retro+=", Objeto no definido"
                                            error+=1
                                            correcto=0
                                    if correcto==1:
                                        ltpts=argpuntos.split(',')
                                        if len(ltpts)==1:
                                            if ((ltpts[0] not in stxlistacirculos) and (ltpts[0] not in stxlistalineas) and (ltpts[0] not in stxlistapuntos)):
                                                nvopt=ltpts[0]
                                                if ((ord(nvopt[0])>=65 and ord(nvopt[0])<=90) or (ord(nvopt[0])>=97 and ord(nvopt[0])<=122)):
                                                    stxlistapuntos.append(nvopt)
                                                else:
                                                    retro+=", El nombre del punto deve siempre empezar con una letra"
                                                    error+=1
                                            else:
                                                retro+=", El nombre del punto a asignar ya existe y no debe repetirse"
                                                error+=1
                                        elif len(ltpts)==2:
                                            auxpts=[]
                                            bien=1
                                            if ((ltpts[0] in stxlistapuntos) or (ltpts[1] in stxlistapuntos) and (ltpts[0] in stxlistacirculos) or (ltpts[1] in stxlistacirculos) and (ltpts[0] in stxlistalineas) or (ltpts[1] in stxlistalineas)):
                                                bien=0
                                            if bien==1:
                                                for pt in ltpts:
                                                    if ((ord(pt[0])>=65 and ord(pt[0])<=90) or (ord(pt[0])>=97 and ord(pt[0])<=122)):
                                                        auxpts.append(pt)
                                                    else:
                                                        retro+=", El nombre del punto deve siempre empezar con una letra"
                                                        error+=1
                                                if len(auxpts)==2:
                                                    stxlistapuntos+=auxpts
                                            else:
                                                error+=1
                                                retro+=", El nombre del punto a asignar ya existe y no debe repetirse"
                                        else:
                                            error+=1
                                    else:
                                        error+=1
                                else:
                                    retro+=", Los objetos deben ser diferentes"
                                    error+=1   
                            else:
                                error+=1
                    else:
                        error+=1
                else:
                    error+=1
            elif cad[i]=='(':
                if cad[-1]==')':
                    aux=linea[2:-1]
                    pts=aux.split(',')
                    if len(pts)==2:
                        while len(pts)!=0:
                            punto=pts.pop(0)
                            if punto not in stxlistapuntos:
                                error+=1
                    else:
                        error+=1
            else:
                error+=1
        elif cad[i]=='D':
            i+=1
            if cad[i]=='(':
                if cad[-1]==')':
                    aux=linea[2:-1]
                    if aux in stxlistapuntos:
                        stxlistapuntos.remove(aux)
                    elif aux in stxlistacirculos:
                        stxlistacirculos.remove(aux)
                    elif aux in stxlistalineas:
                        stxlistalineas.remove(aux)
                    else:
                        retro+=", Etiqueta indefinida"
                        error+=1
        else:
            error+=1 
    else:
        indpt=cad.index('%')
        indcir=cad.index(':')
        ult=len(linea)
        auxpt=linea[0:indpt-1]
        auxcir=linea[indpt+2:indcir-1]
        bien=1
        try:
            auxnum=int(linea[indcir+2:ult])
        except:
            bien=0
        if bien==1:
            if auxpt in stxlistapuntos:
                if auxcir in stxlistacirculos:
                    if auxnum<=0:
                        error+=1
                else:
                    retro+=", Círculo indefinido"
                    error+=1
            else:
                retro+=", Punto indefinido"
                error+=1
        else:
            retro+=", Numero de linea de salto no válido"
            error+=1
    return error,retro

def leerarchivo():
    nombre = raw_input("Cual es el nombre de tu euclid code ")
    f=open(nombre,'r')    
    for line in f:
        codigo.append(line.strip('\n'))
    linea=1
    a=0
    for ln in codigo:        
        if checasintaxis(ln)[0]!=0:                   
            print ("Hay un error en la linea %d: "+"%s"+"%s")%(linea,ln,checasintaxis(ln)[1])
            a=1        
        linea+=1
    if a==1:
        return False
    else:        
        return True

def maxventana():    
    import os
    os.system("xrandr  | grep \* | cut -d' ' -f4 >resolution.txt")
    f = open('resolution.txt', 'r')
    a=f.readline()
    cad=a.split('x')
    return cad    

w=0
if leerarchivo():
    maxwin=maxventana()
    import turtle
    a=turtle
    a.mode("logo")
    a.shape("turtle")
    a.title("Simulador de la maquina de Euclides!")
    a.speed(1)        
    a.setup(int(maxwin[0]),int(maxwin[1]))
    
else:
    w=1
    exit

def puntosaleatorios(eti):
    import random
    k1=int((int(maxwin[0])/2)*.20)
    k2=int((int(maxwin[1])/2)*.20)   
    x=random.randint(-k1,k1)
    y=random.randint(-k2,k2)
    
    lista=[x,y,eti]    
    listanuevapuntos.append(lista)
    a.up()
    a.setx(x)
    a.sety(y)
    a.down()
    a.dot("blue")
    a.write(eti)
    #pts=[[random.randint(-k1,k1),random.randint(-k2,k2),str(i)] for i in listanuevapuntos]    

def pintapunt(lis):    
    for i in lis:
        a.up()
        a.setx(i[0])
        a.sety(i[1])
        a.down()
        a.dot("blue")
        a.write(str(i[2]))
    
def linea1(p1,p2):           
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    a.up()
    a.setx(x1)
    a.sety(y1)
    t=a.towards(x2,y2)
    d=a.distance(x2,y2)
    a.down()
    a.rt(t)
    a.fd(d)
    if y1==y2:        
        if x2>0:            
            a.fd(int(maxwin[0])/2-x2)
            a.bk(int(maxwin[0])/2-x2)
            a.bk(d+int(maxwin[0])/2-x1)
        else:            
            a.fd(int(maxwin[0])/2+x2)
            a.bk(int(maxwin[0])/2+x2)            
            a.bk(int(maxwin[0])/2-x1+d)            
    elif x1==x2:
        if y2>0:
            a.fd(int(maxwin[1])/2-y2)
            a.bk(int(maxwin[1])/2-y2)
            a.bk(d+int(maxwin[0])/2-y1)
        else:            
            a.fd(int(maxwin[1])/2+y2)
            a.bk(int(maxwin[1])/2+y2)            
            a.bk(int(maxwin[1])/2-y1+d)
    else:
        a.fd(int(maxwin[0])/2)
        a.bk(int(maxwin[0])/2+d+int(maxwin[0])/2)    
    a.setheading(0)
    
def circulo(cc,rc):    
    x1=cc[0]
    y1=cc[1]
    x2=rc[0]
    y2=rc[1]
    a.up()
    a.setx(x1)
    a.sety(y1)    
    r=a.distance(x2,y2)
    t=a.towards(x2,y2)
    a.setx(x2)
    a.sety(y2)
    t=a.towards(x1,y1)
    a.rt(t+90)       
    a.down()
    a.circle(r)
    a.setheading(0)
    
def cuadratica(a,b,c):
    qw=[]
    disc=(b**2)+(-4*a*c)
    if disc>0:
        x1=(-1.0*b+sqrt(disc))/(2.0*a)
        x2=(-1.0*b-sqrt(disc))/(2.0*a)
        qw.append(x1)
        qw.append(x2)
        return qw
    if disc==0:
        x=(-1.0*b)/(2.0*a)
        qw.append(x)
        return qw
    if disc<0:
        return qw

def IntersectPoints(P0, P1, r0, r1):
    if type(P0) != complex or type(P1) != complex:
        raise TypeError("P0 and P1 must be complex types")
    # d = distance
    d = sqrt((P1.real - P0.real)**2 + (P1.imag - P0.imag)**2)
    # n**2 in Python means "n to the power of 2"
    # note: d = a + b

    if d > (r0 + r1):
        return False
    elif d < abs(r0 - r1):
        return True
    elif d == 0:
        return True
    else:
        a = (r0**2 - r1**2 + d**2) / (2 * d)
        b = d - a
        h = sqrt(r0**2 - a**2)
        P2 = P0 + a * (P1 - P0) / d

        i1x = P2.real + h * (P1.imag - P0.imag) / d
        i1y = P2.imag - h * (P1.real - P0.real) / d
        i2x = P2.real - h * (P1.imag - P0.imag) / d
        i2y = P2.imag + h * (P1.real - P0.real) / d
        
        if h==0:
            i1 = complex(i1x, i1y)
            return [i1]
        else:
            i1 = complex(i1x, i1y)
            i2 = complex(i2x, i2y)
            return [i1, i2]

def pintcodigo():
	aumentador=20
	a.ht()
	a.speed(10)
	a.up()
	a.goto((int(maxwin[0])/2-25)-100,(int(maxwin[1])/2-60))
	a.down()
	a.write("Instrucciones:",font=("Arial", 12, "bold"))
	ln=1
	for i in range(0,len(codigo)):
		a.up()
		a.goto((int(maxwin[0])/2-25)-90,(int(maxwin[1])/2-60)-aumentador)
		a.down()
		a.write(str(ln)+": "+codigo[i],font=("Arial", 12, "bold"))
		ln+=1
		aumentador+=20
	a.st()
	a.speed(1)

def pintlineacode(aumentador,s,j):
	a.up()
	a.pencolor("red")
	a.goto((int(maxwin[0])/2-25)-90,(int(maxwin[1])/2-60)-aumentador)
	a.down()
	a.write(str(j+1)+": "+s,font=("Arial", 12, "bold"))
	a.pencolor("black")
	a.up()
	a.home()

def main():
    if w==1:
        print "error"
    else:
        n=len(codigo)
        pintcodigo()
        j=0
        aumentador=0        
        while j<n:
            
            salto=0
            ban=0
            ban2=1
            try:
                ind=codigo[j].index('%')
                salto=1
            except:
                salto=0        
            if codigo[j][0]=='P' and salto==0:               
                aumentador+=20
                pintlineacode(aumentador,codigo[j],j)
                print codigo[j]
                cad=codigo[j][2:-1]
                cad1=cad.split(',')                
                for i in cad1:
                    for e in listanuevapuntos:
                        if e[-1]==i:
                            ban=1
                if ban:
                    a.up()
                    a.home()
                    a.down()
                    a.write("Puntos repetidos")
                    j=n
                else:
                    for i in cad1:
                        puntosaleatorios(i)
                    j+=1
            elif codigo[j][0]=='C' and salto==0:
                aumentador+=20
                pintlineacode(aumentador,codigo[j],j)
                print codigo[j]
                cad=codigo[j][2:-1]
                cad1=cad.split(',')        
                pos=0
                for e in listanuevapuntos:
                    if e[-1]==cad1[0]:
                        centro=listanuevapuntos[pos]
                    if e[-1]==cad1[1]:
                        radio=listanuevapuntos[pos]
                    pos+=1        
                circulo(centro,radio)
                o=(centro[-1],radio[-1])
                listacirculos.append(o)
                j+=1
            elif codigo[j][0]=='L' and salto==0:                
                if codigo[j][1]=='(': 
                    aumentador+=20
                    pintlineacode(aumentador,codigo[j],j)				
                    print codigo[j]
                    cad=codigo[j][2:-1]
                    cad1=cad.split(',')
                    pos=0                     
                    for e in listanuevapuntos:
                        if e[-1]==cad1[0]:
                            p1=listanuevapuntos[pos]
                        if e[-1]==cad1[1]:
                            p2=listanuevapuntos[pos]            
                        pos+=1                    
                    linea1(p1,p2)
                    o=(p1[-1],p2[-1])
                    listalineas.append(o)
                    j+=1
                elif codigo[j][1]=='C' and salto==0:                        
                    aumentador+=20
                    pintlineacode(aumentador,codigo[j],j)					
                    print codigo[j]
                    cad=codigo[j][3:-1]           
                    cad1=cad.split(';')
                    auxcad=cad1[0].split(',')
                    qw=[]
                    qw.append(auxcad[0])
                    qw.append(auxcad[1])
                    qw.append(cad1[-1])
                    pos=0            
                    for e in listanuevapuntos:                
                        if e[-1]==qw[0]:
                            centro=listanuevapuntos[pos]
                        if e[-1]==qw[1]:
                            punto=listanuevapuntos[pos]
                        pos+=1
                    tu=(centro[-1],punto[-1])
                    ban=0            
                    for e in listacirculos:                
                        if e==tu:
                            ban=1
                    for e in listacirculosetiquetados:
                        if e[0]==qw[-1]:
                            ban2=0
                    if ban and ban2:
                        x1=centro[0]
                        y1=centro[1]
                        x2=punto[0]
                        y2=punto[1]
                        a.up()
                        a.setx(x1)
                        a.sety(y1)    
                        r=a.distance(x2,y2)
                        a.setpos(x1,y1-r-20)
                        label=(x1,y1-r-20,qw[-1])
                        listaetiquetas.append(label)
                        a.down()
                        a.write(str(qw[-1]),font=("Arial", 12, "bold"))
                        #a.ht()
                        g=(qw[-1],qw[0],qw[1])
                        listacirculosetiquetados.append(g)
                        j+=1
                    else:
                        if  ban2==0:
                            a.up()
                            a.home()
                            a.down()
                            a.write("Cirulo ya etiquetado")
                        else:
                            print "No existe ese circulo con centro en "+str(centro[-1])+" y que pasa por el punto "+str(punto[-1])
                            a.up()
                            a.home()
                            a.down()
                            a.write("No existe ese circulo con centro en "+str(centro[-1])+" y que pasa por el punto "+str(punto[-1]))
                            #a.ht()
                        j=n
                elif codigo[j][1]=='L':
                    aumentador+=20
                    pintlineacode(aumentador,codigo[j],j)
                    print codigo[j]
                    cad=codigo[j][3:-1]
                    cad1=cad.split(';')
                    auxcad=cad1[0].split(',')
                    qw=[]
                    qw.append(auxcad[0])
                    qw.append(auxcad[1])
                    qw.append(cad1[-1])
                    pos=0            
                    for e in listanuevapuntos:                
                        if e[-1]==qw[0]:
                            p1=listanuevapuntos[pos]
                        if e[-1]==qw[1]:
                            p2=listanuevapuntos[pos]
                        pos+=1
                    tu=(p1[-1],p2[-1])
                    ban=0    
                    for e in listalineas:                
                        if e==tu:
                            ban=1
                    for e in listadelineasetiquetadas:
                        if e[0]==qw[-1]:
                            ban2=0
                    if ban and ban2:
                        p1x=p1[0]
                        p1y=p1[1]
                        p2x=p2[0]
                        p2y=p2[1]
                        a.up()
                        a.setpos(p1x,p1y)
                        t=a.towards(p2x,p2y)
                        d=a.distance(p2x,p2y)
                        a.rt(t)
                        a.fd(d/2)
                        a.setheading(0)
                        pos=a.pos()
                        label=(pos[0],pos[1],qw[-1])
                        listaetiquetas.append(label)
                        a.down()
                        a.write(str(qw[-1]),font=("Arial", 12, "bold"))
                        g=(qw[-1],qw[0],qw[1])
                        listadelineasetiquetadas.append(g)
                        j+=1
                    else:
                        if ban2==0:
                            a.up()
                            a.home()
                            a.down()
                            a.write("Linea ya etiquetada")
                        else:
                            print "No existe la linea que pasa por "+str(p1[-1])+" y "+str(p2[-1])
                            a.up()
                            a.home()
                            a.down()
                            a.write("No existe la linea que pasa por "+str(p1[-1])+" y "+str(p2[-1]))
                            #a.ht()                
                        j=n
                elif codigo[j][1]=='P' and salto==0:                    
                    aumentador+=20
                    pintlineacode(aumentador,codigo[j],j)
                    print codigo[j]
                    obj1,obj2 = 0,0
                    cad=codigo[j][3:-1]
                    cad1=cad.split(';')
                    auxcad=cad1[0].split(',')
                    auxcad1=cad1[1].split(',')
                    qw=[]
                    qw.append(auxcad[0])
                    qw.append(auxcad[1])                    
                    qw.append(auxcad1[0])                    
                    if len(auxcad1)<2:                        
                        for e in listadelineasetiquetadas:
                            if e[0]==qw[0]:
                                lin1=e                                
                            if e[0]==qw[1]:
                                lin2=e
                        for e in listadelineasetiquetadas:       
                            if e[0]==qw[0]:
                                r1=e
                            if e[0]==qw[1]:
                                r2=e                            
                        for e in listanuevapuntos:
                            if e[-1]==r1[1]:
                                p1r1=e
                            if e[-1]==r1[2]:
                                p2r1=e
                            if e[-1]==r2[1]:
                                p1r2=e
                            if e[-1]==r2[2]:
                                p2r2=e                        
                        a1=p2r1[1]-p1r1[1]
                        b1=p1r1[0]-p2r1[0]
                        c1=a1*p1r1[0]+b1*p1r1[1]                        
                        a2=p2r2[1]-p1r2[1]
                        b2=p1r2[0]-p2r2[0]
                        c2=a2*p1r2[0]+b2*p1r2[1]                        
                        det=a1*b2-a2*b1
                        if det==0:
                            print "las lineas son paralelas"
                            j+=1
                        else:
                            x=(b2*c1-b1*c2)/det
                            y=(a1*c2-a2*c1)/det
                            tu=[x,y,qw[-1]]
                            listanuevapuntos.append(tu)                                                        
                            j+=1                        
                    else:                        
                        qw.append(auxcad1[1])
                        for e in listacirculosetiquetados:
                            if e[0]==qw[0]:
                                circ1=e
                                obj1=1
                            if e[0]==qw[1]:
                                circ2=e
                                obj2=1
                        for e in listadelineasetiquetadas:
                            if e[0]==qw[0]:
                                lin1=e
                                obj1=2
                            if e[0]==qw[1]:
                                lin2=e
                                obj2=2            
                        if obj1==0 or obj2==0:                        
                            a.up()
                            a.home()
                            a.down()
                            a.write("No se encontro alguno de los objetos")
                            j=n
                        if (obj1==1 and obj2==2):
                            print "interseccion entre lineas y circulos" 
                            print listanuevapuntos      
                            print circ1                     
                            for e in listanuevapuntos:
                                if e[-1]==circ1[1]:
                                    centro=e
                                    print centro
                                if e[-1]==circ1[-1]:
                                    puntopasa=e
                                    print puntopasa
                                if e[-1]==lin2[1]:
                                    p1=e
                                if e[-1]==lin2[-1]:
                                    p2==e
                            a.up()
                            a.setpos(centro[0],centro[1])
                            print puntopasa
                            r=a.distance(puntopasa[0],puntopasa[1])                            
                            if p1[0]==p2[0]:
                                h=float(centro[0])
                                k=float(centro[1])
                                A=1
                                B=-2.0*k
                                C=p1[0]-2.0*p1[0]*h+h**2+k**2-r**2
                                raiz=cuadratica(A,B,C)
                                if len(raiz)==0:
                                    print "no hay intersecciones"                                    
                                if len(raiz)==1:
                                    tu=[p1[0],raiz[0],qw[2]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(p1[0],raiz[0])                                    
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[2])
                                if len(raiz)==2:                                    
                                    tu=[p1[0],raiz[0],qw[2]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(p1[0],raiz[0])
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[2])
                                    a.up()
                                    tu=[p1[0],raiz[1],qw[3]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(p1[0],raiz[1])
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[3])                                
                            else:                                                                                                
                                m=float(p2[1]-p1[1])/float(p2[0]-p1[0])
                                b=(-1.0*m*p1[0])+p1[1]                                
                                #y=str(m)+"x + "+str(b)                                
                                #print "( "+str(centro[0])+", "+str(centro[1])+" )"
                                #print r                                
                                #eccirc="(x - "+str(centro[0])+" )2 + (y -"+str(centro[1])+" )2 = "+str(r*r)
                                #print eccirc
                                h=float(centro[0])
                                k=float(centro[1])
                                A=1.0+m**2
                                B=(2.0*m*b)+(-2.0*m*k)+(-2.0*h)                                
                                C=(h**2+b**2)+(-2.0*b*k)+(k**2)+(-1.0*r*r)
                                raiz=cuadratica(A,B,C)
                                if len(raiz)==0:
                                    print "no hay intersecciones"                                    
                                if len(raiz)==1:
                                    y=m*raiz[0]+b
                                    tu=[raiz[0],y,qw[2]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(raiz[0],y)
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[2])                                    
                                if len(raiz)==2:
                                    y1=m*raiz[0]+b
                                    y2=m*raiz[1]+b
                                    tu=[raiz[0],y1,qw[2]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(raiz[0],y1)
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[2])
                                    a.up()
                                    tu=[raiz[1],y2,qw[3]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(raiz[1],y2)
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[3])                                
                            j+=1
                        if (obj1==2 and obj2==1):                                                
                            for e in listanuevapuntos:
                                if e[-1]==circ2[1]:
                                    centro=e
                                if e[-1]==circ2[-1]:
                                    puntopasa=e
                                if e[-1]==lin1[1]:
                                    p1=e
                                if e[-1]==lin1[-1]:
                                    p2==e
                            a.up()
                            a.setpos(centro[0],centro[1])
                            r=a.distance(puntopasa[0],puntopasa[1])                            
                            if p1[0]==p2[0]:
                                h=float(centro[0])
                                k=float(centro[1])
                                A=1
                                B=-2.0*k
                                C=p1[0]-2.0*p1[0]*h+h**2+k**2-r**2
                                raiz=cuadratica(A,B,C)
                                if len(raiz)==0:
                                    print "no hay intersecciones"                                    
                                if len(raiz)==1:
                                    tu=[p1[0],raiz[0],qw[2]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(p1[0],raiz[0])                                    
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[2])
                                if len(raiz)==2:                                    
                                    tu=[p1[0],raiz[0],qw[2]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(p1[0],raiz[0])
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[2])
                                    a.up()
                                    tu=[p1[0],raiz[1],qw[3]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(p1[0],raiz[1])
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[3])                                
                            else:                                                                                                
                                m=float(p2[1]-p1[1])/float(p2[0]-p1[0])
                                b=(-1.0*m*p1[0])+p1[1]                                
                                #y=str(m)+"x + "+str(b)                                
                                #print "( "+str(centro[0])+", "+str(centro[1])+" )"
                                #print r                                
                                #eccirc="(x - "+str(centro[0])+" )2 + (y -"+str(centro[1])+" )2 = "+str(r*r)
                                #print eccirc
                                h=float(centro[0])
                                k=float(centro[1])
                                A=1.0+m**2
                                B=(2.0*m*b)+(-2.0*m*k)+(-2.0*h)                                
                                C=(h**2+b**2)+(-2.0*b*k)+(k**2)+(-1.0*r*r)
                                raiz=cuadratica(A,B,C)
                                if len(raiz)==0:
                                    print "no hay intersecciones"                                    
                                if len(raiz)==1:
                                    y=m*raiz[0]+b
                                    tu=[raiz[0],y,qw[2]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(raiz[0],y)
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[2])                                    
                                if len(raiz)==2:
                                    y1=m*raiz[0]+b
                                    y2=m*raiz[1]+b
                                    tu=[raiz[0],y1,qw[2]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(raiz[0],y1)
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[2])
                                    a.up()
                                    tu=[raiz[1],y2,qw[3]]
                                    listanuevapuntos.append(tu)
                                    a.setpos(raiz[1],y2)
                                    a.down()
                                    a.dot("blue")
                                    a.write(qw[3])                                
                            j+=1
                            
                        if obj1==1 and obj2==1:
                            print "interseccion entre circulos"                            
                            for e in listanuevapuntos:
                                if e[-1]==circ1[1]:
                                    c1centro=e
                                if e[-1]==circ1[2]:
                                    c1radio=e
                                if e[-1]==circ2[1]:
                                    c2centro=e
                                if e[-1]==circ2[2]:
                                    c2radio=e
                            xc1centro=c1centro[0]
                            yc1centro=c1centro[1]
                            xc2centro=c2centro[0]
                            yc2centro=c2centro[1]
                            xc1radio=c1radio[0]
                            yc1radio=c1radio[1]
                            xc2radio=c2radio[0]
                            yc2radio=c2radio[1]
                            a.up()
                            a.setpos(xc1centro,yc1centro)
                            discentros=a.distance(xc2centro,yc2centro)
                            c1rad=a.distance(xc1radio,yc1radio)
                            a.setpos(xc2centro,yc2centro)
                            c2rad=a.distance(xc2radio,yc2radio)
                            if discentros>(c1rad+c2rad):
                                print "No existe ninguna intersección entre los círculos"
                            elif discentros<abs(c1rad-c2rad):
                                print "Un círculo contiene al otro no hay interseccion"
                            elif discentros==(c1rad+c2rad):
                                P0=complex(xc1centro,yc1centro)
                                P1=complex(xc2centro,yc2centro)
                                inter=IntersectPoints(P0,P1,c1rad,c2rad)
                                tu=[int(inter[0].real),int(inter[0].imag),qw[2]]
                                listanuevapuntos.append(tu)
                                a.up()
                                a.setpos(inter[0].real,inter[0].imag)
                                a.dot("blue")
                                a.write(qw[2])
                                j+=1
                            else:
                                P0=complex(xc1centro,yc1centro)
                                P1=complex(xc2centro,yc2centro)
                                inter=IntersectPoints(P0,P1,c1rad,c2rad)
                                tu=[int(inter[0].real),int(inter[0].imag),qw[2]]
                                listanuevapuntos.append(tu)
                                a.up()
                                a.setpos(inter[0].real,inter[0].imag)
                                a.dot("blue")
                                a.write(qw[2])
                                tu=[int(inter[1].real),int(inter[1].imag),qw[3]]
                                listanuevapuntos.append(tu)
                                a.up()
                                a.setpos(inter[1].real,inter[1].imag)
                                a.dot("blue")
                                a.write(qw[3])
                                a.up()
                                j+=1
                            
                    #j+=1                    
                #else: 
                   # print "cosas raras"
                   # j=n
            elif codigo[j][0]=='D' and salto==0:
                aumentador+=20
                pintlineacode(aumentador,codigo[j],j)
                print codigo[j]
                eti=codigo[j][2:-1]                
                borrado=0
                for pt in listanuevapuntos:
                    if pt[2]==eti:
                        a.setpos(pt[0],pt[1])
                        a.dot("red")
                        a.pencolor("red")
                        a.write(eti)
                        a.pencolor("black")
                        listanuevapuntos.remove(pt)
                        borrado=1
                if borrado==0:
                    for ln in listadelineasetiquetadas:
                        if ln[0]==eti:
                            for pt in listaetiquetas:
                                if pt[-1]==eti:
                                    ubica=pt
                            a.up()
                            a.setpos(ubica[0],ubica[1])
                            a.pencolor("red")
                            a.write(ubica[-1],font=("Arial", 12, "bold"))
                            a.pencolor("black")
                            listadelineasetiquetadas.remove(ln)
                            borrado=1
                if borrado==0:
                    for cir in listacirculosetiquetados:
                        if cir[0]==eti:
                            for pt in listaetiquetas:
                                if pt[-1]==eti:
                                    ubica=pt
                            a.up()
                            a.setpos(ubica[0],ubica[1])
                            a.pencolor("red")
                            a.write(ubica[-1],font=("Arial", 12, "bold"))
                            a.pencolor("black")
                            listacirculosetiquetados.remove(cir)                
                j+=1
            elif salto==1:                
                aumentador+=20
                pintlineacode(aumentador,codigo[j],j)
                print codigo[j]
                existepunto=0                
                existecirculo=0
                linea=codigo[j]
                cad=list(codigo[j])
                indpt=cad.index('%')
                indcir=cad.index(':')
                ult=len(linea)
                auxpt=linea[0:indpt-1]
                auxcir=linea[indpt+2:indcir-1]
                auxnum=int(linea[indcir+2:ult])
                qw=[]
                qw.append(auxpt)
                qw.append(auxcir)
                qw.append(auxnum)
                pos=0            
                for e in listanuevapuntos:            
                    if e[-1]==qw[0]:
                        punto=listanuevapuntos[pos]
                        existepunto=1
                    pos+=1
                if existepunto:
                    pos=0
                    for e in listacirculosetiquetados:
                        if e[0]==qw[1]:
                            circ=listacirculosetiquetados[pos]
                            existecirculo=1
                        pos+=1
                    if existecirculo:                        
                        pos=0
                        for e in listanuevapuntos:
                            if e[-1]==circ[1]:
                                puntocentro=listanuevapuntos[pos]
                            if e[-1]==circ[-1]:
                                puntopasa=listanuevapuntos[pos]
                            pos+=1                        
                        a.up()
                        a.setpos(puntocentro[0],puntocentro[1])                        
                        r=a.distance(puntopasa[0],puntopasa[1])
                        d=a.distance(punto[0],punto[1])
                        #print str(r)+"  "+str(d)
                        if d<=r:                            
                            j=int(qw[-1])-1
                        else:
                            j+=1                        
                    else:
                        a.up()
                        a.home()
                        a.write("No existe el circulo etiquetado con "+str(qw[1]))
                        j=n            
                else:
                    a.up()
                    a.home()
                    a.write("No existe el punto "+str(qw[0]))                    
                    j=n
                
            else:
                print "cosas raras"
        #for i in codigo:
            #ejecuta(i)        
        a.up()        
        a.setpos(int(maxwin[0])/2-25,int(maxwin[1])/2-50)        
        a.mainloop()
    return 0

if __name__=='__main__':
    main()
