

body = ['   Ö', '   Ö\n|         |', ' \.Ö\n|         |', ' \.Ö./\n|         |',
        ' \.Ö./\n|         |\n|       ./', ' \.Ö./\n|         |\n|       ./ \.']
body_erros = ['']


def mount_body(erros: int) -> str:
    if 0 < erros < 2:
        body_erros[0] = body[erros-1]
    if 1 < erros < 3:
        body_erros[0] = body[erros-1]
    if 2 < erros < 4:
        body_erros[0] = body[erros-1]
    if 3 < erros < 5:
        body_erros[0] = body[erros-1]
    if 4 < erros < 6:
        body_erros[0] = body[erros-1]
    if 5 < erros < 7:
        body_erros[0] = (body[erros-1])
    return str(body_erros[0])
