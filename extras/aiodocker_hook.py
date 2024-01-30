def hook_aiodocker():
    from aiodocker.containers import DockerContainer

    def name(container: DockerContainer) -> str:
        names = container._container.get("Names")
        if len(names) == 0:
            return ""

        return names[0].replace("/", "")

    def state(container):
        state_: str | dict = container._container.get("State")
        if type(state_) == str:
            return state_
        else:
            return state_.get("Status")

    def status(container):
        return container._container.get("Status")

    DockerContainer.name = property(name)
    DockerContainer.state = property(state)
    DockerContainer.status = property(status)
