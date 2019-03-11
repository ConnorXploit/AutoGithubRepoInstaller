from subprocess import Popen, PIPE

dependencies_list = ['curl', 'conda', 'git']

anaconda_source='-O https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh'

opciones_menu = {
    '0':'Clone Github Repositorie', 
    '1':'Update a Repositorie', 
    '2':'Update All Repositories'
}

apt = 'sudo apt-get install -y'
update = 'sudo apt-get update -y'

install_type = {
    'curl':apt,
    'conda':'curl',
    'git':apt
}

arguments_package = {
    'conda':anaconda_source
}

python_version = ''
repositories_dir = ''

def cloneRepo(repository, repositories_directory):
    # Clone the repo on the repo directory install dir
    pass

def installRepo(repository):
    # Look for setup.py, requirements, etc.
    pass

def createPythonEnvironment(repository, name):
    pass

def directoryRepositories(repositories_directory):
    pass

def listCondaEnvironments():
    list = execute('conda env list','')

def installTypePackage(package):
    argument = ''
    if not arguments_package[package]:
        argument = package
    else:
        argument = arguments_package[package]
    return install_type[package], argument

def execute(command, args):
    print('Ejecutando: {} {}'.format(command, args))
    result = ''
    try:
        with Popen('{} {}'.format(command, args), stdout=PIPE, universal_newlines=True, shell=True) as process:
            for line in process.stdout:
                result = '{}\n{}'.format(result, line)
        #result = subprocess.run('{} {}'.format(command, args), shell=True)
    except Exception as e:
        print('[ERROR] - {} {} - {}'.format(command, args, str(e)))
    return result

def verifyDependencies(command, arguments=''):
    print('Verificando {} {}'.format(command, arguments))
    result = execute(command, arguments)
    if not isinstance(result, str):
        if not result.returncode == 0:
            print('No está instalado {}'.format(command))
            install, name = installTypePackage(command)
            result2 = execute(install, name)
            if result2.returncode == 0:
                verifyDependencies(command, arguments)
            else:
                print('Algo ha ido mal con la instalacion {} {}'.format(install, name))
    else:
        print('{}'.format(result))
def resolveDependencies():
    for dep in dependencies_list:
        print('Comprobando dependencias de {}'.format(dep))
        verifyDependencies(dep, '--version')

def start():
    resolveDependencies()
    listCondaEnvironments()

def menu():
    print('''
        GitHub Repositories Auto Cloner & Installer Tool

        Created by Connor
    ''')
    start()

menu()
