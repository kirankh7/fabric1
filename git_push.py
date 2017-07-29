from fabric.api import local

def git_deploy():
    local("echo 'Kiran Haridas'")
    local("git add -p && git commit")
    local("git push origin master")

git_deploy()