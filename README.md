# ar_os_environment
Ansible Role for setting up environment variables 

## Requirements
The following packages must be installed on the Ansible control host:
- expect (only required if using secured ssh keys - wip)
- git (>= 1.8)

## Role Variables
The following details:
- the parameters that should be passed to the role (aka vars)
- the defaults that are held
- the secrets that should generally be sourced from an ansible vault.

### Parameters:
| Variable                           | Description                                                                                                                                 | Default        |
| --------                           | -----------                                                                                                                                 | -------        |
| ar_os_environment_git_repo         | Remote location of the git repository                                                                                                       | null (invalid) |
| ar_os_environment_git_ssh_key      | Base 64 encoded ssh key to use to access the git repository                                                                                 | null (invalid) |
| ar_os_environment_git_ssh_key_pass | The passphrase for the ssh key (wip)                                                                                                        | null           |
| ar_os_environment_name             | The name of the environment                                                                                                                 | null (invalid) |
| ar_os_environment_git_comment      | A comment to pass though if changes are committed                                                                                           | ''             |
| ar_os_environment_git_version      | The version of the repository (branch, tag or commit hash note only a branch will be able to have changes committed back to the repository) | 'master'       |


### Defaults
| Variable                        | Description                                                                      | Default                                                                                           |
| --------                        | -----------                                                                      | -------                                                                                           |
| ar_os_environment_assertions    | List of assertions made before execution                                         | ar_os_environment_git_repo, ar_os_environment_name and ar_os_environment_git_ssh_key are provided |
| ar_os_environment_varsdir       | Relative location of vars files                                                  | 'varfiles'                                                                                        |
| ar_os_environment_app_varsfile  | Name of the var file containing environment variables                            | 'app-environment.yml'                                                                             |
| ar_os_environment_app_vaultfile | Name of the vault file containing environment secrets                            | 'app-environment.vault'                                                                           |
| ar_os_environment_git_subdir    | Name of the git repository sub directory that the automation can make changes to | '.'                                                                                               |

### Secrets
The following variables should be provided through an encrypted source:
- ar_os_environment_git_ssh_key
- ar_os_environment_git_ssh_key_pass

### External variables
The following external variables are defined for use outside of this 
role:

| Variable              | Description                                                           | Default                                            |
| --------              | -----------                                                           | -------                                            |
| envdir                | Absolute path to the enviroonment directory holding an specific files | '<git checkout location>/<environment name>'       |
| phase_base_dir        | Another name for envdir                                               | '<envdir>'                                         |
| deployment_phase      | Another name for environment                                          | '<environment name>'                               |
| generated_config_path | Location where to generate environment working files                  | '<envdir>/generated'                               |
| varfiles_dir          | Location of environment var files                                     | '<phase_base_dir>/varfiles'                        |
| local_cert_path       | Location for certificate files                                        | '<generated_config_path>/certs'                    |
| local_key_path        | (Temporary) Location for key files                                    | '<user home>/keys/local'                           |
| app_vault_file_name   | Location for the environment vault file                               | '<varfiles_dir>/<ar_os_environment_app_vaultfile>' |

## Dependencies

- ar_git_repo

## Example Playbook

```
- hosts: localhost
  tasks:
    - name: Get the environment variables
      include_role:
        name: ar_os_environment
      vars:
        ar_os_environment_name:        "DEV"
        ar_os_environment_git_ssh_key: "LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyW..."
        ar_os_environment_git_repo:    "git@git-host:group/repo.git"
        ar_os_environment_git_version: "master"
```

## License

MIT / BSD

## Author Information

This role was created in 2020 by David Stewart (dstewart@redhat.com)
