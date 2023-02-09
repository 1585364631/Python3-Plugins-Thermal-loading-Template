import os


class Platform:
    def __init__(self):
        self.plugins = []
        self.loadPlugins()

    @staticmethod
    def pluginStart(from_):
        print("读取插件 %s." % from_)

    @staticmethod
    def pluginStop(from_):
        print("结束插件 %s." % from_)

    @staticmethod
    def pluginNotRun(from_):
        print("插件已禁用 %s." % from_)

    @staticmethod
    def pluginRun(from_):
        print("插件已启用 %s." % from_)

    # 重新加载插件
    def reload(self):
        self.plugins = []
        self.loadPlugins()

    # 加载插件文件夹
    def loadPlugins(self):
        for filename in os.listdir("plugins"):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue
            self.runPlugin(filename)

    # 读取插件数据
    def runPlugin(self, filename):
        pluginName = os.path.splitext(filename)[0]
        plugin = __import__("plugins." + pluginName, fromlist=[pluginName])
        clazz = plugin.getPluginClass()
        o = clazz()
        o.setPlatform(self)
        o.start()
        # 插件启动状态
        if o.status:
            self.plugins.append(o)
            o.inRun()
        else:
            o.notRun()
            o.setPlatform(None)

    # 结束所有插件
    def shutdown(self):
        for o in self.plugins:
            o.stop()
            o.setPlatform(None)
        self.plugins = []


if __name__ == "__main__":
    platform = Platform()
    platform.shutdown()
