import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#graficando
colors=["#845ec2","#d65db1","#ff6f91","#ff9671","#ffc75f","#f9f871"]
#grafica de barras
plt.figure(figsize=(8,5))
sns.countplot(x='estado',data=dataFrameAsistencia,palette=colors)
plt.title("cantidad de registros por estado de asistencia")
plt.xlabel("estado de asistencia")
plt.ylabel("cantidad de registro")
plt.tight_layout()
plt.show()

#GRAFICAA DE TORTA 
#MOSTRAR PROPROCIONES ENTR DOS COLUNABS DE dF (PROPORCION DE ESTUDIANTES MEDIO TRANSPORTES)

conteoMedioTransporte=dataFrameAsistencia['medio_transporte'].value_counts()

plt.figure(figsize=(5,5))
plt.pie(
    conteoMedioTransporte,
    labels=conteoMedioTransporte.index,
    autopct='%1.1f%%',
    colors=sns.color_palette("Blues")
)
plt.title("distribucion de estudiantes por medio de transportes")
plt.tight_layout()
plt.show()

conteoEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)

conteoEstadoMedioTransporte.plot(
    kind='bar',
    figsize=(10,5),
    color=colors
)

plt.title("cantidad de registros por estado de asistencia")
plt.xlabel("estado de asistencia")
plt.ylabel("cantidad de registro")
plt.legend(title="Medio de transporte")
plt.tight_layout()
plt.show()


#tarea no hay presencial la otra semana analize los filtros de el proyecto integrado hacer tres diagramas de barras como quiera ya sea de torta.etc,
