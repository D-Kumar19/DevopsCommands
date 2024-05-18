# Docker Commands Cheat Sheet 📄

Welcome to the Docker Commands Cheat Sheet! This guide will help you understand and quickly access some of the most commonly used Docker commands. Docker commands are categorized into starting commands, help commands, and other useful commands to manage your Docker environment efficiently.

## Docker Starting Commands 🚀

These commands are essential for getting started with Docker, checking the status, and managing Docker images and containers.

| Command                           | Description                                                                                                                                                                      |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker`                          | Displays a list of available Docker commands.                                                                                                                                    |
| `docker info`                     | Displays system-wide information about Docker.                                                                                                                                   |
| `docker version`                  | Displays the Docker version information.                                                                                                                                         |
| `docker -v`                       | Displays the Docker version number.                                                                                                                                              |
| `docker images`                   | Lists all the Docker images on the local machine. We can also use `docker image ls`.                                                                                             |
| `docker ps`                       | Lists all the running Docker containers.                                                                                                                                         |
|                                   | **Examples:**                                                                                                                                                                    |
|                                   | `docker ps -a` - Lists all containers, including stopped ones.                                                                                                                   |
|                                   | `docker ps -q` - Lists only the container IDs.                                                                                                                                   |
| `docker system df`                |  It displays information about the amount of disk space used by Docker.                                                                                                          |
| `systemctl start docker.service`  | Starts the Docker service (Linux).                                                                                                                                               |
| `systemctl status docker.service` | Checks the status of the Docker service (Linux).                                                                                                                                 |

## Help Commands 🆘

These commands provide help and detailed usage information for Docker commands.

| Command                   | Description                                                                                                                                                                              |
|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker <command> --help` | Displays help information for a specific Docker command.                                                                                                                                 |
|                           | **Examples:**                                                                                                                                                                            |
|                           | `docker ps --help` - Shows help for the `docker ps` command.                                                                                                                             |
|                           | `docker build --help` - Shows help for the `docker build` command.                                                                                                                       |
|                           | `docker pull --help` - Shows help for the `docker pull` command.                                                                                                                         |
|                           | `docker-compose --help` - Shows help for the `docker-compose` command.                                                                                                                   |

## Pulling an Image and Running Your First Container 🚀

This section covers the essential commands for pulling Docker images from a registry and running your first container. These commands help you quickly get started with Docker by using predefined images from Docker Hub or other registries.

### Pulling an Image 🐳

This section covers the command to pull Docker images from a registry. Pulling an image downloads it to your local system so you can use it to create containers.

| Command                                | Description                                                                                                                                                                 |
|:---------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker pull <image_name>:<image_tag>` | Pulls a Docker image from the specified repository with the specified image tag. If image tag not specified then it grabs the latest tagged image.                          |
|                                        | **Examples:**                                                                                                                                                               |
|                                        | `docker pull node` - Pulls the `node` image with the default `latest` tag.                                                                                                  |
|                                        | `docker pull node:latest` - Explicitly pulls the `latest` version of the `node` image.                                                                                      |
|                                        | `docker pull node:22-alpine3.18` - Pulls a specific version of the `node` image.                                                                                            |
|                                        | `docker pull nginx` - Pulls the `nginx` image with the default `latest` tag.                                                                                                |
|                                        | `docker pull nginx:1.23` - Pulls a specific version of the `nginx` image.                                                                                                   |
|                                        | `docker pull mongo` - Pulls the `mongo` image with the default `latest` tag.                                                                                                |

### Running Your First Container 🚀

Once you have pulled an image, you can run it to create a container. This section provides commands to start containers from the downloaded images.

| Command                   | Description                                                                                                                                                                              |
|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run <image_name>` | Runs a Docker container from the specified image.                                                                                                                                        |
|                           | **Examples:**                                                                                                                                                                            |
|                           | `docker run openjdk` - Runs the `openjdk` image (pulls it if not already on the system).                                                                                                 |
|                           | `docker run nginx` - Runs the `nginx` image (works if the tag is `latest`).                                                                                                              |
|                           | `docker run nginx:1.23` - Runs a specific version of the `nginx` image.                                                                                                                  |

**Notes:**

1. When running an image, Docker creates a container. If the container name is not specified, Docker assigns a random name and an ID.
2. After running the container, use `docker ps` and `docker ps -a` to see the running and stopped containers.
3. Containers are designed to perform tasks. If you run an OS image without a task, the container will exit immediately after running.
4. You can specify the object type for each command, such as using `docker container run` instead of `docker run` or `docker container inspect` instead of `docker inspect`. Docker can intelligently determine the intended operation even if you use the shorthand version.
5. Remember that Docker Desktop is not just for installation—it's a powerful tool in its own right. While this command sheet focuses on CLI-based operations, Docker Desktop offers a user-friendly interface for managing your Docker environment. When you pull an image, it automatically appears in Docker Desktop. It also displays running and stopped containers, allowing you to manage them efficiently. You can run images, specify options for containers, start and stop containers, and manage volumes and networks—all through Docker Desktop's interface, just as you would with CLI commands.

## Adding Features to Our Containers ⚙️

This section covers commands to add various features to your running Docker containers. You can run containers in detached mode, map ports, allocate pseudo-TTYs, pass environment variables, and more.

