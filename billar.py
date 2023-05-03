import numpy as np
import pygame,sys
from pygame.locals import *
import random
import os


R=30
alto = 500
ancho = 1000
h=0


X0=[(ancho/2)]
Y0=[alto-R]
vx=[0]
vy=[0]
ax=0
ay=0
ay0=0
DELAY=10
x=[X0[0]]
y=[Y0[0]]
taupiso=0.95
tau=0.998
tau0=tau


Xeje=0
Yeje=0
piso=int(alto-R/2+Yeje)
techo=int(0+R/2+Yeje)
pared0=int(0+R/2-Xeje)
pared1=int(ancho-R/2-Xeje)


usoKEYUP=False
usoKEYDOWN=False
usoKEYRIGHT=False
usoKEYLEFT=False
ck1=0
ck2=0
ck3=0
ck4=0
intervalo=4
modvx=0.
modvy=0.
dvx=0.
minvYpiso=0.01



drP=[1]
dr=1
dt=100

radio=1
rADIO0=30	
FuerzaControl=1
tita=0.					
XVER=-1
YVER=-1			
Cuadrante=4
Fx=0.
Fy=0.


CantBolas=1
X=50
Y=50
tita=0
M=[1000]
kill=[False]
m=[1]
G=3000
Fx=0.
Fy=0.
r=0.

poligonX=[0]
poligonY=[0]
poligonX0=[0]
poligonY0=[0]


FIJO=[False]
PxFijo=[0]
PyFijo=[0]
select=1

CLAVADO=True
CLAVADO2=False
ANALISIS=False #INIDICA SI LAS BOLAS QUE NO SON M0 SE sinTIRAN ENTRE ELLAS
CHOQUES=True	#INDICA SI LOS CHOQUES ESTAN ACTIVADOS
PAREDES=True 
CamFija=False
BarraON=True
freez=False

pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
screen = pygame.display.set_caption("Spaceinvader")

img=[pygame.image.load("spaceinvader.png")]
rect=[img[0].get_rect()]

#MODO PREsinTACION
#imgPELON=pygame.image.load("pelonazo.png")
#rectPELON=imgPELON.get_rect()

LabelSys1=pygame.font.SysFont("Calibri", 20)
LabelSys2=pygame.font.SysFont("Calibri", 30)
fnt=20
fnt2=50



def radio(a,b):
	try:
		r=((((x[b-1]-x[a-1])/dr)**2)+((-y[b-1]+y[a-1])**2))**(1/2)
	except:
		pass
		print("func:r(a,b)  - a y/o b no existen")
		r=rADIO0

	if r==0:
		print("func:r(a,b)  - r=0, se estableció r=rADIO0")
		r=rADIO0
	return(r) 

def tita(a,b):
	X=x[b-1]-x[a-1]
	Y=-y[b-1]+y[a-1]
	if X==0:						
		if Y>=0:
			tita=np.pi/2			
		else:
			tita=-(np.pi/2)
	else:
		if X>0:
			tita=np.arctan(Y/X)	
		if X<0:
			tita=(np.arctan(Y/X))+np.pi	
	return(tita)

def titaP(x0, y0, x,y):
	X=x-x0
	Y=-y+y0
	if X==0:						
		if Y>=0:
			titaP=np.pi/2			
		else:
			titaP=-(np.pi/2)
	else:
		if X>0:
			titaP=np.arctan(Y/X)	
		if X<0:
			titaP=(np.arctan(Y/X))+np.pi	
	return(titaP)

