
# ¿Para qué es?

Estas recetas permiten configurar el usuario y credenciales de pulumi para administrar la infraestructura del proyecto.

## Requisitos

* Ansible instalado
* Pulumi Token generado
* Credenciales de seguridad a la cuenta de AWS

## Resultado

* __01_prepare.yml:__ Esta receta se encarga de crear el usuario local
* __02_pulumi.yml:__ Esta receta se encarga de encriptar/desencriptar el token de pulumi

## Pasos

1. Ejecutar el playbook para crear el usuario:
    * `ansible-playbook 01_prepare.yml --extra-vars "LOCALUSER=$(whoami)"`
2. Iniciamos session como usuario nuevo
    * `sudo su - infra-andra-portfolio`
3. Nos ubicamos en la carpeta del repositorio en la terminal:
   * `cd /home/<USER>/<INFRASTRUCTURE_REPOSITORY_PATH>`
4. Ejecutamos la receta para encriptar el token de pulumi:
   * `ansible-playbook 02_encrypt_pulumi_token.yml -i inventory`
5. Copiamos el token de pulumi encriptado y lo pegamos en el archivo vars.yml
6. Ejecutamos la receta para desencriptar el token de pulumi:
   * `ansible-playbook 03_decrypt_pulumi_token.yml -i inventory`
7. Copiamos el token de pulumi y lo ingresamos al momento de hacer el pulumi login.