| Command                                             | Description                                                                                                                                                    |
|:----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run -d <image_name>`                        | Runs a container in detached mode.                                                                                                                             |
|                                                     | **Examples:**                                                                                                                                                  |
|                                                     | `docker run -d nginx:1.23` - Runs the `nginx:1.23` image in detached mode.                                                                                     |
|                                                     | `docker run -d node:22-alpine3.18` - Runs the `node:22-alpine3.18` image in detached mode.                                                                     |
| `docker run -p <port>:<port> <image_name>`          | Maps a port on the host to a port in the container.                                                                                                            |
|                                                     | **Examples:**                                                                                                                                                  |
|                                                     | `docker run -p 3000:3000 nginx:1.23` - Maps port 3000 on the host to port 3000 in the container.                                                               |
|                                                     | `docker run -p 50:80 node:22-alpine3.18` - Maps port 50 on the host to port 80 in the container.                                                               |
|                                                     | **Note:** Multiple containers of the same image can run side by side if different ports are used.                                                              |
| `docker run -t <image_name>`                        | Allocates a pseudo-TTY (terminal) for the container.                                                                                                           |
|                                                     | **Examples:**                                                                                                                                                  |
|                                                     | `docker run -t nginx:1.23` - Runs the `nginx:1.23` image with a pseudo-TTY.                                                                                    |
|                                                     | `docker run -t node:22-alpine3.18` - Runs the `node:22-alpine3.18` image with a pseudo-TTY.                                                                    |
| `docker run -i <image_name>`                        | Runs the container in interactive mode.                                                                                                                        |
|                                                     | **Examples:**                                                                                                                                                  |
|                                                     | `docker run -i nginx:1.23` - Runs the `nginx:1.23` image in interactive mode.                                                                                  |
|                                                     | `docker run -i node:22-alpine3.18` - Runs the `node:22-alpine3.18` image in interactive mode.                                                                  |
| `docker run --rm <image_name>`                      | Automatically removes the container when it exits.                                                                                                             |
|                                                     | **Examples:**                                                                                                                                                  |
|                                                     | `docker run --rm nginx:1.23` - Runs the `nginx:1.23` image and removes the container upon exit.                                                                |
|                                                     | `docker run --rm node:22-alpine3.18` - Runs the `node:22-alpine3.18` image and removes the container upon exit.                                                |
| `docker run --name <container_name> <image_name>`   | Assigns a name to the container.                                                                                                                               |
|                                                     | **Examples:**                                                                                                                                                  |
|                                                     | `docker run --name myWebApp nginx:1.23` - Runs the `nginx:1.23` image with the name `myWebApp`.                                                                |
|                                                     | `docker run --name myNodeApp node:22-alpine3.18` - Runs the `node:22-alpine3.18` image with the name `myNodeApp`.                                              |
| `docker run -e <environment_variable> <image_name>` | Passes an environment variable to the container.                                                                                                               |
|                                                     | **Examples:**                                                                                                                                                  |
|                                                     | `docker run -e COLOR=BLUE nginx:1.23` - Runs the `nginx:1.23` image with the `COLOR` environment variable set to `BLUE`.                                       |
|                                                     | `docker run --env PASSWORD=root node:22-alpine3.18` - Runs the `node:22-alpine3.18` image with the `PASSWORD` environment variable set to `root`.              |
|                                                     | **Note:** `-e` and `--env` can both be used to pass environment variables.                                                                                     |
| `docker run <image_name> sleep <number>`            | Runs a container with a sleep command to keep it alive for a specified number of seconds.                                                                      |
|                                                     | **Examples:**                                                                                                                                                  |
|                                                     | `docker run nginx:1.23 sleep 100` - Runs the `nginx:1.23` image and keeps the container alive for 100 seconds.                                                 |
|                                                     | `docker run node:22-alpine3.18 sleep 10` - Runs the `node:22-alpine3.18` image and keeps the container alive for 10 seconds.                                   |
|                                                     | **Note:** This is useful for OS images to prevent the container from exiting immediately.                                                                      |

## Starting and Stopping Containers 🛑▶️

Managing the lifecycle of containers is crucial. This section explains how to start and stop Docker containers using various commands.

### Starting a Container ▶️

The commands in this section are used to start stopped Docker containers. This is useful when you need to restart a container without recreating it.

| Command                                         | Description                                                                                                                                                        |
|:------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker start <container_name>\|<container_id>` | Starts a stopped container.                                                                                                                                        |
|                                                 | **Examples:**                                                                                                                                                      |
|                                                 | `docker start web-app` - Starts the container named `web-app`.                                                                                                     |
|                                                 | `docker start 190124321` - Starts the container with the specified ID `190124321`.                                                                                 |
|                                                 | `docker start myWebApp1 myWebApp2 myWebApp3` - Starts multiple containers specified by their names.                                                                |
|                                                 | `docker start $(docker ps -a -q)` - Starts all containers by getting the container ID of all stopped containers.                                                   |

### Stopping a Container 🛑

When we run a container, it may exit on its own. In such cases, we don't need to do anything. We can also specify `--rm` to automatically remove the container upon exit. If a container blocks the screen, use `CTRL + C` to exit, or open another terminal to stop the container using the commands below.