def ANGPAREDES(vx, x0, vy, y0):
	if PAREDES==True:

		x=int(x0)+int(vx)
		y=int(y0)+int(vy)
		choquepared0=False
		choquepared1=False
		choquetecho=False
		choquepiso=False

		if vx<=0:
			if x<=pared0<x0:
				choquepared0=True
			if x<=pared1<x0:
				choquepared1=True

		else:
			if x>=pared0>x0:
				choquepared0=True
			if x>=pared1>x0:
				choquepared1=True


		if vy<=0:
			if y<=piso<y0:
				choquepiso=True
			if y<=techo<y0:
				choquetecho=True

		else:
			if y>=piso>y0:
				choquepiso=True
			if y>=techo>y0:
				choquetecho=True

		print("x0,x1,y0,y1:",choquepared0,choquepared1,choquepiso,choquetecho)
		if choquepared0==True:
			x0=int(pared0)
			alpha=0
			vy=(vy*(2*((np.cos(alpha))**2)-1)-vx*np.sin(2*alpha))*taupiso
			vx=(vx*(2*((np.sin(alpha))**2)-1)-vy*np.sin(2*alpha))*taupiso
			choquepared0=False



		if choquepared1==True:
			x0=int(pared1)
			alpha=-np.pi
			vy=(vy*(2*((np.cos(alpha))**2)-1)-vx*np.sin(2*alpha))*taupiso
			vx=(vx*(2*((np.sin(alpha))**2)-1)-vy*np.sin(2*alpha))*taupiso
			choquepared1=False


		if choquetecho==True:
			y0=int(techo)
			alpha=-np.pi/2
			vy=(vy*(2*((np.cos(alpha))**2)-1)-vx*np.sin(2*alpha))*taupiso
			vx=(vx*(2*((np.sin(alpha))**2)-1)-vy*np.sin(2*alpha))*taupiso
			choquetecho=False

		if choquepiso==True:
			y0=int(piso)
			alpha=np.pi/2
			vy=(vy*(2*((np.cos(alpha))**2)-1)-vx*np.sin(2*alpha))*taupiso
			vx=(vx*(2*((np.sin(alpha))**2)-1)-vy*np.sin(2*alpha))*taupiso
			choquepiso=False



	return([x0, y0, vx, vy])
				
 


