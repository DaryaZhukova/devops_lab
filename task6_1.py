import io
import os
import pip
import site
import sys
import yaml


def versions():
    return (
        os.popen("pyenv versions --bare --skip-aliases").read().split())


def virt_env():
    a = []
    sor = "source \"/usr/bin/virtualenvwrapper.sh\""
    hom = "export WORKON_HOME=\"/opt/virtual_env/\""
    for item in os.popen(
            "{0} && {1} && lsvirtualenv".format(sor, hom)):
        if item not in ("\n", "=====\n", "====\n"):
            a.append(item.replace("\n", ""))
    return a


def current_version():
    return os.popen("pyenv version").read()


def packages_instaled():
    return pip.utils.get_installed_distributions()


def site_packages():
    return site.getsitepackages()[0]


def pyth_path():
    a = []
    for item in sys.path:
        a.append(str(item))
    return a


def pip_path():
    for n in sys.path:
        if os.path.isdir("{}{}".format(n, '/pip')):
            return "{}{}".format(n, '/pip')


def python_path():
    return sys.executable


def get_aliases():
    return os.popen("pyenv versions").read()


def write_yaml(mydict):
    with io.open("data.yaml", "w", encoding="utf8") as outfile:
        yaml.dump(mydict, outfile, default_flow_style=False,
                  allow_unicode=True)


def write_json(mydict):
    with open("data.json", "w") as outfile:
        outfile.write(str(mydict))


a = {"Python names and versions": versions(),
     "Python current": current_version(),
     "packages installed": packages_instaled(),
     "site packages": site_packages(), "PYTHONPATH": pyth_path(),
     "pip path": pip_path(),
     "virtual environments": virt_env()}
write_yaml(a)
write_json(a)