| Command                                        | Description                                                                                                                                                         |
|:-----------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker stop <container_name>\|<container_id>` | Stops a running container.                                                                                                                                          |
|                                                | **Examples:**                                                                                                                                                       |
|                                                | `docker stop myWebApp` - Stops the container named `myWebApp`.                                                                                                      |
|                                                | `docker stop 190124321` - Stops the container with the specified ID `190124321`.                                                                                    |
|                                                | `docker stop -f myWebApp` - Forces the stop of the container named `myWebApp`.                                                                                      |
|                                                | `docker stop myWebApp1 myWebApp2 myWebApp3` - Stops multiple containers specified by their names.                                                                   |
|                                                | `docker stop $(docker ps -q -f name=myWebApp)` - Stops all containers that match the name `myWebApp`.                                                               |

## Debugging Containers and Images 🐞

This section covers essential commands for debugging Docker containers and images. You will learn how to inspect, view logs, execute commands inside containers, and attach to running containers.

### Using Inspect Command 🔍

The `docker inspect` command provides detailed information about Docker objects, such as containers, images, and volumes.

| Command                         | Description                                                                                                                                                                        |
|:--------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker inspect <container_id>` | Retrieves detailed information about a specific container.                                                                                                                         |
|                                 | **Examples:**                                                                                                                                                                      |
|                                 | `docker inspect myWebApp` - Inspects the container named `myWebApp`.                                                                                                               |
|                                 | `docker inspect 190124321` - Inspects the container with the specified ID `190124321`.                                                                                             |
|                                 | `docker inspect nginx` - Inspects the image named `nginx`.                                                                                                                         |
|                                 | `docker inspect $(docker ps -q -f name=myWebApp)` - Inspects all containers matching the name `myWebApp`.                                                                          |
|                                 | `docker inspect myPrivateStorage` - Inspects the volume named `myPrivateStorage` (Volume is covered later).                                                                        |

### Using Logs Command 📜

The `docker logs` command retrieves logs from a container, which is useful for debugging purposes.

| Command                                          | Description                                                                                             |
|:---------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker logs <container_id>`                     | Retrieves logs from a specific container.                                                               |
|                                                  | **Examples:**                                                                                           |
|                                                  | `docker logs web-app` - Retrieves logs from the container named `web-app`.                               |
|                                                  | `docker logs 190124321` - Retrieves logs from the container with the specified ID `190124321`.            |
|                                                  | `docker logs mongodb \| tail` - Retrieves the last few lines of logs from the `mongodb` container.          |
|                                                  | `docker logs mongodb -f` - Follows the log output from the `mongodb` container.                          |

### Using Exec Command 🖥️

The `docker exec` command runs a new command in a running container. This is useful for debugging and interacting with the container's filesystem or processes.

| Command                                                      | Description                                                                                                                                           |
|:-------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker exec <container_name>\|<container_id> -it /bin/bash` | Opens an interactive terminal in the container using `/bin/bash`.                                                                                     |
|                                                              | **Examples:**                                                                                                                                         |
|                                                              | `docker exec -it myWebApp /bin/bash` - Opens a bash shell in the `myWebApp` container.                                                                |
|                                                              | `docker exec -it myWebApp /bin/sh` - Opens a sh shell in the `myWebApp` container.                                                                    |
|                                                              | `docker exec -it myWebApp bash` - Opens a bash shell in the `myWebApp` container.                                                                     |
|                                                              | `docker exec -it myWebApp sh` - Opens a sh shell in the `myWebApp` container.                                                                         |
|                                                              | `docker exec -it -u root myWebApp bash` - Opens a bash shell as the root user in the `myWebApp` container.                                            |
|                                                              | `docker exec -it myWebApp ls` - Runs the `ls` command in the `myWebApp` container.                                                                    |
|                                                              |`docker exec -it myWebApp env` - Lists the environment variables in the `myWebApp` container.                                                          |
|                                                              |`docker exec -it myWebApp cat /etc/hostname` - Displays the hostname of the `myWebApp` container.                                                      |

**Note:**

- The command `/bin/bash` can be replaced with `bash` or `sh` to match the shell available in the container.
- To check which shell (subsystem) is being used, you can try running the following command inside the container:

  ```sh
  docker exec -it <container_name> sh -c 'echo $0'
  ```

  This will output the shell being used (e.g., `sh` or `bash`).
- Use `exit` to leave the container's shell.

### Using Attach Command 🔗

The `docker attach` command connects to a running container's main process, allowing you to interact with it directly.

| Command                                          | Description                                                                                                                                                       |
|:-------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker attach <container_name>\|<container_id>` | Attaches to a running container.                                                                                                                                  |
|                                                  | **Examples:**                                                                                                                                                     |
|                                                  | `docker attach myWebApp` - Attaches to the container named `myWebApp`.                                                                                            |
|                                                  | `docker attach 190124321` - Attaches to the container with the specified ID `190124321`.                                                                          |

## Removing Containers and Images 🗑️

Managing the cleanup of containers and images is essential to maintain an efficient Docker environment. This section covers commands for removing containers and images, and for pruning unused Docker objects.

### Using `-rm` to Remove Containers 🗑️

The `docker rm` command removes stopped containers. It's useful for cleaning up containers that are no longer needed.

| Command                                      | Description                                                                                                                                                           |
|:---------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker rm <container_name>\|<container_id>` | Removes a stopped container by name or ID.                                                                                                                            |
|                                              | **Examples:**                                                                                                                                                         |
|                                              | `docker rm myWebApp` - Removes the container named `myWebApp`.                                                                                                        |
|                                              | `docker rm 190124321` - Removes the container with the specified ID `190124321`.                                                                                      |
|                                              | `docker rm -f myWebApp` - Forces the removal of the container named `myWebApp`, even if it's running.                                                                 |
|                                              | `docker rm $(docker ps -aq)` - Removes all stopped containers by getting their container ID.                                                                          |
|                                              | `docker rm -f $(docker ps -aq)` - Removes all running and stopped containers by getting their container ID.                                                           |

