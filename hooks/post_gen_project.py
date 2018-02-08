import os
import shutil

MOLECULE_PATH = 'molecule/{{ cookiecutter.scenario_name }}'
if '{{ cookiecutter.enable_openshift_testing }}':
    if '{{ cookiecutter.ops_roles_path }}' != "":
        os.symlink('{{ cookiecutter.ops_roles_path }}', "%s/ops_roles" % MOLECULE_PATH)
    if '{{ cookiecutter.tools_roles_path }}' != "":
        os.symlink('{{ cookiecutter.tools_roles_path }}', "%s/tools_roles" % MOLECULE_PATH)
    if '{{ cookiecutter.private_roles_path }}' != "":
        os.symlink('{{ cookiecutter.private_roles_path }}', "%s/private_roles" % MOLECULE_PATH)
else:
    shutil.rmtree(MOLECULE_PATH+'/files')
    shutil.rmtree(MOLECULE_PATH+'/.molecule/files')
