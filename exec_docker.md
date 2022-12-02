1. Vais a diretória onde esta o código no terminal
2. Crias uma imagem do server utilizando o seguinte comando : docker build --tag <um nome qualquer> .
3. Crias um container dessa image: docker run <nome que desta a imagem>

Comandos importantes:
    "docker images": consegues ver as imagens que criastes e as suas informações

    "docker rmi <id da imagem>": elimina essa imagem (as imagens, a imagem do nosso server ocupa quase 1.5 GB), tens que elimiar os container criados desta imagem para elimina-la. Há algumas que tens que forçar a eliminação com "-f" em frente de rmi

    "docker ps": server para ver os container criados e activos, entre outras informações

    "docker ps -a": server para ver todos os containers, independentemente de que estos estejam parados

    "docker rm <nome do container>": eliminar container, mas primeiro este deve estar parado
    
    "docker stop <nome do container>": para um container