### Using `rmi` to Remove Images 🗑️

The `docker rmi` command removes one or more images from the local Docker registry.

| Command                   | Description                                                                                                                                                                              |
|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker rmi <image_name>` | Removes an image by name or ID.                                                                                                                                                          |
|                           | **Examples:**                                                                                                                                                                            |
|                           | `docker rmi nginx` - Removes the image named `nginx`.                                                                                                                                    |
|                           | `docker rmi -f nginx` - Forces the removal of the image named `nginx`.                                                                                                                   |
|                           | `docker rmi nginx:1.23` - Forces the removal of the image named `nginx` with tag `1.23`.                                                                                                 |

### Using `prune` to Remove Unused Docker Objects 🧹

The `docker prune` commands remove all unused containers, networks, images, or volumes. This is helpful for freeing up space.

| Command                  | Description                                                                                                                                                                               |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker container prune` | Removes all stopped containers.                                                                                                                                                           |
| `docker image prune`     | Removes unused images.                                                                                                                                                                    |
| `docker volume prune`    | Removes all unused volumes.                                                                                                                                                               |
| `docker network prune`   | Removes all unused networks.                                                                                                                                                              |
| `docker system prune -a` | Removes all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.                                                                                |
|                          | **Warning:** This is a powerful command and should be used with caution as it can remove critical Docker objects.                                                                         |

## Formatting and History 📜

This section covers commands for formatting the output of Docker commands and viewing the history of Docker images.

### Formatting Output 🎨

Docker allows you to format the output of commands to better suit your needs. The `docker ps -f` command can be used to specify a formatter.

| Command                            | Description                                                                                                                                                                     |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker ps -f <specify formatter>` | Filters the output of `docker ps` based on the specified formatter.                                                                                                             |
|                                    | **Examples:**                                                                                                                                                                   |
|                                    | `docker ps -q -f name=myWebApp` - Lists the IDs of containers with the name `myWebApp`.                                                                                         |
|                                    | `docker ps -f status=running` - Lists only running containers.                                                                                                                  |
|                                    | `docker ps -f ancestor=nginx` - Lists containers created from the `nginx` image.                                                                                                |
|                                    | `docker ps -f label=env=production` - Lists containers with the label `env=production`.                                                                                         |

#### Bonus Command

You can define a custom format for the `docker ps` command output using environment variables.

**Linux:**

```sh
export FORMAT="ID\t{{.ID}}\nNAME\t{{.Names}}\nIMAGE\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n"
docker ps --format=$FORMAT
```

**PowerShell:**

```ps
$env:FORMAT = "ID`t{{.ID}}`nNAME`t{{.Names}}`nIMAGE`t{{.Image}}`nPORTS`t{{.Ports}}`nCOMMAND`t{{.Command}}`nCREATED`t{{.CreatedAt}}`nSTATUS`t{{.Status}}`n"
docker ps --format=$env:FORMAT
```

### Viewing Image History 🕰️

The `docker image history` command shows the history of an image, including the commands that were used to create it.

| Command                             | Description                                                                                                                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker image history <image_name>` | Displays the history of a specified image.                                                                                                                                     |
|                                     | **Examples:**                                                                                                                                                                  |
|                                     | `docker image history nginx` - Shows the history of the `nginx` image.                                                                                                         |
|                                     | `docker image history node:latest` - Shows the history of the `node:latest` image.                                                                                             |
|                                     | `docker image history alpine` - Shows the history of the `alpine` image.                                                                                                       |
|                                     | `docker image history my_custom_image` - Shows the history of a custom image named `my_custom_image`.                                                                          |

## Volume in Docker 🗃️

Docker volumes are essential for persisting data and sharing it between containers. This section covers various commands for managing Docker volumes, different types of volumes, and how to use them with examples.

### Docker Volume Commands 📜

These commands help you manage Docker volumes, including listing, inspecting, and creating volumes.

| Command                               | Description                                                                                                                                                                  |
|:--------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker volume --help`                | Displays help information for Docker volume commands.                                                                                                                        |
| `docker volume ls`                    | Lists all Docker volumes on the system.                                                                                                                                      |
| `docker volume ls -qf dangling=true`  | Lists all anonymous (dangling) volumes.                                                                                                                                      |
| `docker volume inspect <volume_name>` | Provides detailed information about a specific volume.                                                                                                                       |
|                                       | **Example:**                                                                                                                                                                 |
|                                       | `docker volume inspect myVolume` - Inspects the volume named `myVolume`.                                                                                                     |
| `docker volume create <volume_name>`  | Creates a new Docker volume with the specified name.                                                                                                                         |
|                                       | **Example:**                                                                                                                                                                 |
|                                       | `docker volume create myVolume` - Creates a volume named `myVolume`.                                                                                                         |
| `docker volume rm <volume_name>`      | Removes a Docker volume.                                                                                                                                                     |
|                                       | **Example:**                                                                                                                                                                 |
|                                       | `docker volume rm myVolume` - Removes the volume named `myVolume`.                                                                                                           |
| `docker volume prune`                 | Removes all unused volumes.                                                                                                                                                  |
|                                       | **Example:**                                                                                                                                                                 |
|                                       | `docker volume prune` - Removes all unused Docker volumes.                                                                                                                   |

### Types of Volumes 📁

Docker supports three types of volumes: anonymous, named, and bind mounts. Each has its specific use cases and advantages.

#### Anonymous Volumes 🔍

Anonymous volumes are created automatically by Docker when you don't specify a volume name.

| Command                                       | Description                                                                                                                                                          |
|:----------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run -v /path/in/container image_name` | Creates an anonymous volume and mounts it to the specified path in the container.                                                                                    |
|                                               | **Example:**                                                                                                                                                         |
|                                               | `docker run -v /data busybox` - Creates an anonymous volume and mounts it to `/data` in the container.                                                               |
| `docker volume ls -qf dangling=true`          | Lists all anonymous (dangling) volumes.                                                                                                                              |

