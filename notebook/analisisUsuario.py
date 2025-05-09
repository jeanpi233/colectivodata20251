import pandas as pd

dataFrameUsuario = pd.read_excel("./data/usuarios_sistema_completo.xlsx")

#1. Solo estudiantes
soloEstudiantes=dataFrameUsuario.query('tipo_usuario=="estudiante"')
#2. Solo profesores
soloProfesores=dataFrameUsuario.query('tipo_usuario=="docente"')
#3. Todos excepto estudiantes
exceptoEstudiantes=dataFrameUsuario.query('tipo_usuario!="estudiante"')
#4. Filtrar por especialidad
filtroEspecialidad=dataFrameUsuario.query('especialidad=="Ingenieria Civil"')
#5. Excluir una especialidad
excluirEspecialidad=dataFrameUsuario.query('especialidad!="Ingenieria Civil"')
#6. Excluir administrativos
excluirAdministrativos=dataFrameUsuario.query('especialidad!="Administrativo"')
#7. Direcciones en medellin
filtroMedellin = dataFrameUsuario.query("direccion.str.contains('medellin', case=False, na=False)", engine='python')
#8. Direcciones terminadas en sur
filtroSur = dataFrameUsuario.query("direccion.str.contains('sur', case=False, na=False)", engine='python')
#9. Direcciones que inician con calle
filtroCalle = dataFrameUsuario.query("direccion.str.match('^Calle(?!jón)', case=False, na=False)", engine='python')
#10.Especialidades que contienen la palabra datos
filtroDatosEspecialidades=dataFrameUsuario.query("especialidad.str.contains('datos', case=False, na=False)", engine='python')
#11. instructores en itagui
instructoresItagui = dataFrameUsuario.query('especialidad=="Instructor"' and "direccion.str.contains('sur', case=False, na=False)"'', engine='python')
#12. nacidos despues de 2000
dataFrameUsuario['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuario['fecha_nacimiento'], errors='coerce')
filtroNacidosDespues2000 = dataFrameUsuario[dataFrameUsuario['fecha_nacimiento'] > '2000-12-31']
#13. nacidos en los 90
filtroNacidos90s = dataFrameUsuario[(dataFrameUsuario['fecha_nacimiento'] >= '1990-01-01') & (dataFrameUsuario['fecha_nacimiento'] <= '1999-12-31')]
#14. direcciones en envigado
filtroEnvigado = dataFrameUsuario.query("direccion.str.contains('envigado', case=False, na=False)", engine='python')
#15. especialdiades que empizan por I
empezarEspecialidadesConI = dataFrameUsuario.query("especialidad.str.match('^I', na=False)", engine='python')
#16. usuarios sin direccion
usuariosSinDireccion = dataFrameUsuario.query("direccion.isna()")
#17. usuarios sin especialidad
usuariosSinEspecialidad = dataFrameUsuario.query("especialidad.isna()")
#18. profesores que viven en sabaneta
profesoresDeSabaneta = dataFrameUsuario.query("direccion.str.contains('sabaneta', case=False, na=False)", engine='python')
#19. aprendices que viven en bello
aprendicesDeBello = dataFrameUsuario.query('tipo_usuario == "aprendiz"' and "direccion.str.contains('bello', case=False, na=False)"'', engine='python')
#20. nacidos en el nuevo milenio
filtroNuevoMilenio = dataFrameUsuario[dataFrameUsuario['fecha_nacimiento'] >= '2000-01-01']


#1. total por tipo
totalePorTipo = dataFrameUsuario.groupby('tipo_usuario').size()
#2. total por especialidad
totalePorEspecialidad = dataFrameUsuario.groupby('especialidad').size()
#3. cantidad de especialidades distintas
cantidadPorEspecialidad = dataFrameUsuario['especialidad'].nunique()
#4. tipos de usuario por especialidad
tipoUsuarioPorEspecialidad = dataFrameUsuario.groupby(['especialidad','tipo_usuario']).size()
#7. primer registro por tipo
primerRegistroPorTipo = dataFrameUsuario.groupby('tipo_usuario').first()
#8. ultimo registro por tipo
ultimoRegistroPorTipo = dataFrameUsuario.groupby('tipo_usuario').last()
#9. combinacion tipo por especialidad
combinacionTipoPorEspecialidad = dataFrameUsuario.groupby(['tipo_usuario', 'especialidad']).size()
#10. el mas viejo por especialidad
dataFrameUsuario = dataFrameUsuario.dropna(subset=['fecha_nacimiento'])
masViejoPorEspecialidad = dataFrameUsuario.loc[dataFrameUsuario.groupby('especialidad')['fecha_nacimiento'].idxmin()]
#11. cuantos de cada especialidad por tipo
cantidadPorEspecialidadPorTipo = dataFrameUsuario.groupby(['tipo_usuario', 'especialidad']).size()
#12. edad promedio por tipo
dataFrameUsuario['edad'] = 2025 - dataFrameUsuario['fecha_nacimiento'].dt.year
edadPromedioPorTipo = dataFrameUsuario.groupby('tipo_usuario')['edad'].mean()
#13. años de nacimeinto mas frecuente por especialidad
añoNacimientoMasFrecuentePorEspecialidad = dataFrameUsuario.groupby('fecha_nacimiento')['especialidad'].mean()
#14. mes de nacimiento mas frecuente por tipo
dataFrameUsuario['mes_nacimiento'] = dataFrameUsuario['fecha_nacimiento'].dt.month_name()
mesNacimientoMasFrecuentePorTipo = dataFrameUsuario.groupby('tipo_usuario')['mes_nacimiento'].value_counts()
#15. UNA CONSULTA O FILTRO QUE UD PROPONGA
#Mostrar estudiantes de guadalajara
estudiantesGuadalara = dataFrameUsuario.query('tipo_usuario == "estudiante"' and "direccion.str.contains('guadalajara', case=False, na=False)"'', engine='python')
print(edadPromedioPorTipo)