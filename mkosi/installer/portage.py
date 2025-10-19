from pathlib import Path
from mkosi.config import Config
from mkosi.context import Context
from mkosi.installer import PackageManager
from mkosi.util import PathString


class Portage(PackageManager):
    @classmethod
    def executable(cls, config: Config) -> str:
        return "emerge"
    @classmethod
    def subdir(cls, config: Config) -> Path:
        return Path("/etc/portage")
    @classmethod
    def package_subdirs(cls, cache: Path) -> list[tuple[Path, Path]]:
        return super().package_subdirs(cache)
    @classmethod
    def scripts(cls, context: Context) -> dict[str, list[PathString]]:
        return {
            "emerge": cls.apivfs_script_cmd(context) + cls.env_cmd(context) + cls.env_cmd(context),
            "mkosi-install": ["emerge", "-v", "--with-bdeps=y"],
            "mkosi-upgrade": ["emerge", "vuDN", "--with-bdeps=y", "@world"],
            "mkosi-remove": ["emerge", "--depclean"]
        }
    @classmethod
    def setup(cls, )