#### Named Volumes 🏷️

Named volumes have a specific name and are easier to reference in different commands.

| Command                                                  | Description                                                                                                                                               |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run -v <volume_name>:<destination> <image_name>` | Creates a named volume and mounts it to the specified path in the container.                                                                              |
|                                                          | **Example:**                                                                                                                                              |
|                                                          | `docker run -v myVolume:/app nginx` - Creates a named volume `myVolume` and mounts it to `/app` in the `nginx` container.                                 |

#### Bind Mounts 📂

Bind mounts map a directory on the host to a directory in the container.

| Command                                                   | Description                                                                                                                                              |
|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run -v "<source>:<destination>" <image_name>`     | Binds a host directory to a container directory.                                                                                                         |
|                                                           | **Examples:**                                                                                                                                            |
|                                                           | `docker run -v "/host/path:/container/path" nginx` - Binds `/host/path` on the host to `/container/path` in the `nginx` container.                       |
|                                                           | `docker run -v "$(pwd):/app" busybox` - Binds the current working directory to `/app` in the `busybox` container.                                        |
| `docker run --volumes-from <container_name> <image_name>` | Shares volumes between containers.                                                                                                                       |
|                                                           | **Example:**                                                                                                                                             |
|                                                           | `docker run --volumes-from webapp busybox` - Runs a `busybox` container and mounts volumes from the `webapp` container.                                  |

### Adding Permissions to Volumes 🔒

You can specify permissions when creating volumes to make them read-only or writable.

| Command                                                                | Description                                                                                                                                 |
|:-----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run -v <volume_name>:<destination>:<permissions> <image_name>` | Creates a volume with specified permissions.                                                                                                |
|                                                                        | **Examples:**                                                                                                                               |
|                                                                        | `docker run -v myVolume:/data:ro nginx` - Creates a read-only volume `myVolume` mounted to `/data` in the `nginx` container.                |
|                                                                        | `docker run -v myVolume:/data:rw nginx` - Creates a read-write volume `myVolume` mounted to `/data` in the `nginx` container.               |

### Using `--mount` Option 🏗️

The `--mount` option provides a more explicit way to define and use volumes.

| Command                                              | Description                                                                                                                                                   |
|:-----------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run --mount type=<type>,source=<source>,target=<destination> <image_name>` | Mounts a volume using the `--mount` option.                                                                                     |
|                                                      | **Examples:**                                                                                                                                                 |
|                                                      | `docker run --mount type=bind,source=/host/path,target=/container/path nginx` - Binds `/host/path` on the host to `/container/path` in the `nginx` container. |
|                                                      | `docker run --mount type=volume,source=myVolume,target=/app busybox` - Mounts the volume `myVolume` to `/app` in the `busybox` container.                     |

### Excluding Directories from Bind Mounts 🚫

When bind mounting, you can exclude certain directories to avoid making the container heavy. Although Docker does not directly support excluding subdirectories within a bind mount, you can achieve this by selectively mounting only the necessary subdirectories.

For example, instead of mounting the entire directory, you can individually mount the subdirectories you need, excluding the unwanted ones:

```sh
docker run -v /host/path/subdir1:/container/path/subdir1 -v /host/path/subdir2:/container/path/subdir2 nginx
```

This mounts `subdir1` and `subdir2` from the host to the container, effectively excluding any other subdirectories in `/host/path`.

### Limiting Memory and CPU Usage 🧠💪

Docker allows you to limit the memory and CPU usage of containers to ensure they do not consume more resources than intended.

#### Limiting Memory Usage 🔒

You can limit the memory usage of a container using the `--memory` flag.

| Command                                           | Description                                                                                                                                                      |
|:--------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run --memory <memory_limit> <image_name>` | Limits the memory usage of the container.                                                                                                                        |
|                                                   | **Examples:**                                                                                                                                                    |
|                                                   | `docker run --memory 512m nginx` - Limits the `nginx` container to use a maximum of 512 MB of memory.                                                            |
|                                                   | `docker run --memory 1g redis` - Limits the `redis` container to use a maximum of 1 GB of memory.                                                                |

#### Limiting CPU Usage 🚫

You can limit the CPU usage of a container using the `--cpus` flag.

| Command                                      | Description                                                                                                                                                           |
|:---------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run --cpus <cpu_limit> <image_name>` | Limits the CPU usage of the container.                                                                                                                                |
|                                              | **Examples:**                                                                                                                                                         |
|                                              | `docker run --cpus 1.5 nginx` - Limits the `nginx` container to use a maximum of 1.5 CPU cores.                                                                       |
|                                              | `docker run --cpus 0.5 alpine` - Limits the `alpine` container to use a maximum of 0.5 CPU cores.                                                                     |

## Docker Network 🌐

Docker networking allows containers to communicate with each other and with external systems. It is crucial for setting up multi-container applications, enabling service discovery, and ensuring containers can access necessary resources.

### Docker Network Commands 📜

