class Plugin1:
    # 插件启动状态
    status = True
    # 插件名
    pluginName = "plugin1"

    def __init__(self):
        self.platform = None

    def setPlatform(self, platform):
        self.platform = platform

    def start(self):
        self.platform.pluginStart(self.pluginName)

    def stop(self):
        self.platform.pluginStop(self.pluginName)

    def notRun(self):
        self.platform.pluginNotRun(self.pluginName)

    def inRun(self):
        self.platform.pluginRun(self.pluginName)


def getPluginClass():
    return Plugin1