YaChoco={}
Choq=False
h0=0
jugando = True
file = open("prueba1.txt", "w")
file.write("Hello people this is the start of the first try in the story of the writes in python in the course of learning"+os.linesep)
file.write(""+os.linesep+os.linesep+os.linesep)
while jugando:
	
	PTotal=0
	
	piso=int(alto-R/2+Yeje)
	techo=int(0+R/2+Yeje)
	pared0=int(0+R/2-Xeje)
	pared1=int(ancho-R/2-Xeje)
	h=h+1

	if CantBolas==1:						#Caso CantBolas ==1 se presintó como algo que no parece estar contemplado en el caso del loop
		Fy=0								# Evidentemente no le gusta a la funcion "range()" tener(0, 0) como argumento, asique debo definir el caso ese. 
		Fx=0
		
		vy[0]=(vy[0]*tau+Fy+ay)
		vx[0]=(vx[0]*tau+Fx+ax)

		if PAREDES==True:
			Rebote=ANGPAREDES(vx[0]/dt, x[0], vy[0]/dt, y[0])
			x[0]=Rebote[0]
			y[0]=Rebote[1]
			vx[0]=Rebote[2]*dt
			vy[0]=Rebote[3]*dt


		y[0]=y[0]+int(vy[0]/dt)
		x[0]=x[0]+int(vx[0]/dt)

		PTotal=M[0]/2*((vx[0]**2+vy[0]**2)**(1/2))

	else:
		for i in range(0,CantBolas-1):				#Ya sin 1 sola bola
			Fx=0
			Fy=0
			if FIJO[i]==True:
				x[i]=PxFijo[i]	
				y[i]=PyFijo[i]
			elif CantBolas>1:
				for n in range(0,CantBolas-1):
					if i==n:
						pass
					else:
						if kill[n]==True:		#Por esta condicion "kill[n]==True nadie siente a fuerza de bola"n"
							FxN=0
							FyN=0
						else:


							if ANALISIS==True:
								if n==0:
									#aca todas las operaciones que tiene cada componente de F
									FyN=0.		#    NO   TOCAR   PARTE   DE    ANALISIS
									FxN=0.		#    NO   TOCAR   PARTE   DE    ANALISIS
									r=0.		#    NO   TOCAR   PARTE   DE    ANALISIS
									X=0
									Y=0
									tita=0.		#    NO   TOCAR   PARTE   DE    ANALISIS
									if FIJO[n]==True:		#    NO   TOCAR   PARTE   DE    ANALISIS
										x[n]=PxFijo[n]		#    NO   TOCAR   PARTE   DE    ANALISIS
										y[n]=PyFijo[n]		#    NO   TOCAR   PARTE   DE    ANALISIS


									X=(x[i]-x[n])		#    NO   TOCAR   PARTE   DE    ANALISIS
									Y=(-y[i]+y[n])		#    NO   TOCAR   PARTE   DE    ANALISIS
									r=((X)**2+(Y)**2)**(1/2)		#    NO   TOCAR   PARTE   DE    ANALISIS
								

									if X==0:						#El angulo no hace falta usarlo en este caso, porque pusimos directo X, que es r.cos(tita)
										if Y>=0:
											tita=np.pi/2			# pero por si hace falta esta disponible el ángulo.
										else:
											tita=-(np.pi/2)		#    NO   TOCAR   PARTE   DE    ANALISIS
									else:
										if X>0:		#    NO   TOCAR   PARTE   DE    ANALISIS
											tita=np.arctan(Y/X)			#    NO   TOCAR   PARTE   DE    ANALISIS
										if X<0:
											tita=(np.arctan(Y/X))+np.pi			#    NO   TOCAR   PARTE   DE    ANALISIS


									if r<rADIO0:		#    NO   TOCAR   PARTE   DE    ANALISIS
										r=rADIO0		#    NO   TOCAR   PARTE   DE    ANALISIS

									FyN=G*M[n]*Y/((r)**3)   
 
									FxN=-G*M[n]*X/((r)**3)
								else:
									FyN=0.					#    NO   TOCAR   PARTE   DE    ANALISIS
									FxN=0.		#    NO   TOCAR   PARTE   DE    ANALISIS

							else:				#FIN DEL ANALISIS

								FyN=0.
								FxN=0.
								r=0.
								X=0
								Y=0
								tita=0.
								if FIJO[n]==True:
									x[n]=PxFijo[n]
									y[n]=PyFijo[n]


								X=(x[i]-x[n])
								Y=(-y[i]+y[n])
								r=((X)**2+(Y)**2)**(1/2)
									
								if X==0:					
									if Y>=0:
										tita=np.pi/2	
									else:
										tita=-(np.pi/2)	
								else:
									if X>0:	
										tita=np.arctan(Y/X)
									if X<0:
										tita=(np.arctan(Y/X))+np.pi	
								X2=-X
								Y2=-Y
								if X2==0:					
									if Y2>=0:
										tita2=np.pi/2	
									else:
										tita2=-(np.pi/2)	
								else:
									if X2>0:	
										tita2=np.arctan(Y2/X2)
									if X2<0:
										tita2=(np.arctan(Y2/X2))+np.pi	

								if r<=rADIO0:
									if X>=0:
										x[i]=x[i]+(rADIO0-r)*np.cos(tita)/2
										x[n]=x[n]-(rADIO0-r)*np.cos(tita)/2
									else:
										x[i]=x[i]-(rADIO0-r)*np.cos(tita)/2
										x[n]=x[n]+(rADIO0-r)*np.cos(tita)/2
									if Y>=0:
										y[i]=y[i]+(rADIO0-r)*np.sin(tita)/2
										y[n]=y[n]-(rADIO0-r)*np.sin(tita)/2
									else:
										y[i]=y[i]-(rADIO0-r)*np.sin(tita)/2
										y[n]=y[n]+(rADIO0-r)*np.sin(tita)/2
									r=rADIO0



								if CHOQUES==True:

									Choq=False
									if r<=rADIO0:

										try:
											if YaChoco[i][0]==True:
												print("aca0, yachoco activado, no se chocara denuevo")
												Choq=True
												r=rADIO0
										except:
											print("aca0, yachoco descativado, se chocará")
											r=rADIO0
											pass

										if Choq==False:
											
											C=M[n]/M[i]
											vxRes=vx[i]
											vyRes=(-vy[i])

											vxi=vxRes*(1-2*C/(1+C))
											vyi=vyRes*(1-2*C/(1+C))
											YaChoco[i]=[True, vxi, -vyi, 1]


											vxn=2*(vxRes)/(1+C)
											vyn=2*(vyRes)/(1+C)
											YaChoco[n]=[True, vxn, -vyn, 1]


											C2=M[i]/M[n]
											vxRes=vx[n]
											vyRes=(-vy[n])
											vxi=vxRes*(1-2*C2/(1+C2))
											vyi=vyRes*(1-2*C2/(1+C2))
											YaChoco[n]=[True, YaChoco[n][1]+vxi, YaChoco[n][2]-vyi, 1]


											vxn=2*(vxRes)/(1+C2)
											vyn=2*(vyRes)/(1+C2)
											YaChoco[i]=[True, YaChoco[i][1]+vxn, YaChoco[i][2]-vyn, 1]

								

								FyN=G*M[n]*Y/((r)**3)
								FxN=-G*M[n]*X/((r)**3)
								#aca termina el for de esa bola "n" con esa i, pasa a la siguiente "n".


						Fx=Fx+FxN
						Fy=Fy+FyN

						#aca termina el for de esa bola "i" con todas las "n", pasa a la siguiente "i".


			if CHOQUES==True:
				try:
					if YaChoco[i][0]==True:
						vx[i]=YaChoco[i][3]*YaChoco[i][1]
						print("yachoco1", vx[i], i)
						vy[i]=YaChoco[i][3]*YaChoco[i][2]
						print("yachoco2", vy[i], i)
						YaChoco[i][0]=False
				except:
					pass

			vy[i]=(vy[i]*tau+Fy+ay)
			print("vy", vy[i], i)
			vx[i]=(vx[i]*tau+Fx+ax)
			print("vx", vx[i], i)


			if PAREDES==True:
				Rebote=ANGPAREDES(vx[i]/dt, x[i], vy[i]/dt, y[i])
				x[i]=int(Rebote[0])
				y[i]=int(Rebote[1])
				vx[i]=int(Rebote[2]*dt)
				vy[i]=int(Rebote[3]*dt)


			if FIJO[i]==True:
				y[i]=int(PyFijo[i])
				x[i]=int(PxFijo[i])
			else:
				y[i]=y[i]+int(vy[i]/dt)
				x[i]=x[i]+int(vx[i]/dt)


			poligonX[i]=int(Fx+x[i])
			poligonY[i]=int(Fy+y[i])
			poligonX0[i]=int(x[i])
			poligonY0[i]=int(y[i])


			PTotal=PTotal+M[i]*(((vx[i]**2)+(vy[i])**2)**(1/2))/2


	rango=slice(0,11)

	txt=["Tiempo:",str(h),"X:", str(x[0]),"Y:", str(y[0]),"Radio:",str(r)[rango],"Tita:",str(tita)[rango],"G:", str(G),"CantBolas:",str(CantBolas),"FzaControl:",str(FuerzaControl),"ay:",str(ay),"tau:",str(tau),"M0:",str(M[0]),"dr:",str(dr),"select:",str(select), "paredes:", str(PAREDES),"PTotal:", str(PTotal)]
	lentxt=[6, 6, 2, 6, 2, 6, 5, 11, 4, 11, 2, 6, 8, 4, 9, 6, 2, 4, 3, 6, 3, 6, 2, 4, 5, 3, 6, 4,6,6]
	cant1=len(txt)


	for i in range(2,CantBolas-1):	#imprime radio de todas las bolas respecto a M0
		print("R",str(radio(0,i))[rango])
		#Ahroa falta borrar estos agregados para antes de la siguiente ronda



	cantxt=len(txt)+1
	lent=30
	filas=1
	xtxt=[0]
	ytxt=[0]
	for i in range(0,cantxt):
		if i==0:
			pass
	
		else:
			lent=lent+lentxt[i-1]*12

		try:
			xtxt[i]=lent+int(i/2)*15
		except:
			xtxt.append(lent+int(i/2)*15)

		if xtxt[i]+50>=ancho:
			filas=filas+1
			xtxt[i]=xtxt[i]-ancho
			lent=lent-ancho

		try:
			ytxt[i]=filas*15
		except:
			ytxt.append(filas*15)

	texto=[""]
	for i in range(0,cantxt-1):
		try:
			texto[i]=LabelSys1.render(txt[i],False, (225, 225, 225))
		except:	
			texto.append(LabelSys1.render(txt[i],False, (225, 225, 225)))

		ventana.blit(texto[i], (xtxt[i],ytxt[i]))



	#VISOR PRINCIPAL
	textoVy=LabelSys2.render("raiz(G*M/R): Vy",False, (225, 225, 225))
	textoVy2=LabelSys2.render(str(np.sqrt(G*M[0]/(250*dr))),False, (225, 225, 225))
	textoR=LabelSys2.render("R:",False, (225, 225, 225))
	textoR2=LabelSys2.render(str(250*dr),False, (225, 225, 225))
	#BARRA
	if BarraON==True:
		pygame.draw.line(ventana,(255,0,0), (int(Xeje),int(Yeje)),(int(Xeje+250),int(Yeje+0)),3)


	if freez==False:
		ventana.blit(textoVy,(int(ancho*3/4),int(alto*3/4-30)))
		ventana.blit(textoVy2,(int(ancho*3/4),int(alto*3/4)))
		ventana.blit(textoR,(int(ancho*3/4),int(alto*3/4+30)))
		ventana.blit(textoR2,(int(ancho*3/4+30),int(alto*3/4+30)))






	#MODO PREsinTACION#
	#ventana.blit(imgPELON,(ancho/2-330, alto/2-70-120))

 
	if CamFija==True:
		Xeje=-x[0]/dr+ancho/2
		Yeje=-y[0]/dr+alto/2
	if CantBolas==1:		
		rect[0].left = int(x[0]-R/2)
		rect[0].top = int(y[0]-R/2)
		ventana.blit(img[0],rect[0])
		pygame.draw.line(ventana,(255,255,255),(poligonX0[0], poligonY0[0]),(poligonX[0],poligonY[0]),4)
	else:
		for i in range(0, CantBolas-1):

			rect[i].left = int(Xeje+(x[i]-R/2)/dr)
			rect[i].top = int(Yeje+(y[i]-R/2)/dr)
			ventana.blit(img[i],rect[i])
			if i==0:
				pygame.draw.line(ventana,(255,0,0),(int(Xeje+poligonX0[i]/dr), int(Yeje+poligonY0[i]/dr)),(int(Xeje+poligonX[i]/dr),int(Yeje+poligonY[i]/dr)),4)
			else:
				pass 






	#UNA VEZ SETEADA NUESTRA PANTALLA LA MOSTRAMOS, BRINDAMOS LA DATA A LA CONSOLA, Y DEMORAMOS LA SIGUIENTE INTERACION.
	pygame.display.flip()
	pygame.time.wait(DELAY)
	file.write(str(PTotal) + " -             "+ str(CantBolas) + os.linesep)
	#Luego de dibujar borramos la pantalla en los sectores elegidos
 
	poly = [(0,0), (ancho,0), (ancho, int((filas+1)*30)), (0, int((filas+1)*30)),(0,0) ]
	pygame.draw.polygon(ventana, (0, 0, 0), poly, 0)


	poly2 = [(0,int((filas+1)*30)), (0,alto) , (ancho, alto), (ancho,int((filas+1)*30)),(0,int((filas+1)*30))]
	
	if freez==False:

		pygame.draw.polygon(ventana, (0, 0, 0), poly2, 0)

	#ACA EMPIEZA LA PROGRAMACION DEL MANDO:

	#1ERO LOS CHECK DE USO Y SUS CONTADORES SE BAJAN UNA VUELTA SI ES EL CASO.
	if usoKEYUP==True:
		vy[0]=vy[0]-100*FuerzaControl


	if usoKEYRIGHT==True:
		vx[0]=vx[0]+50*FuerzaControl


	if usoKEYLEFT==True:
		vx[0]=vx[0]-50*FuerzaControl


	if usoKEYDOWN==True:
		vy[0]=vy[0]+100*FuerzaControl


	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
		    pygame.quit()	
		elif event.type == pygame.KEYUP:
			if event.key==273:
				usoKEYUP=False

			elif event.key==275:
				usoKEYRIGHT=False

			elif event.key == 276:
				usoKEYLEFT=False

			elif event.key == 274:
				usoKEYDOWN=False

		elif event.type == pygame.KEYDOWN:
			
			if event.key==K_UP:
				if usoKEYUP==True:
					pass
				else:	
					#print(vy)
					usoKEYUP=True

			elif event.key==K_RIGHT:
				if usoKEYRIGHT==True:
					pass
				else:	
					#print(vy)
					usoKEYRIGHT=True

			elif event.key == K_LEFT:
				if usoKEYLEFT==True:
					pass
				else:	
					#print(vx)
					usoKEYLEFT=True

			elif event.key == K_DOWN:
				if usoKEYDOWN==False:
					usoKEYDOWN=True
				else:
					pass


			elif event.key==117: #U
				#print("U")
				if G>=3000:
					G=G+1000
				elif G>=300:
					G=G+100
				elif G>=10:
					G=G+10
				else:
					G=G+1
					
				
			elif event.key==121: #Y
				#print("Y")
				if G>3000:
					G=G-1000
				elif G>300:
					G=G-100
				elif G>10:
					G=G-10
				else:
					G=G-1
					

			elif event.key==106: #J
				#print("J")
				FuerzaControl=FuerzaControl+1
					

				
			elif event.key==104: #H
				#print("H")
				FuerzaControl=FuerzaControl-1
					

			elif event.key==110: #N
				#print("N")
				tau=tau-0.001
					

				
			elif event.key==109: #M
				#print("M")
				tau=tau+0.001
					

			elif event.key==44: #,  (coma)
				#print("ay")
				if ay==100:
					ay=ay-10
				else:
					ay=ay-10
					

				
			elif event.key==48: # 0  (teclado letras)
				#print("0")

				if CantBolas>=3:
					CantBolas=CantBolas-1
					x.pop
					y.pop
					vx.pop
					vy.pop
					M.pop
					m.pop
					poligonX.pop
					poligonX0.pop
					poligonY.pop
					poligonY0.pop
					img.pop
					rect.pop
					FIJO.pop
					PxFijo.pop
					PyFijo.pop

			elif event.key==46: # .  (punto)
				#print(".")
				if ay==0:
					ay=ay+10
				else:
					ay=ay+10

			elif event.key==47: # - (guion medio)  desactiva barra roja de radio
				#print("-")
				if BarraON==True:
					BarraON=False
				else:
					BarraON=True


			elif event.key==55: #7 
				#print("7")
				if select==100:
					pass
				else:
					if select==CantBolas-1:
						pass
					else:
						select=select+1
						kill[select]=True
					

				
			elif event.key==54: # 6 
				#print("6")
				if select==1:
					pass
				else:
					select=select-1



				
			elif event.key==115: # s
				if M[0]>=3000:
					M[0]=M[0]+1000
				elif M[0]>=300:
					M[0]=M[0]+100
				elif M[0]>=10:
					M[0]=M[0]+10
				else:
					M[0]=M[0]+1


			elif event.key==97: # a
				if M[0]>3000:
					M[0]=M[0]-1000
				elif M[0]>300:
					M[0]=M[0]-100
				elif M[0]>10:
					M[0]=M[0]-10
				else:
					M[0]=M[0]-1



			elif event.key==96: # |
				if PAREDES==True:
					PAREDES=False
					
				else:
					PAREDES=True
				#PAREDES=CParedes(PAREDES)



			elif event.key==32:  #Barra espaciadora

				if CantBolas==1:
					Xeje=ancho/2
					Yeje=alto/2
					tau=1
					ay=0
					x[0]=0
					y[0]=0
					
					#PAREDES=CParedes(PAREDES)

				pipi=(250)*dr
				CantBolas=CantBolas+1
				x.append(pipi)
				y.append(0)
				vx.append(0)
				vy.append(-(dt*G*M[0]/(pipi))**(1/2))

				M.append(1)
				m.append(1)
				poligonX.append(0)
				poligonX0.append(0)
				poligonY.append(0)
				poligonY0.append(0)
				if CLAVADO==False:
					FIJO.append(False)
					kill.append(False)
				else:
					FIJO.append(True)
					kill.append(True)

				if CantBolas<20:
					PxFijo.append(CantBolas*(ancho/20)-ancho/2)
					PyFijo.append(-alto/2)
				elif CantBolas<40:
					PxFijo.append((CantBolas-20)*(ancho/20)-ancho/2)
					PyFijo.append(+alto/2)
				elif CantBolas<60:
					PxFijo.append(-ancho/2)
					PyFijo.append((CantBolas-40)*(alto/20)-alto/2)
				elif CantBolas<80:
					PxFijo.append(ancho/2)
					PyFijo.append((CantBolas-60)*(alto/20)-alto/2)
				img.append(pygame.image.load("spaceinvader.png"))
				img[CantBolas-1]=pygame.transform.scale(img[CantBolas-1], (int(R/dr),int(R/dr)))
				rect.append(img[CantBolas-1].get_rect())



			elif event.key==256:  #0 TEC NUM
				
				if CantBolas>=3:
					CantBolas=CantBolas-1
					x.pop
					y.pop
					vx.pop
					vy.pop
					M.pop
					m.pop
					poligonX.pop
					poligonX0.pop
					poligonY.pop
					poligonY0.pop
					img.pop
					rect.pop
					FIJO.pop
					PxFijo.pop
					PyFijo.pop


			elif event.key==114:  #R 
				
				if CantBolas>=2:
					DEST=CantBolas-1
					for i in range(DEST):
						i=i+1
						x.pop
						y.pop
						vx.pop
						vy.pop
						M.pop
						m.pop
						poligonX.pop
						poligonX0.pop
						poligonY.pop
						poligonY0.pop
						img.pop
						rect.pop
						FIJO.pop
						PxFijo.pop
						PyFijo.pop
					CantBolas=1
					x[0]=0+Xeje
					y[0]=0+Yeje
					vx[0]=0
					vy[0]=0



			elif event.key==261:  #5 TEC NUM
				
				if CamFija==False:
					CamFija=True
				else:
					CamFija=False




			elif event.key==102:  #f

				if FIJO[select-1]==False:
					FIJO[select-1]=True
				else:
					FIJO[select-1]=False
					vx[select-1]=0
					vy[select-1]=0


			elif event.key==99:  #c
				if CLAVADO==True:
					CLAVADO=False
				else:
					CLAVADO=True

			elif event.key==303:  #Shift D
				if freez==True:
					freez=False
				else:
					freez=True
				



			elif event.key==270:  #+ TEC NUM
				if dr>=30:
					dr=dr+10
				else:
					dr=dr+1

				for i in range(0, CantBolas):
					img[i]=pygame.image.load("spaceinvader.png")
					if int(R/dr)<2:
						img[i]=pygame.transform.scale(img[i], (2, 2)) 
					else:
						img[i]=pygame.transform.scale(img[i], (int(R/dr), int(R/dr))) 

			elif event.key==269:  #- TEC NUM
				if dr<=10:
					if dr==1:
						pass
					else:
						dr=dr-1
				else:
					dr=dr-10

				for i in range(0, CantBolas):
					img[i]=pygame.image.load("spaceinvader.png")
					if int(R/dr)<2:
						img[i]=pygame.transform.scale(img[i], (2, 2)) 
					else:
						img[i]=pygame.transform.scale(img[i], (int(R/dr), int(R/dr))) 


			elif event.key==260: # 4  (punto)
				if CLAVADO2==True:
					PxFijo[select-1]=PxFijo[select-1]-50
				else:
					Xeje=Xeje+50

			elif event.key==264: # 8  (punto)
				if CLAVADO2==True:
					PyFijo[select-1]=PyFijo[select-1]-50
				else:
					Yeje=Yeje+50

			elif event.key==262: # 6  (punto)
				if CLAVADO2==True:
					PxFijo[select-1]=PxFijo[select-1]+50
				else:
					Xeje=Xeje-50

			elif event.key==258: # 2  (punto)
				if CLAVADO2==True:
					PyFijo[select-1]=PyFijo[select-1]+50
				else:
					Yeje=Yeje-50


			elif event.key==113:  #Q   elije o no el clavado2 que sirve para mover la posicion donde fijamos a la pelota 
										# indicada por "select"
				if CLAVADO2==False:
					CLAVADO2=True
				else:
					CLAVADO2=False

			elif event.key==93:  #+ notebook
				if dr>=30:
					dr=dr+10
				else:
					dr=dr+1

				for i in range(0, CantBolas):
					img[i]=pygame.image.load("spaceinvader.png")
					if int(R/dr)<2:
						img[i]=pygame.transform.scale(img[i], (2, 2)) 
					else:
						img[i]=pygame.transform.scale(img[i], (int(R/dr), int(R/dr))) 

			elif event.key==92:  #- notebook
				if dr<=10:
					if dr==1:
						pass
					else:
						dr=dr-1
				else:
					dr=dr-10

				for i in range(0, CantBolas):
					img[i]=pygame.image.load("spaceinvader.png")
					if int(R/dr)<2:
						img[i]=pygame.transform.scale(img[i], (2, 2)) 
					else:
						img[i]=pygame.transform.scale(img[i], (int(R/dr), int(R/dr))) 


#SI SE CIERRA EL BUCLE (BREAK) SE LLAMA AL CIERRE.
pygame.quit()   