These commands help you manage Docker networks, including listing, inspecting, and creating networks.

| Command                                 | Description                                                                                                                                                                |
|:----------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker network --help`                 | Displays help information for Docker network commands.                                                                                                                     |
| `docker network ls`                     | Lists all Docker networks on the system.                                                                                                                                   |
| `docker network inspect <network_name>` | Provides detailed information about a specific network.                                                                                                                    |
|                                         | **Example:**                                                                                                                                                               |
|                                         | `docker network inspect myNetwork` - Inspects the network named `myNetwork`.                                                                                               |
| `docker network prune`                  | Removes all unused networks.                                                                                                                                               |
|                                         | **Example:**                                                                                                                                                               |
|                                         | `docker network prune` - Removes all unused Docker networks.                                                                                                               |
| `docker network create <network_name>`  | Creates a new Docker network with the specified name.                                                                                                                      |
|                                         | **Example:**                                                                                                                                                               |
|                                         | `docker network create myNetwork` - Creates a network named `myNetwork`.                                                                                                   |
| `docker network rm <volume_name>`       | Removes a Docker network.                                                                                                                                                  |
|                                         | **Example:**                                                                                                                                                               |
|                                         | `docker network rm myNetwork` - Removes the network named `myNetwork`.                                                                                                     |

### Types of Networks 🕸️

Docker supports different types of networks, each serving specific purposes:

#### Null Network 🚫

The null network type provides no network isolation or connectivity. Containers run without any network interfaces.

| Command                                  | Description                                                                                                                                                               |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run --network=none <image_name>` | Runs a container with no network connectivity.                                                                                                                            |
|                                          | **Example:**                                                                                                                                                              |
|                                          | `docker run --network=none busybox` - Runs the `busybox` container with no network.                                                                                       |

#### Host Network 🏠

The host network type removes network isolation between the Docker host and the containers, allowing them to share the host's network stack.

| Command                                  | Description                                                                                                                                                               |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run --network=host <image_name>` | Runs a container on the host's network stack.                                                                                                                             |
|                                          | **Example:**                                                                                                                                                              |
|                                          | `docker run --network=host nginx` - Runs the `nginx` container on the host's network.                                                                                     |

#### Bridge Network 🌉

The bridge network type creates a private internal network on the Docker host. Containers on the same bridge network can communicate with each other.

| Command                                    | Description                                                                                                                                                             |
|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run --network=bridge <image_name>` | Runs a container on the default bridge network.                                                                                                                         |
|                                            | **Example:**                                                                                                                                                            |
|                                            | `docker run --network=bridge alpine` - Runs the `alpine` container on the default bridge network.                                                                       |

### Bonus: Connecting Containers 🏗️

When running multiple containers that need to communicate, they must be on the same network. Here’s an example of running two containers and connecting them.

#### Without Docker Network

1. **Run the first container:**

   ```sh
   docker run -d --name db-container -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password mongo
   ```

2. **Get the IP address of the first container:**

   ```sh
   docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db-container
   ```

3. **Run the second container with the IP address of the first container:**

   ```sh
   docker run -d --name mongo-express --network my-network -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=password -e ME_CONFIG_MONGODB_SERVER=<db-container-ip> mongo-express
   ```

**Drawback:** If the first container stops and restarts, it might get a different IP address, breaking the connection.

#### With Docker Network

1. **Create a custom network:**

   ```sh
   docker network create my-network
   ```

2. **Run the first container on the custom network:**

   ```sh
   docker run -d --name mongodb --network my-network -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password mongo
   ```

3. **Run the second container on the custom network, using the name of the first container:**

   ```sh
   docker run -d --name mongo-express --network my-network -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=password -e ME_CONFIG_MONGODB_SERVER=mongodb mongo-express
   ```

**Advantage:** By using the network and naming the containers, you ensure they can always communicate by name, avoiding issues with dynamic IP addresses.

## Docker Compose 📋

Docker Compose is a tool that simplifies the process of defining and running multi-container Docker applications. Using a `docker-compose.yml` file, you can specify your application's services, networks, and volumes in a simple, readable format.

### Docker Compose Command Help 🆘

The `docker-compose --help` command displays a list of available commands and options for Docker Compose.

**Example:**

```sh
docker-compose --help
```

This command provides detailed usage information and available commands for managing Docker Compose files and services.

### What is Docker Compose and What is the Problem with Usual Commands? 🤔

Docker Compose allows you to define multi-container applications with all their dependencies in a single file (`docker-compose.yml`). This simplifies the process of starting, stopping, and managing multiple containers as a single unit.

**Problems with usual commands:**

- **Complexity:** Managing multiple containers with individual `docker run` commands can become complex and error-prone.
- **Scalability:** Scaling services up or down requires manually starting or stopping containers.
- **Reproducibility:** Ensuring consistent configurations across different environments can be challenging.

### Example of a Simple Docker Compose File 📝

Here is an example of a `docker-compose.yml` file with a single service, specifying environment variables, ports, container name, volumes, and network.

```yaml
version: '3'
services:
  web:
    image: nginx:latest
    container_name: web_container
    ports:
      - "8080:80"
    environment:
      - NGINX_HOST=localhost
      - NGINX_PORT=80
    volumes:
      - web_data:/usr/share/nginx/html
    networks:
      - webnet

volumes:
  web_data:

networks:
  webnet:
```

### Example of a Complex Docker Compose File 🏗️

