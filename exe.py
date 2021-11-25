
import cx_Freeze
executables = [cx_Freeze.Executable(
    script="jogo.py", icon="imagens/logo.ico"
)]
cx_Freeze.setup(
    name='Peaky Blinders',
    options={"build_exe":{"packages":["pygame"],
    "include_files":["imagens"]}},
    executables=executables
    )