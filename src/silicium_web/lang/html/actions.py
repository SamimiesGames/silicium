from silicium import AbstractAction


HTML_ACTION_EVENTS = [
    "onclick", "hover"
]


class Action(AbstractAction):
    def __init__(self, function: staticmethod):
        self.function = function
        self.on_deploy()

    def on_trigger(self):
        ...

    def on_deploy(self):
        assert self.function.__name__ in HTML_ACTION_EVENTS

    def __call__(self, *args, **kwargs):
        self.on_trigger()
        return self.function(*args, **kwargs)
