def programas_ordenados(solicitud):
    query = solicitud.programas.all()
    result = []

    for x in query:
        index = -1
        band = True
        periodo_format = '{}-{}'.format(x.periodo_electivo, x.periodo_annio)
        for y in result and band:
            index += 1
            if y.periodo == periodo_format:
                band = False


        if index < 0:

            result.append({
                'periodo' : periodo_format,
                'materias' : [x.codigo_materia],
            })

        else:
            result[index].materias.append(x.codigo_materia)

    return result
