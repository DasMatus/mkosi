from mkosi.config import Config
from mkosi.distribution import Distribution, DistributionInstaller, PackageType
from mkosi.installer import portage


class Installer(DistributionInstaller, distribution=Distribution):
    @classmethod
    def pretty_name(cls) -> str:
        return super().pretty_name()
    @classmethod
    def filesystem(cls) -> str:
        return super().filesystem()
    @classmethod
    def package_type(cls) -> PackageType:
        return super().package_type()
    @classmethod
    def default_release(cls) -> str:
        return super().default_release()
    @classmethod
    def package_manager(cls, config: "Config") -> type[portage.Portage]:
        return portage.Portage