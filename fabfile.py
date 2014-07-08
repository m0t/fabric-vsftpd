from fabric.api import run
#assuming a ubuntu installation
def deploy():
    run("apt-get install -y vsftpd")
    run("mkdir -p /srv/data/myftp")
    run("chmod 777 /srv/data/myftp")
    run("sed -i \"s/\#write_enable=YES/write_enable=YES/\" /etc/vsftpd.conf")
    run("echo 'local_root=/srv/data/myftp' >>/etc/vsftpd.conf")
    run("service vsftpd restart")