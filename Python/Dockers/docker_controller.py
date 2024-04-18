import docker
from threading import Lock


class DockerController:
    client = docker.from_env()
    containers = dict()
    lock = Lock()

    @classmethod
    def turn_on(cls, container_name: str) -> bool:
        """Starts a Docker container by name, unless it's already running."""
        with cls.lock:
            if container_name in cls.containers:
                return False
    
            # Inspect the image to find out the exposed ports
            image = cls.client.images.get(container_name)
            ports = image.attrs['Config']['ExposedPorts']
            
            # Setup port mappings - map each exposed port to the same port on the host
            port_bindings = {port: int(port.split('/')[0]) for port in ports}
            try:
                # Attempt to run the container
                container = cls.client.containers.run(
                    container_name,
                    detach=True,
                    # Ensure port mappings are specific to the container if needed
                    ports=port_bindings
                )
            except docker.errors.ContainerError as e:
                return False

            # Successfully started the container
            if container:
                cls.containers[container_name] = container
                return True
            else:
                return False

    @classmethod
    def turn_off(cls, container_name: str):
        container = cls.containers.get(container_name)
        if not container:
            return False
        # container.stop()
        container.remove(force=True)
        with cls.lock:
            cls.containers.pop(container_name)
        return True

    @classmethod
    def turn_off_all(cls):
        for container_name in cls.containers.copy():
            cls.turn_off(container_name)