Here is an example of a more complex `docker-compose.yml` file with five services. Three services are built from Dockerfiles, and two are pulled from Docker Hub. This example includes frontend and backend components, specifying container names, build contexts, images, ports, volumes, and networks.

```yaml
version: '3'
services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: frontend_container
    ports:
      - "3000:3000"
    volumes:
      - frontend_data:/app
    networks:
      - appnet

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: backend_container
    ports:
      - "5000:5000"
    volumes:
      - backend_data:/app
    networks:
      - appnet

  database:
    image: postgres:latest
    container_name: db_container
    environment:
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=admin
      - POSTGRES_DB=mydb
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - appnet

  cache:
    image: redis:latest
    container_name: cache_container
    ports:
      - "6379:6379"
    networks:
      - appnet

  proxy:
    build:
      context: ./proxy
      dockerfile: Dockerfile
    container_name: proxy_container
    ports:
      - "80:80"
    networks:
      - appnet

volumes:
  frontend_data:
  backend_data:
  db_data:

networks:
  appnet:
```

### Docker Compose Commands 💻

Here are some useful Docker Compose commands with descriptions and examples.

Sure, here is the sorted table:

| Command                                  | Description                                                                                                                                                               |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker-compose up`                      | Starts all the services defined in the `docker-compose.yml` file.                                                                                                         |
| `docker-compose up -d`                   | Starts all services in detached mode.                                                                                                                                     |
| `docker-compose up --build -d`           | Builds images before starting the containers in detached mode.                                                                                                            |
| `docker-compose -f <file_name> up`       | Uses a specific Compose file to start services.                                                                                                                           |
|                                          | **Example:**                                                                                                                                                              |
|                                          | `docker-compose -f custom-compose.yml up` - Starts services using `custom-compose.yml`.                                                                                   |
| `docker-compose build`                   | Builds or rebuilds the services.                                                                                                                                          |
| `docker-compose build --no-cache`        | Builds images without using cache.                                                                                                                                        |
| `docker-compose ps`                      | Lists the status of all containers.                                                                                                                                       |
| `docker-compose logs`                    | Displays logs from all services.                                                                                                                                          |
| `docker-compose logs -f`                 | Follows the log output.                                                                                                                                                   |
| `docker-compose exec <service> <command>`| Executes a command in a running service container.                                                                                                                        |
|                                          | **Example:**                                                                                                                                                              |
|                                          | `docker-compose exec web_container sh` - Opens a shell in the `web_container` service.                                                                                    |
| `docker-compose pause`                   | Pauses all services.                                                                                                                                                      |
| `docker-compose unpause`                 | Unpauses all services.                                                                                                                                                    |
| `docker-compose stop`                    | Stops all running services.                                                                                                                                               |
| `docker-compose restart`                 | Restarts all services.                                                                                                                                                    |
| `docker-compose restart <service>`       | Restarts a specific service.                                                                                                                                              |
|                                          | **Example:**                                                                                                                                                              |
|                                          | `docker-compose restart web_container` - Restarts the `web_container` service.                                                                                            |
| `docker-compose down`                    | Stops and removes containers, networks, volumes, and images created by `up`.                                                                                              |
| `docker-compose down -rmi all -v`        | Removes all images and volumes.                                                                                                                                           |
| `docker-compose -f <file_name> down`     | Uses a specific Compose file to stop services.                                                                                                                            |
|                                          | **Example:**                                                                                                                                                              |
|                                          | `docker-compose -f custom-compose.yml down` - Stops services using `custom-compose.yml`.                                                                                  |
| `docker-compose run <service> <command>` | Runs a one-off command on a service.                                                                                                                                      |
|                                          | **Example:**                                                                                                                                                              |
|                                          | `docker-compose run web_container echo "Hello, World!"` - Runs the command `echo "Hello, World!"` in the `web_container` service.                                         |
| `docker-compose rm`                      | Removes stopped service containers.                                                                                                                                       |
| `docker-compose rm -f`                   | Forces the removal of stopped service containers.                                                                                                                         |
| `docker-compose pull`                    | Pulls service images from the registry.                                                                                                                                   |
| `docker-compose top`                     | Displays the running processes of the services.                                                                                                                           |
| `docker-compose config`                  | Validates and views the Compose file configuration.                                                                                                                       |

## Building Your Own Image 🏗️

Creating your own Docker images allows you to customize and optimize your application environment. This section covers essential configurations for writing a Dockerfile and explains how to build an image from it.

### Dockerfile Configurations 📝

Here are the main instructions you can use in a Dockerfile, along with examples:

| Instruction  | Description                                                                                                                                                                                           |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FROM`       | Specifies the base image to use for the Docker image.                                                                                                                                                 |
|              | **Example:**                                                                                                                                                                                          |
|              | `FROM ubuntu:20.04` - Uses the `ubuntu:20.04` image as the base image.                                                                                                                                |
| `WORKDIR`    | Sets the working directory inside the Docker image.                                                                                                                                                   |
|              | **Example:**                                                                                                                                                                                          |
|              | `WORKDIR /app` - Sets `/app` as the working directory inside the image.                                                                                                                               |
| `COPY`       | Copies files or directories from the host to the Docker image.                                                                                                                                        |
|              | **Example:**                                                                                                                                                                                          |
|              | `COPY . /app` - Copies the current directory contents to `/app` in the image.                                                                                                                         |
| `ADD`        | Similar to `COPY`, but also supports remote URLs and unpacking archives.                                                                                                                              |
|              | **Example:**                                                                                                                                                                                          |
|              | `ADD https://example.com/file.tar.gz /app/` - Downloads and extracts a file from a URL to `/app/`.                                                                                                    |
| `RUN`        | Executes a command in the Docker image during the build process.                                                                                                                                      |
|              | **Example:**                                                                                                                                                                                          |
|              | `RUN apt-get update && apt-get install -y nodejs` - Updates the package list and installs Node.js.                                                                                                    |
| `EXPOSE`     | Informs Docker that the container listens on the specified network ports at runtime.                                                                                                                  |
|              | **Example:**                                                                                                                                                                                          |
|              | `EXPOSE 8080` - Exposes port 8080 for the container.                                                                                                                                                  |
| `CMD`        | Specifies the default command to run when a container is started.                                                                                                                                     |
|              | **Example:**                                                                                                                                                                                          |
|              | `CMD ["node", "app.js"]` - Runs `node app.js` by default when the container starts.                                                                                                                   |
| `ENV`        | Sets environment variables in the Docker image.                                                                                                                                                       |
|              | **Example:**                                                                                                                                                                                          |
|              | `ENV NODE_ENV=production` - Sets the `NODE_ENV` environment variable to `production`.                                                                                                                 |
| `ENTRYPOINT` | Configures a container that will run as an executable.                                                                                                                                                |
|              | **Example:**                                                                                                                                                                                          |
|              | `ENTRYPOINT ["node", "app.js"]` - Sets `node app.js` as the command to run.                                                                                                                           |
| `USER`       | Sets the user name or UID to use when running the image.                                                                                                                                              |
|              | **Examples:**                                                                                                                                                                                         |
|              | `USER appuser` - Sets the user to `appuser`.                                                                                                                                                          |
|              | `USER root` - Sets the user to `root`.                                                                                                                                                                |
|              | `USER 1001` - Sets the user to the user with UID 1001.                                                                                                                                                |

