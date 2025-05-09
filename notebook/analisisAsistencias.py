import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")


#ANTES DE FILTRAR COMO ANALISTAS DE DATOS DEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
#print(dataFrameAsistencia['estado'].unique())
#print(dataFrameAsistencia['estrato'].unique())
#print(dataFrameAsistencia['medio_transporte'].unique())


#FILTROS Y CONDICIONES PARA TRANSOFRMAR DATOS
#1. Reportar todos los estudiantes que asistieron
estudiantesQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')
#2. Reportar todos los estudiantes que faltaron
estudiantesQueFaltaron=dataFrameAsistencia.query('estado=="inasistencia"')
#3. Reportar todos los estudiantes que llegaron tarde(Justificado)
estudiantesConFaltaJustificada=dataFrameAsistencia.query('estado=="justificado"')
#4. Reportar todos los estudiantes de estrato 1
estudiantesEstratoUno=dataFrameAsistencia.query('estrato==1')
#5. Reportar todos los estudiantes de estratos altos
estudiantesEstratosAltos=dataFrameAsistencia.query('estrato>3')
#6. Reportar todos los estudaintes que llegan en metro
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')
#7. Reportar todos los estudaintes que llegan en bicicleta
estudiantesLleganBicicleta=dataFrameAsistencia.query('medio_transporte=="bicicleta"')
#8. Reportar todos los estudiantes que no caminan para llegar a la u
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')
#9. Reportar todos los registros de asistencia del mes de junio
registroAsistenciaJunio=dataFrameAsistencia.query("fecha.str.contains('2025-06', case=False, na=False)", engine='python')


#10. Reportar los estudaintes que faltaron y usan bus para llegar a la u
estudiantesQueFaltanUsanBus=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="bus"')
#11. Reportar estudiantes que usan bus y son de estratos altos
estudiantesEstratoAltoUsanBus=dataFrameAsistencia.query('estrato > 3 and medio_transporte=="bus"')
#12. Reportar estudiantes que usan bus y son de estratos bajos
estudiantesEstratoBajoUsanBus=dataFrameAsistencia.query('estrato < 4 and medio_transporte=="bus"')
#13. Reportar estudiantes que llegan tarde y son de estrato 3,4,5 o 6
estudiantesLleganTardeEnEstratosMayorDos=dataFrameAsistencia.query('estrato>2 and estado=="justificado"')
#14. Reportar estudiantes que usan transportes ecologicos 
estudiantesUsanTransporteEcologico=dataFrameAsistencia.query('medio_transporte=="a pie" or medio_transporte == "bicicleta"')
#15. Reportar estudiantes que faltan y usan carro para transportarse
estudiantesFaltaronUsanCarro=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="carro"')
#16. Reportar estudiantes que asisten son estratos altos y caminan
estudiantesAsistieronEstratosAltosYCaminan=dataFrameAsistencia.query('estrato>3 and estado=="asistio" and medio_transporte=="a pie"')
#17. Reportar estudiantes que son estratos bajos y justifican su iniasistencia
estudiantesEstratosBajosJustifican=dataFrameAsistencia.query('estrato<3 and estado=="justificado"')
#18. Reportar estudiantes que son estratos altos y justifican su iniasistencia
estudiantesEstratosBajosJustifican=dataFrameAsistencia.query('estrato<3 and estado=="justificado"')
#19. Reportar estudiantes que usan carro y justifican su inasistencia
estudiantesJustificadosQueUsanCarro=dataFrameAsistencia.query('estado=="justificado" and medio_transporte=="carro"')
#20. Reportar estudiantes que faltan y usan metro y son estratos medios
estudiantesEstratosMediosQueUsanMetroYFaltan=dataFrameAsistencia.query('estrato==3 and estado=="inasistencia" and medio_transporte=="metro"')


#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. Contar cada registro de asistencia por cada estado
conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()

#2. Numero de registros por estrato
conteoRegistrosPorEstrato=dataFrameAsistencia.groupby('estrato').size()

#3. Cantidad de estudiantes por medio de transporte
conteoEstudiantesPorTransporte=dataFrameAsistencia.groupby('medio_transporte').size()

#4. Cantidad de registros por grupo
conteoRegistrosGrupo=dataFrameAsistencia.groupby('id_grupo').size()

#5. Cruce entre estado y medio de transporte
cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()

#6. Promedio de estrato por estado de asistencia
promedioEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()

#7. Estrato promedio por medio de transporte
estratoPromedioPorTransporte=dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean()

#8. Maximo estrato por estado de asistencia
maximoEstratoPorAsistencia=dataFrameAsistencia.groupby('estado')['estrato'].max()

#9. Minimo estrato por estado de asistencia
minimoEstratoPorAsistencia=dataFrameAsistencia.groupby('estado')['estrato'].min()

#10.Conteo de asistencias por grupo y por estado
conteoAsistenciaPorGrupoYEstado=dataFrameAsistencia.groupby(['id_grupo','estado']).size()

#11. Transporte usado por cada grupo
transporteUsadoPorCadaGrupo=dataFrameAsistencia.groupby(['id_grupo','medio_transporte']).size()

#12. cuantos grupos distintos registraron asistencia por fecha
gruposPorFecha=dataFrameAsistencia.groupby(['id_grupo','fecha']).size()

#13. Promedio de estrato por fecha
estratoPromedioPorFecha=dataFrameAsistencia.groupby('fecha')['estrato'].mean()

#14. Numero de tipos de estado por transporte
conteoEstadosPorTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()

#15. Primer Registro de cada grupo
primerRegistroPorGrupo=dataFrameAsistencia.groupby('id_grupo').first()
