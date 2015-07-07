# jnettop

Forked version of jnettop with ClearOS changes applied

## Update usage
  Add __#kojibuild__ to commit message to automatically build

* git clone git+ssh://git@github.com/clearos/jnettop.git
* cd jnettop
* git checkout master
* git remote add upstream git://pkgs.fedoraproject.org/jnettop.git
* git pull upstream master
* git checkout clear7
* git merge --no-commit master
* git commit
