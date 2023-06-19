import subprocess
import pkg_resources

packages = [dist.project_name for dist in pkg_resources.working_set]
subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y"] + packages)
