import subprocess

from .config import API_HOST

__all__ = ['update_api']

def update_api():
    compose_file = API_HOST / 'docker' / 'docker-compose.yml'

    subprocess.run(
        [
            "docker", "compose", "-f",
            str(compose_file),
            "exec", "-T",
            "api",
            "python", "manage.py", "atualizar_sorteios"
        ],
        cwd=API_HOST,
        check=True
    )