**Note:** CMD, RUN, and ENTRYPOINT may seem similar but they serve different purposes:

- **CMD:** Provides default arguments for ENTRYPOINT. If ENTRYPOINT is not specified, CMD will be executed as the default command. It can be overridden by arguments provided to `docker run`.
- **RUN:** Executes commands during the image build process and creates layers in the image. It's used to install software packages or perform other tasks needed to set up the image.
- **ENTRYPOINT:** Configures a container to run as an executable. It sets the main command and parameters that cannot be overridden by `docker run` command arguments. However, CMD can be used to provide additional default arguments to ENTRYPOINT. For example ENTRYPOINT is set as sleep and when we want to run the image we can provide the number as a parameter. However, if you don't provide it then the run will fail. Therefore, a default parameter can be set for this with CMD and if user doesn't provide the value it will be taken from CMD.

### Building an Image 🔨

After writing your Dockerfile, you can build an image using the `docker build` command.

| Command                          | Description                                                                                                                                                                       |
|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker build .`                 | Builds an image from the Dockerfile in the current directory.                                                                                                                     |
|                                  | **Example:**                                                                                                                                                                      |
|                                  | `docker build .` - Creates an image with `<none>` as the name and `<none>` as the tag.                                                                                            |
| `docker build -t <name> .`       | Builds an image with a specified name.                                                                                                                                            |
|                                  | **Example:**                                                                                                                                                                      |
|                                  | `docker build -t node-app .` - By default, the `latest` tag will be used.                                                                                                         |
| `docker build -t <name>:<tag> .` | Builds an image with a specified name and tag.                                                                                                                                    |
|                                  | **Example:**                                                                                                                                                                      |
|                                  | `docker build -t node-app:1.0 .` - Creates an image named `node-app` with the tag `1.0`.                                                                                          |

**Note:** Docker images are read-only. If you make changes to your project after creating the image, you need to rebuild the image to incorporate those changes.

### Running Your Custom Image 🚀

After creating the image, you can run it the same way as other pulled images:

| Command                                                            | Description                                                                                                                                     |
|:-------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker run -d -p <host_port>:<container_port> <image_name>:<tag>` | Runs a container from the created image.                                                                                                        |
|                                                                    | **Example:**                                                                                                                                    |
|                                                                    | `docker run -d -p 8080:8080 node-app:1.0` - Runs the `node-app:1.0` image, mapping port 8080.                                                   |

## Pulling and Pushing Your Own Image to Registries 🌍

After creating your own image, you can push it to a registry for others to use, such as a test team for testing purposes.

### Tagging, Pushing, and Pulling Images 🏷️📥🚀

To push an image, you need to tag it with your username and repository name.

| Command                                                  | Description                                                                                                                                               |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `docker tag <old_name> <username>/<new_name>:<tag_name>` | Tags an image with a new name and tag for the registry.                                                                                                   |
|                                                          | **Example:**                                                                                                                                              |
|                                                          | `docker tag node-app:1.0 username/node-app:1.0` - Tags the image `node-app:1.0` for the registry.                                                         |
| `docker push <username>/<image_name>:<tag_name>`         | Pushes the tagged image to the specified registry.                                                                                                        |
|                                                          | **Example:**                                                                                                                                              |
|                                                          | `docker push username/node-app:1.0` - Pushes the `node-app:1.0` image to the registry.                                                                    |
| `docker pull <username>/<image_name>:<tag_name>`         | Pulls the image from the specified registry.                                                                                                              |
|                                                          | **Example:**                                                                                                                                              |
|                                                          | `docker pull username/node-app:1.0` - Pulls the `node-app:1.0` image from the registry.                                                                   |
